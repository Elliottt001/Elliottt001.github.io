
## 抽象数据类型 ADT

数据类型 + 操作，不关心具体实现

### 线性结构

一个列表，可以完成许多操作

- 查找
- 插入
- 删除

实现方式：数组/链表

数组：开buffer（连续内存空间），用偏移量表示数；

- 缺点：需要估计 MaxSize；插入删除复杂（平均时间复杂度是 $O(N)$ 首为N，尾为1，平均还是N）

链表：结构体，每个node只知道下一个是谁next指针

- 优点节约 memory
- 查找：从头遍历，$O(N)$ （中间 half n, still about n）
- 插入：三步：allocate + 连尾 + 连头
    ```c
    temp->next = node->next
    node-> next = temp
    //两步不能反：否则自己指向自己 断链disaster！
    ```
- 删除：先从头遍历找到前一个指针（他的next = node），再改next，再free
    ```c

    ```

双向链表：空间换时间

每个节点两个指针，`llink` 和 `rlink` 分别指前面和后面

判断单链是否由loop：快指针 慢指针

ACM~

#### 多项式

算术运算

数组：下标即次数，缺点是中间空的

链表：

- 存储：系数、次数、next

#### multilist

数组：`array[n][m]`

链表：

水平竖直

没有pointer实现链表

### cuesor implement

针对没有pointer的语言

一次开一个buffer

## stack 栈

一种线性表

delete —— pop，insert —— push都是在顶上

reverse order 有用

操作：

- isempty
- creat
- makeempty
- push
- top
- pop
- disposestack

### 实现

链表：关键点是 **指针指向前一个**

定义一个栈顶指针

设计一个recycle bin 的stack，存储删除的东西，但不删除

不free！

数组

### 应用

#### balancing symble

#### 后缀表达式计算

- postfix后缀表达式：机器可读

- infix中缀表达式：人可读

操作数顺序不变，区别是操作符在两个数后面

eg：$62/ \Leftrightarrow 6/2$, 结果替换原来的式子

**算法**：读入，一次删pop两个

优点：不需要考虑优先级

写计算器：

1. infix -> postfix

    - reverse order 思想
    - 比较优先级，决定是继续pop or push
    - 例如对于 $a + b * c - d / e$：push进
    - 有括号：方法是规定括号在栈外部优先级最高，在栈内最低，仅当出现右括号才pop左括号；有右括号则pop everything
    

2. 计算

    - 

#### 函数调用

是 system stack

首先要有 return address（需要回来） —— stack frame —— local variable —— pop

recursion：编译器自动转换成带标号的

工程应用：不用递归

## queue 队列

特点：进出口不一样 first in first out

### 操作

- isempty
- create
- dispose
- makeempty
- enqueue
- dequeue
- front：数据类型

### 实现

能用数组则数组

#### 数组

取余操作！：逻辑上实现环形queue，但物理上还是线性的，最后一个不能占用：否则full和empty是同样状态（用front和rear的相对位置判断size

长度：头减尾/定义长度变量

## tree

作用主要的searching

递归定义的：基本都是recursive

与学校管理一样的（

organization tree / decision tree

组成：是一系列节点node

- root 根节点
- 其他 subtree（单独拿一个节点和子节点都是tree）

特点

- 是graph的一种：subtree是 must not connect each other
- N node 的 tree 有 N - 1 条边：edge 

定义

- degree of node 节点的度 degree(node)：有几个孩子（孩子的集合的模）
- parent / children：一条边产生的关系，是不对称关系
- siblings：互为姊妹，是对称的关系
- leaf / terminal node 叶节点：degree = 0
- path from $n_1$ to $n_k$ : 
- length of path : number of **edges** on the path
- depth of $n_i$ : length of the unique path from the root to $n_i$
- height of $n_i$ : longest path from $n_i$ to a leaf
- height/depth of tree = height(root) = depth()

特点：向上走唯一，向下走很多

### 实现

数组（复杂）：用括号

链表：

方法一：直接实现

方法二：FirstChild NextSibling —— 旋转45度——> binary tree

0/1/2 个孩子，左为FirstChild，右为NextSibling

### 示例

:star: 四种traversal必考

[CSDN文章](https://blog.csdn.net/qq_44096670/article/details/109638015)

只有 inorder 的只针对二叉树

根据两个traversal的顺序写另一个：

- 识别一般规律：postorder根节点最后，
- inorder
- 用recursion！

levelorder需要一个queue

非递归实现：用 自定义 stack 代替system stack

时间复杂度：所有的traversal都是线性的：因为每个node当且仅当访问一次！

### 线索二叉树 threaded binary tree

N node 的二叉树有几个 NULL：N + 1

- 每个节点贡献两个分支，共 2N 个，实实在在的边为 N - 1，故 N + 1

