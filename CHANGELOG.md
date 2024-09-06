Changelog / 更新日志
===================

> [!TIP]  
> This changelog has the following 7 types of updates, each of which is represented by 7 different colors  
> 此更新日志有以下 7 中类型的更新内容，分别用 7 中不同颜色来表示
> 
> * 🟢 **Added / 新增**
> * 🔴 **Removed / 移除**
> * 🟡 **Changed / 变更**
> * 🔵 **Optimized / 优化**
> * 🟣 **Fixed / 修复**
> * 🟠 **Deprecated / 弃用**
> * 🟤 **Refactored / 重构**

🔖 `1.0.1`
----------

🕓 *Release Date / 发布日期 : 2024-09-06*

🟢 **Added / 新增**

- A new mechanism has been added to determine whether `grid` is enabled or not, so that the grid color can be automatically adapted to the theme  
新增了 `grid` 是否开启的判定机制，使得网格颜色可以自动对主题进行适配

🟡 **Changed / 变更**

- Now requires `matplotlib` version `>= 3.7.0`  
现在要求 `matplotlib` 版本 `>= 3.7.0`

🔵 **Optimized / 优化**

- The icon color of the button adapts to the dark theme  
按钮的图标颜色适配了暗色主题

🟣 **Fixed / 修复**

- Fixed the bug that the real-time coordinate information of the mouse was not displayed under the bright color theme  
修复亮色主题下鼠标实时坐标信息不显示的 bug

🔖 `1.0.0`
----------

🕓 *Release Date / 发布日期 : 2024-08-07*

🟤 **Refactored / 重构**

- Completed the project detached from `tkintertools` and refactored to be compatible  
完成了项目从 `tkintertools` 的分离，并重构以兼容
