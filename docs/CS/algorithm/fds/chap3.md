
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




