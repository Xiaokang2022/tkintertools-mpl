"""APIs for Matplotlib"""

import tkinter

import matplotlib
import matplotlib.backends._backend_tk
import matplotlib.backends.backend_tkagg
import matplotlib.figure
import mpl_toolkits.mplot3d
import tkintertools.style.manager
import tkintertools.toolbox.tools

from .constants import DARK_THEME, LIGHT_THEME

__all__ = [
    "FigureCanvas",
    "FigureToolbar",
    "set_mpl_default_theme",
    "DARK_THEME",
    "LIGHT_THEME",
]


class FigureCanvas(tkinter.Canvas, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
    """A canvas for interface of `matplotlib`"""

    def __init__(
        self,
        figure: matplotlib.figure.Figure,
        master: tkinter.Misc,
        *args,
        **kwargs,
    ) -> None:
        """
        * `figure`: a `Figure` object from `matplotlib`
        * `master`: parent widget
        """
        self.figure = figure
        self._TkAgg: matplotlib.backends.backend_tkagg.FigureCanvasTkAgg = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(
            figure, master)

        tkintertools.toolbox.tools._forward_methods(
            self._TkAgg._tkcanvas, self)
        tkintertools.toolbox.tools._forward_methods(self._TkAgg, self)

        self.configure(*args, **kwargs)
        self.bind("<Configure>", self._fix_size, "+")
        tkintertools.style.manager.register_event(self._theme)
        self._theme(tkintertools.style.manager.get_color_mode() == "dark")

    def _fix_size(self, event: tkinter.Event) -> None:
        """Correct the size of Figure"""
        self.update()
        self.resize(event)

    def _theme(self, dark: bool) -> None:
        """Change the color theme of the Figure"""
        self.update()
        for key, value in DARK_THEME.items() if dark else LIGHT_THEME.items():
            keys = key.split(".")
            match keys[0]:
                case "figure": self.figure.set(**{keys[-1]: value})
                case "grid":
                    for axes in self.figure.axes:
                        # if getattr(axes.xaxis, "_gridOnMinor", None):  # BUG: It not work now
                        axes.grid(color=value)
                case "axes3d":
                    for axes in self.figure.axes:
                        if isinstance(axes, mpl_toolkits.mplot3d.Axes3D):
                            getattr(axes, keys[1]).set(pane_color=value)
                case "axes":
                    for axes in self.figure.axes:
                        if keys[-1] == "labelcolor":
                            for attr in ("xaxis", "yaxis", "zaxis") if isinstance(axes, mpl_toolkits.mplot3d.Axes3D) else ("xaxis", "yaxis"):
                                getattr(axes, attr).label.set_color(value)
                        elif keys[-1] == "titlecolor":
                            axes.title.set_color(value)
                        else:
                            axes.patch.set(**{keys[-1]: value})
                case "xtick":
                    for axes in self.figure.axes:
                        for attr in ("xaxis", "yaxis", "zaxis") if isinstance(axes, mpl_toolkits.mplot3d.Axes3D) else ("xaxis",):
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
        self.draw()

    # @typing.override
    def destroy(self) -> None:
        self.figure.clf()
        tkintertools.style.manager.remove_event(self._theme)
        return self._TkAgg.get_tk_widget().destroy()


class FigureToolbar(matplotlib.backends._backend_tk.NavigationToolbar2Tk):
    """An interface class for the matplotlib navigation cursor"""

    def __init__(
        self,
        canvas: FigureCanvas,
        master: tkinter.Misc | FigureCanvas | None = None,
        *,
        pack_toolbar: bool = True,
        **kwargs,
    ) -> None:
        """
        * `canvas`: the figure canvas on which to operate
        * `master`: parent widget
        * `pack_toolbar`: if True, add the toolbar to the parent's pack manager's packing
        list during initialization with `side="bottom"` and `fill="x"`.

        TIPS:

        If you want to use the toolbar with a different layout manager, use `pack_toolbar=False`
        """
        if isinstance(master, FigureCanvas):
            master = master._TkAgg._tkcanvas
        matplotlib.backends._backend_tk.NavigationToolbar2Tk.__init__(
            self, canvas._TkAgg, master, pack_toolbar=pack_toolbar)
        self.configure(**kwargs)
        self.update()
        tkintertools.style.manager.register_event(self._theme)
        self._theme(tkintertools.style.manager.get_color_mode() == "dark")

    def _theme(self, dark: bool) -> None:
        """Change the color theme of the Toolbar"""
        if dark:
            self["bg"] = "#303030"
            for name, child in self.children.items():
                child["bg"] = "#303030"
                if name.startswith("!label"):
                    child["fg"] = "#F1F1F1"
        else:
            self["bg"] = "#F0F0F0"
            for name, child in self.children.items():
                child["bg"] = "#F0F0F0"
                if name.startswith("!label"):
                    child["fg"] = "#F1F1F1"

    # @typing.override
    def destroy(self) -> None:
        tkintertools.style.manager.remove_event(self._theme)
        return matplotlib.backends._backend_tk.NavigationToolbar2Tk.destroy(self)


def set_mpl_default_theme(dark: bool) -> None:
    """
    Set default color constants of `matplotlib`

    * `dark`: Wether it is dark mode
    """
    for key, value in DARK_THEME.items() if dark else LIGHT_THEME.items():
        matplotlib.rcParams[key] = value
