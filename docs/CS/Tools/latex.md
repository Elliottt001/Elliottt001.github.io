[官方教学文档](https://cn.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)

都2025年了为什么还有人不会用 LaTex ？！

你是否苦于学术论文中公式特别难敲？

你是否苦于期末论文中排版特别费事？

万恶之源，就是 word！

只要你学会了latex，就可以摆脱word~

## 原理部分

以下是 LaTeX 环境（TeX Live、VSCode）与 C 语言环境（MinGW、DevC++）以及 Python 环境（PyCharm）的对应关系表格：

| **组件**         | **LaTeX 环境**       | **C 语言环境**       | **Python 环境**      |
|------------------|----------------------|----------------------|----------------------|
| **环境**     | TeX Live             | MinGW                | Python3.x       |
| **功能**         | 提供 LaTeX 编译器、宏包、字体等 | 提供 C 编译器（gcc）、标准库等 | 提供 Python 解释器、标准库等 |
| **IDE（集成开发环境）**       | VSCode | DevC++/VSCode | PyCharm/VSCode |
| **VSCode插件**     | LaTeX Workshop | C/C++   | Python、Pylance、Python Debugger |

具体来说，要在电脑上编写并运行C/C++代码，就需要 C 语言环境，MinGW 就包含C语言编译器 GCC、调试工具 GDB、自动化构建工具Make。

要在电脑上运行python代码，就需要python解释器Python 3.x、python包（用pip3管理）
同理，要在电脑上编写latex文档，就需要 TeX Live

![alt text](image.png)