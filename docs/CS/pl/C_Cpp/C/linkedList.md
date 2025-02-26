
## 问题一：(Node*)malloc(sizeof(Node))
```c
Node* createList() {
    Node* head = (Node*)malloc(sizeof(Node)); // 创建头节点
    head->next = NULL; // 头节点的指针域初始化为NULL
    return head;
    //是(Node*)malloc(sizeof(Node))而不是(Node*)malloc(sizeof(Node*))
}
```

`head` 是一个指向 `Node` 类型的指针，而你要分配的内存是用来存储一个 `Node` 结构体的数据。因此，应该为 **结构体本身** 分配内存，而不是为指针分配内存。

**`malloc(sizeof(Node))` 的含义**：

   - `malloc(sizeof(Node))` 会根据 `Node` 结构体的大小分配内存。例如，假设 `Node` 结构体包含一个 `next` 指针（通常是 `Node*` 类型），那么 `sizeof(Node)` 就是 `Node` 结构体的总大小，包含 `next` 指针所占的空间。
   - 当你为 `Node` 分配内存时，你实际上是为整个结构体分配空间，而不是为指针本身分配空间。指针只是用来指向那个结构体的。

