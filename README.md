<h1 align="center">tkintertools-mpl</h1>

<p align="center"><a title="Official Website" href="https://xiaokang2022.github.io/tkintertools/">https://xiaokang2022.github.io/tkintertools/</a></p>

<p align="center">Extension package of <code>tkintertools</code> for <code>matplotlib</code></p>

<p align="center">
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/releases"><img alt="Version" src="https://img.shields.io/github/v/release/Xiaokang2022/tkintertools-mpl?include_prereleases&logo=github&label=Version" title="Latest Version" /></a>
<a href="https://pypistats.org/packages/tkintertools-mpl"><img alt="Downloads" src="https://img.shields.io/pypi/dm/tkintertools-mpl?label=Downloads&logo=pypi&logoColor=skyblue" title="Downloads" /></a>
<a href="https://pepy.tech/project/tkintertools-mpl"><img alt="Total Downloads" src="https://img.shields.io/pepy/dt/tkintertools-mpl?logo=pypi&logoColor=gold&label=Total%20Downloads" title="Total Downloads" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl"><img alt="Size" src="https://img.shields.io/github/languages/code-size/Xiaokang2022/tkintertools-mpl?label=Size&logo=github" title="Code Size"/></a>
<br/>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/watchers"><img alt="Watchers" src="https://img.shields.io/github/watchers/Xiaokang2022/tkintertools-mpl?label=Watchers&logo=github&style=flat" title="Watchers" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/forks"><img alt="Forks" src="https://img.shields.io/github/forks/Xiaokang2022/tkintertools-mpl?label=Forks&logo=github&style=flat" title="Forks" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Xiaokang2022/tkintertools-mpl?label=Stars&color=gold&logo=github&style=flat" title="Stars" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Xiaokang2022/tkintertools-mpl?label=Issues&logo=github" title="Issues" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Xiaokang2022/tkintertools-mpl?label=Pull%20Requests&logo=github" title="Pull Requests" /></a>
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/Xiaokang2022/tkintertools-mpl?label=Discussions&logo=github" title="Discussions" /></a>
</p>

<p align="center">
<a href="https://github.com/Xiaokang2022/tkintertools-mpl/pulse"><img alt="Insights" src="https://repobeats.axiom.co/api/embed/16b936d7774f2727ca057af76b700997a60c9b67.svg" /></a>
</p>

<p align="center">
    <a href="https://star-history.com/#Xiaokang2022/tkintertools-mpl&Date">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Xiaokang2022/tkintertools-mpl&type=Date&theme=dark" />
            <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Xiaokang2022/tkintertools-mpl&type=Date" />
            <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Xiaokang2022/tkintertools-mpl&type=Date" />
        </picture>
    </a>
</p>

📦 Installation
---------------

```shell
pip install tkintertools-mpl
```

### 👀 Preview

![preview-1](./preview-1.png)

```python
import math

import matplotlib.figure
import numpy

import tkintertools
from tkintertools import mpl, theme

mpl.set_mpl_default_theme(theme.get_color_mode())

x = numpy.linspace(-math.tau, math.tau, 100)
y = numpy.sin(x)

figure = matplotlib.figure.Figure()
axes = figure.add_subplot()
axes.plot(x, y)

axes.set(xlabel='x', ylabel='y', title='Plotting based on the theme in tkt')
axes.legend(["$y=sin(x)$"])
axes.grid()

root = tkintertools.Tk((960, 720), title="tkintertools-mpl")
root.center()
canvas = tkintertools.Canvas(auto_zoom=True)
canvas.place(width=960, height=720)
figure_canvas = mpl.FigureCanvas(canvas, figure)
toolbar = mpl.FigureToolbar(canvas, figure_canvas)
figure_canvas.pack(side="top", fill="both", expand=True)

root.mainloop()
```

![preview-2](./preview-2.png)

```python
import matplotlib.figure
import numpy

import tkintertools
from tkintertools import mpl, theme

mpl.set_mpl_default_theme(theme.get_color_mode())

figure = matplotlib.figure.Figure()
axes = figure.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]

for c, k in zip(colors, yticks):
    xs = numpy.arange(20)
    ys = numpy.random.rand(20)
    cs = [c] * len(xs)
    cs[0] = 'c'
    axes.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.7)

axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')
axes.set_title("3D plotting with interoperability")

axes.set_yticks(yticks)

root = tkintertools.Tk((960, 720), title="tkintertools-mpl")
root.center()
canvas = tkintertools.Canvas(auto_update=True)
canvas.place(width=960, height=720)
figure_canvas = mpl.FigureCanvas(canvas, figure)
toolbar = mpl.FigureToolbar(canvas, figure_canvas)
figure_canvas.pack(side="top", fill="both", expand=True)

root.mainloop()
```
