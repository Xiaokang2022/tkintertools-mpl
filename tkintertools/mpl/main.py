"""APIs for Matplotlib"""

import inspect
import tkinter
import typing

import matplotlib
import matplotlib.backends._backend_tk
import matplotlib.backends.backend_tkagg
import matplotlib.figure
import mpl_toolkits.mplot3d
import typing_extensions
from tkintertools.core import constants
from tkintertools.style import manager

from . import _constants

__all__ = [
    "FigureCanvas",
    "FigureToolbar",
    "set_mpl_default_theme",
]


def _forward_methods(
    source_object: object | type,
    target_object: object,
) -> None:
    """
    Forward methods and attributes of one object to another object

    * `source_object`: the source object, that is, the forwarded object
    * `target_object`: the target object, that is, the object to be forwarded
    """
    if inspect.isclass(source_object):
        source_object = source_object.__class__
    for name, value in inspect.getmembers(source_object, inspect.ismethod):
        setattr(target_object, name, value)
    for name, value in inspect.getmembers(source_object, inspect.isfunction):
        setattr(target_object, name, value)


class FigureCanvas(
        tkinter.Canvas, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
    """A canvas for interface of `matplotlib`"""

    def __init__(
        self,
        master: tkinter.Misc,
        figure: matplotlib.figure.Figure,
        *args,
        **kwargs,
    ) -> None:
        """
        * `master`: parent widget
        * `figure`: a `Figure` object from `matplotlib`
        """
        self.figure = figure
        self._TkAgg: matplotlib.backends.backend_tkagg.FigureCanvasTkAgg \
            = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master)

        _forward_methods(self._TkAgg._tkcanvas, self)
        _forward_methods(self._TkAgg, self)

        self.configure(*args, **kwargs)
        self.bind("<Configure>", self._fix_size, "+")
        manager.register_event(self._theme)
        self._theme(manager.get_color_mode() == "dark")

    def _fix_size(self, event: tkinter.Event) -> None:
        """Correct the size of Figure"""
        self.update()
        self.resize(event)

    def _theme(self, dark: bool) -> None:
        """Change the color theme of the Figure"""
        self.update()
        style = _constants.DARK_THEME if dark else _constants.LIGHT_THEME

        for key, value in style.items():
            keys = key.split(".")

            match keys[0]:
                case "figure":
                    self.figure.set(**{keys[-1]: value})
                case "grid":
                    for axes in self.figure.axes:
                        # NOTE: A private approach is used,
                        # and there may be issues in future releases
                        if axes.xaxis._major_tick_kw["gridOn"]:
                            axes.grid(color=value)
                case "axes3d":
                    for axes in self.figure.axes:
                        if isinstance(axes, mpl_toolkits.mplot3d.Axes3D):
                            getattr(axes, keys[1]).set(pane_color=value)
                case "axes":
                    for axes in self.figure.axes:
                        if keys[-1] == "labelcolor":
                            for attr in (
                                ("xaxis", "yaxis", "zaxis")
                                if isinstance(axes, mpl_toolkits.mplot3d.Axes3D)
                                else ("xaxis", "yaxis")
                            ):
                                getattr(axes, attr).label.set_color(value)
                        elif keys[-1] == "titlecolor":
                            axes.title.set_color(value)
                        else:
                            axes.patch.set(**{keys[-1]: value})
                case "xtick":
                    for axes in self.figure.axes:
                        for attr in (
                            ("xaxis", "yaxis", "zaxis")
                            if isinstance(axes, mpl_toolkits.mplot3d.Axes3D)
                            else ("xaxis",)
                        ):
                            if keys[-1] == "color":
                                getattr(axes, attr).set_tick_params(
                                    colors=value)
                                for k, spine in axes.spines.items():
                                    if k in ("top", "bottom"):
                                        spine.set_color(value)
                case "ytick":
                    for axes in self.figure.axes:
                        if not isinstance(axes, mpl_toolkits.mplot3d.Axes3D):
                            if keys[-1] == "color":
                                axes.yaxis.set_tick_params(colors=value)
                                for k, spine in axes.spines.items():
                                    if k in ("right", "left"):
                                        spine.set_color(value)
        self.draw_idle()

    @typing_extensions.override
    def destroy(self) -> None:
        for axis in self.figure.get_axes():
            axis.cla()
        self.figure.clf()
        manager.remove_event(self._theme)
        return self._TkAgg.get_tk_widget().destroy()


class FigureToolbar(matplotlib.backends._backend_tk.NavigationToolbar2Tk):
    """An interface class for the matplotlib navigation cursor"""

    def __init__(
        self,
        master: tkinter.Misc | FigureCanvas,
        figure_canvas: FigureCanvas | None = None,
        *,
        pack_toolbar: bool = True,
        **kwargs,
    ) -> None:
        """
        * `master`: parent widget
        * `figure_canvas`: the figure canvas on which to operate
        * `pack_toolbar`: if True, add the toolbar to the parent's pack
        manager's packing list during initialization with `side="bottom"` and
        `fill="x"`.

        TIPS:

        If you want to use the toolbar with a different layout manager,
        use `pack_toolbar=False`
        """
        if figure_canvas is None:
            figure_canvas = master
        if isinstance(master, FigureCanvas):
            master = master._TkAgg._tkcanvas
        matplotlib.backends._backend_tk.NavigationToolbar2Tk.__init__(
            self, figure_canvas._TkAgg, master, pack_toolbar=pack_toolbar
        )
        self.configure(**kwargs)
        self.update()
        manager.register_event(self._theme)
        self._theme(manager.get_color_mode() == "dark")

    def _theme(self, dark: bool) -> None:
        """Change the color theme of the Toolbar"""
        if dark:
            self["bg"] = "#303030"
            for name, child in self.children.items():
                child["bg"] = self["bg"]
                if name.startswith("!label"):
                    child["fg"] = "#F1F1F1"
                elif name.startswith("!frame"):
                    child["bg"] = "#565656"
                else:
                    child["fg"] = "#D3D3D3"

        else:
            self["bg"] = "#F0F0F0"
            for name, child in self.children.items():
                child["bg"] = self["bg"]
                if name.startswith("!label"):
                    child["fg"] = "#000000"
                elif name.startswith("!frame"):
                    child["bg"] = "#A9A9A9"
                else:
                    child["fg"] = "#000000"

        self._rescale()

    @typing_extensions.override
    def destroy(self) -> None:
        manager.remove_event(self._theme)
        return matplotlib.backends._backend_tk.NavigationToolbar2Tk.destroy(
            self)


def set_mpl_default_theme(
    theme: typing.Literal["light", "dark"],
    *,
    apply_font: bool = False,
) -> None:
    """
    Set default color constants of `matplotlib`

    * `theme`: theme mode
    * `apply_font`: whether to use the font of `tkintertools`
    """
    for key, value in _constants.DARK_THEME.items() \
            if theme == "dark" else _constants.LIGHT_THEME.items():
        matplotlib.rcParams[key] = value
    if apply_font:
        matplotlib.rcParams['axes.unicode_minus'] = False
        matplotlib.rcParams["font.family"] = constants.FONT
