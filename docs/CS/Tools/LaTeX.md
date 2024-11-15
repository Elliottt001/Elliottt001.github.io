[LaTeX新手教程-知乎](https://zhuanlan.zhihu.com/p/456055339)
[LaTeX详细教程+技巧总结-CSDN博客](https://blog.csdn.net/NSJim/article/details/109066847?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522DDE21D5F-09C5-4831-9600-120D6CEF2094%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=DDE21D5F-09C5-4831-9600-120D6CEF2094&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-109066847-null-null.142^v100^pc_search_result_base4&utm_term=latex&spm=1018.2226.3001.4187)
[直接查看第二篇博客中的LaTex数学公式部分](https://blog.csdn.net/NSJim/article/details/109045914)

[希腊字母和LaTeX命令对照表](https://www.xilazimu.net/m/articles/greek_letter_latex.html)
在Markdown中生成矩阵，你可以使用LaTeX语法，因为Markdown本身不支持复杂的数学公式排版，但很多Markdown编辑器和渲染器支持LaTeX语法。以下是一些矩阵的LaTeX表示方法：

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
