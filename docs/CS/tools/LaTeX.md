# LaTeX

[官方教学文档](https://cn.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)

[LaTeX 新手教程（知乎）](https://zhuanlan.zhihu.com/p/456055339)

[LaTeX 详细教程 + 技巧总结（CSDN）](https://blog.csdn.net/NSJim/article/details/109066847)

[希腊字母与 LaTeX 命令对照表](https://www.xilazimu.net/m/articles/greek_letter_latex.html)

## 环境与组件

LaTeX 环境与 C、Python 环境的对应关系：

| 组件 | LaTeX 环境 | C 语言环境 | Python 环境 |
|------|------------|------------|-------------|
| 环境 | TeX Live | MinGW | Python 3.x |
| 功能 | LaTeX 编译器、宏包、字体 | C 编译器 (gcc)、标准库 | Python 解释器、标准库 |
| IDE | VSCode | DevC++ / VSCode | PyCharm / VSCode |
| VSCode 插件 | LaTeX Workshop | C/C++ | Python、Pylance、Python Debugger |

编辑 LaTeX 文档需要安装 TeX Live；编辑 C 代码需要 MinGW（含 gcc、gdb、make）；运行 Python 需要 Python 3.x 解释器与 pip。

## 矩阵
1. **一般矩阵**：
   ```markdown
   $$
   \begin{bmatrix}
   a & b \\
   c & d
   \end{bmatrix}
   $$
   ```
   这将生成一个2x2的矩阵。

2. **方阵**：
   ```markdown
   $$
   \begin{pmatrix}
   a & b & c \\
   d & e & f \\
   g & h & i
   \end{pmatrix}
   $$
   ```
   这将生成一个3x3的方阵。

3. **圆括号包围的矩阵**：
   ```markdown
   $$
   \begin{pmatrix}
   a & b \\
   c & d
   \end{pmatrix}
   $$
   ```

4. **花括号包围的矩阵**（通常用于集合论）：
   ```markdown
   $$
   \left\{
   \begin{array}{cc}
   a & b \\
   c & d
   \end{array}
   \right\}
   $$
   ```

5. **带框的矩阵**：
   ```markdown
   $$
   \begin{array}{cc}
   a & b \\
   c & d
   \end{array}
   $$
   ```

6. **斜体矩阵**（用于表示变换矩阵）：
   ```markdown
   $$
   \mathbf{A} = \begin{pmatrix}
   a & b \\
   c & d
   \end{pmatrix}
   $$
   ```

7. **转置矩阵**：
   ```markdown
   $$
   \mathbf{A}^T = \begin{pmatrix}
   a & c \\
   b & d
   \end{pmatrix}
   $$
   ```
 ^a07424
8. **行列式**：
   ```markdown
   $$
   \det(\mathbf{A}) = \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
   $$
   ```
9. **迹**（矩阵对角线元素之和）：
   ```markdown
   $$
   \text{tr}(\mathbf{A}) = a + d
   $$
   ```
10. **逆矩阵**：
    ```markdown
    $$
    \mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{pmatrix}
    d & -b \\
    -c & a
    \end{pmatrix}
    $$
    ```

## 希腊字母
小写的希腊字母:

| 小写  | LaTex命令     |
| --- | ----------- |
| α   | \alpha      |
| β   | \beta       |
| γ   | \gamma      |
| δ   | \delta      |
| ε   | \varepsilon |
| η   | \eta        |
| θ   | \theta      |
| ι   | \iota       |
| κ   | \kappa      |
| λ   | \lambda     |
| μ   | \mu         |
| ν   | \nu         |
| ξ   | \xi         |
| ο   | \o          |
| π   | \pi         |
| ρ   | \rho        |
| σ   | \sigma      |
| τ   | \tau        |
| υ   | \upsilon    |
| φ   | \varphi     |
| χ   | \chi        |
| ψ   | \psi        |
| ω   | \omega      |

大写的希腊字母:

|大写|LaTex|
|---|---|
|Γ|\Gamma|
|Δ|\Delta|
|Θ|\Theta|
|∧|\Lambda|
|Ξ|\Xi|
|∏|\Pi|
|∑|\Sigma|
|Υ|\Upsilon|
|Φ|\Phi|
|Ψ|\Psi|
|Ω|\Omega|

通过对比以上左右两侧的内容，可以发现LaTex表达式完全借助了希腊字母的英文标识，我们可以回到[首页](http://www.xilazimu.net/)查看[英文]列，一看就明白了。

> 补充:下图可以方便大家保存到手机或电脑

![](https://www.xilazimu.net/static/xilazimu/xlzm_upload/images/greek_letter_latex_00.jpg)

$\alpha$ α
$\xi$

eee输入法：输入xxxl就会生成希腊字母输入法