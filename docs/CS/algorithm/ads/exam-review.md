## Data Structure

[时间复杂度详解](https://chatgpt.com/c/69107885-8d20-832e-bc2a-23ba5805abca)

### AVL Tree

时间复杂度：

| 操作         | 平均复杂度         | 最坏复杂度         | 说明                         |
| ---------- | ------------- | ------------- | -------------------------- |
| 查找（Search） | \( O(\log n) \) | \( O(\log n) \) | 和普通 BST 一样，沿树高查找           |
| 插入（Insert） | \( O(\log n) \) | \( O(\log n) \) | 查找插入点 + 回溯更新平衡因子 + 最多旋转常数次 |
| 删除（Delete） | \( O(\log n) \) | \( O(\log n) \) | 查找删除节点 + 回溯调整，可能逐层旋转    |

![alt text](res/images/94380a89b8d8269cd972af3efd51b339.jpg)

AVL 树是一种 BST，插入删除都遵循 BST 的规则

BF（Balance Factor，平衡因子）是左子树高度减去右子树高度

### Splay Tree

Splay Tree 也是 BST
   

### Red-Black Tree

时间复杂度：

| 操作                           | 平均复杂度         | 最坏复杂度         | 摊销复杂度         | 说明                   |
| ---------------------------- | ------------- | ------------- | ------------- | -------------------- |
| 查找（Search）                   | \( O(\log n) \) | \( O(\log n) \) | \( O(\log n) \) | 按 BST 性质沿树高查找        |
| 插入（Insert）                   | \( O(\log n) \) | \( O(\log n) \) | \( O(\log n) \) | 查找插入点 + 修复平衡（≤2次旋转）  |
| 删除（Delete）                   | \( O(\log n) \) | \( O(\log n) \) | \( O(\log n) \) | 查找删除节点 + 修复平衡（≤3次旋转） |
| 最小值/最大值（Min/Max）             | \( O(\log n) \) | \( O(\log n) \) | \( O(\log n) \) | 走一条路径                |
| 前驱/后继（Predecessor/Successor） | \( O(\log n) \) | \( O(\log n) \) | \( O(\log n) \) | 类似查找                 |

![alt text](res/images/ab7615cb7c294c3edd3a5e89f0cedfaa.jpg)

红黑树也是 BST

红黑树的插入：

![alt text](res/images/a324bd8a4410a78ec4d84ee93db7ad17.jpg)

注意：

1. 别忘 NIL，这也是黑色节点，有可能作为叔叔
2. 只有红黑树性质被破坏才调整

红黑树的删除：

![alt text](image.png)

![alt text](res/images/4635980aef6b25b3f7440ae2e9e5734c.jpg)

### B Plus Tree

!!! warning ""

    ZJU 版本B+树和正经B+树不一样，做题按照 ZJU 版本，叶子节点关键字范围：$⌈M/2⌉ ≤ keys ≤ M$

时间复杂度：

| 操作   | 最坏时间复杂度           | 摊还时间复杂度           | 主要原因         |
| ---- | ----------------- | ----------------- | ------------ |
| 查找   | \(O(\log_b n)\)     | \(O(\log_b n)\)     | 走树高层数        |
| 插入   | \(O(\log_b n)\)     | \(O(\log_b n)\)     | 分裂摊还常数       |
| 删除   | \(O(\log_b n)\)     | \(O(\log_b n)\)     | 合并摊还常数       |
| 范围查询 | \(O(\log_b n + k)\) | \(O(\log_b n + k)\) | 查找起点 + 顺链表扫描 |

节点结构：

| 节点类型 | 含义 | 关键字数量范围 | 子节点数量范围 |
|-----------|------|----------------|----------------|
| 根节点（仅一个叶子） | 整棵树只有一个节点 | 1 ≤ keys ≤ M−1 | 0 |
| 根节点（内部节点） | 有子节点的根 | 1 ≤ keys ≤ M−1 | 2 ≤ pointers ≤ M |
| 内部节点 | 中间层节点 | ⌈M/2⌉−1 ≤ keys ≤ M−1 | ⌈M/2⌉ ≤ pointers ≤ M |
| 叶子节点 | 存储实际数据 | **⌈M/2⌉ ≤ keys ≤ M** | 0（或一个指向下一个叶子的指针） |

![alt text](res/images/1653617766d6fb0fea697403811b5127.jpg)

查找的时间复杂度就是 $O(\log N)$，不管 M

### Leftist Heap

时间复杂度：

| 操作          | 通过 merge 实现        | 最坏复杂度 | 摊还复杂度    |
| ----------- | ------------------ | ----- | -------- |
| `merge`     | 基础操作               | \( O(\log n) \)  | \( O(\log n) \) |
| `insert`    | merge(H, newNode)  | \( O(\log n) \)  | \( O(\log n) \) |
| `deleteMin` | merge(left, right) | \( O(\log n) \)  | \( O(\log n) \) |
| `findMin`   | 取根                 | \( O(1) \)  | \( O(1) \)     |


左偏堆是**右路径短**，merge 只沿右路径走，所以最坏也是 $O(\log n)$。不要和斜堆的“最坏线性、摊销对数”混了。

### Skew Heap（斜堆）

时间复杂度：

| 操作          | 最坏复杂度 | 摊还复杂度    | 说明                    |
| ----------- | ----- | -------- | --------------------- |
| `merge`     | \( O(n) \)  | \( O(log n) \) | 自调整保持平衡               |
| `insert`    | \( O(n) \)  | \( O(log n) \) | 相当于 merge(H, newNode) |
| `deleteMin` | \( O(n) \)  | \( O(log n) \) | 合并左右子堆                |
| `findMin`   | \( O(1) \)  | \( O(1) \)     | 取根节点                  |


斜堆的插入：

- 比较右路径上节点大小
- 合并时候，写出按顺序该出现的那个节点，二话不说先把其 **左子树移到右边**

### Inverted File

| | Relevant | Irrelevant |
| :--- | :---: | :---: |
| **Retrieved** | R<sub>R</sub> | I<sub>R</sub> |
| **Not Retrieved**| R<sub>N</sub> | I<sub>N</sub> |

Precision P = R<sub>R</sub> / (R<sub>R</sub> + I<sub>R</sub>)

Recall R = R<sub>R</sub> / (R<sub>R</sub> + R<sub>N</sub>)

记忆：

- recall：召回率 / 查全率，在所有应该被找回的结果中，我成功找回来了多少？

- precision：精确率 / 准确率，在所有我找回来的结果中，有多少是真正对的？


### Binomial Heap

| 操作              | 描述     | 最坏复杂度        | 摊还复杂度        |
| --------------- | ------ | ------------ | ------------ |
| `findMin()`     | 找最小根   | \( O(\log n) \) | \( O(\log n) \) |
| `insert(x)`     | 插入元素   | \( O(\log n) \) | \( O(1) \)     |
| `merge(H1, H2)` | 合并两个堆  | \( O(\log n) \) | \( O(\log n) \) |
| `deleteMin()`   | 删除最小元素 | \( O(\log n) \) | \( O(\log n) \) |
| `decreaseKey()` | 降低键值   | \( O(\log n) \) | \( O(\log n) \) |
## Methods

### Master Theorem

递推式先写成 $T(N) = aT(N/b) + f(N)$，比较 $f(N)$ 与叶子数量 $N^{\log_b a}$。

| 情况 | 条件（某个 ε > 0） | 结果 |
| --- | --- | --- |
| Case 1 | $f(N) = O(N^{\log_b a - \varepsilon})$ | $\Theta(N^{\log_b a})$ |
| Case 2 | $f(N) = \Theta(N^{\log_b a})$ | $\Theta(N^{\log_b a}\log N)$ |
| Case 3 | $f(N) = \Omega(N^{\log_b a + \varepsilon})$，且 $af(N/b) \le cf(N)$，某个 c < 1 | $\Theta(f(N))$ |

第一、三种要差一个**多项式因子**，不是只要稍微大一点 / 小一点就行。第三种还要检查正则条件，主方法也不是所有递推都能套。

里面的 $N^{\log_ b a}$ 是叶子结点的数量，也是当 $af(N/b) = f(N)$ 时候的函数表达式（差一个常数）

### Amortized Analysis

摊销：看一串操作总共花了多少，再摊到每一次。不是假设某种输入随机出现，所以和平均情况分析不一样。

例子：动态数组满了就扩到两倍。某一次扩容要复制 n 个元素，很慢；但不是每次插入都扩容。

连续插入 n 次，复制量是 `1 + 2 + 4 + ...`，总共 $O(n)$；再加每次插入本身，总开销仍然 $O(n)$，摊到一次就是 $O(1)$。

- 聚合分析：直接加总时间。
- 记账法：便宜的操作多收一点，存下来付以后贵的操作。
- 势能法：$\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$，相加后中间的势能项会消掉。

选势能时记得检查非负、初始值。不能凭空给未来的开销借一笔永远不还的账。


## Algorithm

### Divide Conquer

分成子问题，各自递归解决，再合并。例子：归并排序先分左右两半，最后 merge。

### Backtracking

先测试约束强、候选少的部分，早点排除不可能的解；这个是回溯剪枝的思路，和分治合并要分开。
