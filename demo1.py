import matplotlib.figure as figure
import numpy
import tkintertools.style as style

import tkintertools as tkt
import tkintertools.mpl as mpl

mpl.set_mpl_default_theme(style.get_color_mode() == "dark")

t = numpy.arange(0.0, 2.0, 0.01)
s = 1 + numpy.sin(2 * numpy.pi * t)

fig = figure.Figure()
ax = fig.add_subplot()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Plotting based on the theme in tkt')
ax.grid()
ax.legend(["y=sin(x)"])

root = tkt.Tk((960, 720), title="tkintertools-mpl")
root.center()
canvas = tkt.Canvas(root, zoom_item=True)
canvas.place(width=960, height=720)
figure_canvas = mpl.FigureCanvas(fig, canvas)
toolbar = mpl.FigureToolbar(figure_canvas, canvas)
figure_canvas.pack(side="top", fill="both", expand=True)

root.mainloop()
