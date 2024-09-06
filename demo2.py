import matplotlib.figure as figure
import numpy
import tkintertools.style as style

import tkintertools as tkt
import tkintertools.mpl as mpl

mpl.set_mpl_default_theme(style.get_color_mode() == "dark")

fig = figure.Figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]

for c, k in zip(colors, yticks):
    xs = numpy.arange(20)
    ys = numpy.random.rand(20)
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D plotting with interoperability")

ax.set_yticks(yticks)

root = tkt.Tk((960, 720), title="tkintertools-mpl")
root.center()
canvas = tkt.Canvas(root, zoom_item=True)
canvas.place(width=960, height=720)
figure_canvas = mpl.FigureCanvas(fig, canvas)
toolbar = mpl.FigureToolbar(figure_canvas, canvas)
figure_canvas.pack(side="top", fill="both", expand=True)

root.mainloop()
