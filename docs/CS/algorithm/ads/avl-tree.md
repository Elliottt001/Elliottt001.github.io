## 定义概念

平均搜索时间 average search time：节点深度平均值

### AVL tree 定义

0. 空树是 height balanced 的
1. 左右子树都 height balanced：**递归下去所有都是**
2. $|h_L - h_r| \le 1$，即对所有节点 $BF(node) = -1 / 0 / 1$，

!!! info ""

    定义  $BF(node) = h_L - h_R$

## 旋转（核心）

**一句话，每次插入 / 删除，带来 BF 的变化，就要看需不需要旋转，如果需要的话，看从 trouble maker 到 trouble finder 这条路上的情况，决定怎样旋转**

### 规律

**命名来由**（LL / LR / RR / RL）：

- trouble maker：插入/删除点
- trouble finder：失衡节点

从 trouble finder 看 trouble maker 在哪边的哪边，只数三个节点（包含头尾，也就是中间经过一个节点）：L代表左子树，R代表右子树

- LL：左子树的左子树插入
- LR：左子树的右子树插入
- RR：右子树的右子树插入
- RL：右子树的左子树插入


### RR rotate
![alt text](res/images/image.png)

1. trouble maker: $B_R$，右子树的右子树插入
2. trouble finder（此处是A）：从插入/删除点往上回溯
3. 局部调整，整体起效：一般 AVL 调整只需要处理 离插入点最近的、最底层的失衡节点（即第一个 finder），即此处 A 没必要是根节点
4. 调整过程保持 二叉搜索树的中序遍历结果不变，即这里 $B_L$ 变成 A 的右子树

### LL rotate

![alt text](res/images/image-1.png)

### LR rotate

![alt text](res/images/image-3.png)


旋转方法：反着转，先右后左

- 左：左子树，即 trouble finder 的左子树
- 右：右子树，即 trouble finder 的左子树的右子树

右：把从 trouble maker 和从他开始到 trouble finder 的路径上前三个节点向左旋转（逆时针）

左：旋转原来的 trouble finder 节点，向右旋转（顺时针）

### RL rotate

![alt text](res/images/image-2.png)

基本同上，变一下顺序

## 数据存储

## 复杂度
![alt text](res/images/image-4.png)

$n_h$ 为高度为 h 的 AVL 树的最小节点数，由于是最小，则 root 的左右子树高度差1（相等的话左 / 右减去一个还是 AVL 树）

$$n_h = 1 + n_{h-1} + n_{h-2}$$

每一步操作都是 $O(\log n)$

- 插入：$O(\log n)$
- 删除：$O(\log n)$
- 查找：$O(\log n)$


## Spary Tree

### 基础操作

有些操作比较快（要求松），有的操作比较慢，做到连续 M 次操作最多 $O(M \log n)$

当一个节点被访问（时间超过某个阈值），就通过 AVL 的旋转使得其到根节点（ push to the root）

![alt text](res/images/image-5.png)

![alt text](res/images/image-6.png)

看一个节点 X、其父亲 P，和其祖父 G：

zig-zig

- X 是 P 的左子树，P 是 G 的左子树：两次单旋，先 P & G，再 X & P
- X 是 P 的右子树，P 是 G 的右子树：两次单旋

zig-zag

- X 是 P 的右子树，P 是 G 的左子树：一次双旋，左旋 P，再右旋 G
- X 是 P 的左子树，P 是 G 的右子树：一次双旋，右旋 P，再左旋 G

![alt text](res/images/image-7.png)

### 删除

![alt text](res/images/image-8.png)

### Spray Tree & AVL Tree 对比

|               | AVL Tree               | Spray Tree                      |
| ------------- | ---------------------- | ------------------------------- |
| 优点        |                  | 树高低                  |
| 缺点        | 每次都旋转           | 多一个push to root                          |

|               | AVL Tree               | Spray Tree                      |
| ------------- | ---------------------- | ------------------------------- |
| 平衡性        | 严格平衡               | 松散平衡                        |
| 旋转次数      | 每次插入/删除可能旋转   | 不是每次都要| 每次访问可能旋转多次            |
| 单次操作时间  | $O(\log n)$           | 不能保证                     |
| 多次操作时间 | $O(M \log n)$          | $O(M \log n)$                   |


## Amortized Analysis

概念：摊销分析是一种通过考虑一系列操作的总成本来平摊单个操作的成本，从而得出更精确的时间复杂度的方法。

![alt text](res/images/image-9.png)


思想：$n$ 个操作花时间为 $T(n)$，In the worse case, amortised cose is $T(n) / n$

Example: on an initially 

!!! success ""

    We can pop each object from the stack at most once for each time we have pushed it onto the stack


### Accouting Method

![alt text](res/images/image-10.png)

计算方法：将所有时间加起来，除以 n

以 multipop 举例，只有 push 才能 pop，push 时存一个 1 的 credit

### Potential method

![alt text](res/images/image-12.png)

最关键的是 $D_i$ $D_i$ 的定义

用 Potential method 可以计算 accounting method 的 credit，继而算 amortized time

![alt text](res/images/image-11.png)

Why rank of the subtree, not height of the tree.

局部性原理：rank 只与局部有关（X / P / G）

