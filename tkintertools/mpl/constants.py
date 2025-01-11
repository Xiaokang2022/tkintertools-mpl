"""Constants for theme"""

from __future__ import annotations

DARK_THEME: dict[str, str] = {
    "axes.edgecolor": "#AAAAAA",  # outline
    "axes.facecolor": "#202020",  # internal
    "axes.labelcolor": "#CCCCCC",  # label
    "axes.titlecolor": "#CCCCCC",  # title

    "axes3d.xaxis.panecolor": "#2A2A2A",  # x pane
    "axes3d.yaxis.panecolor": "#2A2A2A",  # y pane
    "axes3d.zaxis.panecolor": "#2A2A2A",  # z pane

    # "figure.edgecolor": "#202020",
    "figure.facecolor": "#202020",  # external

    "legend.edgecolor": "#707070",  # outline
    "legend.facecolor": "#202020",  # internal
    "legend.labelcolor": "#CCCCCC",  # label

    "grid.color": "#505050",  # grid
    "text.color": "#CCCCCC",  # text

    "xtick.color": "#CCCCCC",  # ruler (3D)
    "xtick.labelcolor": "#CCCCCC",  # scale (3D)
    "ytick.color": "#CCCCCC",  # ruler
    "ytick.labelcolor": "#CCCCCC",  # scale
}

LIGHT_THEME: dict[str, str] = {
    "axes.edgecolor": "#2A2A2A",
    "axes.facecolor": "#FFFFFF",
    "axes.labelcolor": "#000000",
    "axes.titlecolor": "#000000",

    "axes3d.xaxis.panecolor": "#F5F5F5",
    "axes3d.yaxis.panecolor": "#F5F5F5",
    "axes3d.zaxis.panecolor": "#F5F5F5",

    # "figure.edgecolor": "#FFFFFF",
    "figure.facecolor": "#FFFFFF",

    "legend.edgecolor": "#D6D6D6",
    "legend.facecolor": "#FFFFFF",
    "legend.labelcolor": "#000000",

    "grid.color": "#BDBDBD",
    "text.color": "#000000",

    "xtick.color": "#000000",
    "xtick.labelcolor": "#000000",
    "ytick.color": "#000000",
    "ytick.labelcolor": "#000000",
}
