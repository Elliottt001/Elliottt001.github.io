# 循环和分支

循环：

- for 
- while 
- do while
### 语法

**`do while` 的语法**
```c
int main()
{
    do
    {
        /* code */
    } while (/* condition */);
}
```
很好用，意义是不管任何条件先做一次，适用于条件判断处有特殊情况时。例如输入的数字是0，条件判断是 `> 0` 

当 `while` 做出错时，试试 `do while`

**灵活：**

- for内部：`(起始条件; 条件判断; 结束条件)`

    - 内部三处均可按需省略，保留两个分号即可
    - 不一定只能有一个变量，几个条件不一定必须是只含 `i` 的逻辑表达式

- 何时开始何时结束

    ```c
    #include <stdio.h>
    #include<stdlib.h>
    #include<string.h>
    int main(void)
    {
        int i, n = 0;
        char *color[20], str[15];
        scanf("%s", str);
        while(str[0] != '#') {
            color[n] = (char *)malloc(sizeof(char)*(strlen(str)+1)); 
            strcpy(color[n], str);     
            n++;
            scanf("%s", str);
        }
        
        for(i = n-1; i >= 0; i--)
            printf("%s  ", color[i]);
        return 0;
    }
    ```

### 示例

写无限循环遇到某条件跳出：
```c
for(i = 0; ; i++){
    if(/*条件*/) break;
    else /*代码块例如cnt++*/;
}
```
```c
while(1){
    /*代码块例如cnt++*/;
    if(/*条件*/) break;
}
```

分支

`if`

`switch`

```c
switch (expression)
{
case /* constant-expression */:  //一定得是常量
    /* code */
    break;

default:
    break;
}
```

**示例：**

模拟一个**内存管理操作系统的命令行界面**，提供查看内存状态、分配内存、释放内存和退出操作。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BLOCKS 10  // 最大内存块数

typedef struct {
    int id;       // 内存块 ID
    size_t size;  // 内存块大小
    int in_use;   // 是否正在使用（1 表示使用中，0 表示未使用）
} MemoryBlock;

MemoryBlock memory[MAX_BLOCKS];  // 模拟内存块数组

void initialize_memory() {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        memory[i].id = i;
        memory[i].size = 0;
        memory[i].in_use = 0;
    }
}

void view_memory() {
    printf("\n=== 内存状态 ===\n");
    for (int i = 0; i < MAX_BLOCKS; i++) {
        printf("块 ID: %d, 大小: %zu 字节, 状态: %s\n",
               memory[i].id,
               memory[i].size,
               memory[i].in_use ? "已分配" : "未分配");
    }
}

void allocate_memory() {
    int id;
    size_t size;

    printf("请输入要分配的块 ID (0-%d): ", MAX_BLOCKS - 1);
    scanf("%d", &id);

    if (id < 0 || id >= MAX_BLOCKS) {
        printf("无效的块 ID！\n");
        return;
    }

    if (memory[id].in_use) {
        printf("块 ID %d 已被占用！\n", id);
        return;
    }

    printf("请输入要分配的大小 (字节): ");
    scanf("%zu", &size);

    memory[id].size = size;
    memory[id].in_use = 1;
    printf("内存块 ID %d 分配成功，大小为 %zu 字节！\n", id, size);
}

void free_memory() {
    int id;

    printf("请输入要释放的块 ID (0-%d): ", MAX_BLOCKS - 1);
    scanf("%d", &id);

    if (id < 0 || id >= MAX_BLOCKS) {
        printf("无效的块 ID！\n");
        return;
    }

    if (!memory[id].in_use) {
        printf("块 ID %d 未被分配，无需释放！\n", id);
        return;
    }

    memory[id].size = 0;
    memory[id].in_use = 0;
    printf("内存块 ID %d 已成功释放！\n", id);
}

int main() {
    int choice;

    initialize_memory();  // 初始化内存状态

    while (1) {
        // 打印菜单
        printf("\n=== 内存管理系统 ===\n");
        printf("1. 查看内存状态\n");
        printf("2. 分配内存\n");
        printf("3. 释放内存\n");
        printf("4. 退出\n");
        printf("请输入你的选择 (1-4): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                view_memory();
                break;
            case 2:
                allocate_memory();
                break;
            case 3:
                free_memory();
                break;
            case 4:
                printf("退出内存管理系统。\n");
                return 0;
            default:
                printf("无效的选择，请输入 1 到 4 之间的数字。\n");
        }
    }

    return 0;
}
```

---

**运行示例**

初始化时查看内存状态：

```
=== 内存状态 ===
块 ID: 0, 大小: 0 字节, 状态: 未分配
块 ID: 1, 大小: 0 字节, 状态: 未分配
块 ID: 2, 大小: 0 字节, 状态: 未分配
...
```

分配内存块：

```
请输入要分配的块 ID (0-9): 2
请输入要分配的大小 (字节): 1024
内存块 ID 2 分配成功，大小为 1024 字节！
```

查看内存状态：

```
=== 内存状态 ===
块 ID: 0, 大小: 0 字节, 状态: 未分配
块 ID: 1, 大小: 0 字节, 状态: 未分配
块 ID: 2, 大小: 1024 字节, 状态: 已分配
...
```

释放内存块：

```
请输入要释放的块 ID (0-9): 2
内存块 ID 2 已成功释放！
```

查看内存状态：

```
=== 内存状态 ===
块 ID: 0, 大小: 0 字节, 状态: 未分配
块 ID: 1, 大小: 0 字节, 状态: 未分配
块 ID: 2, 大小: 0 字节, 状态: 未分配
...
```

退出程序：

```
退出内存管理系统。
```

---

**代码解析**

1. **`MemoryBlock` 结构体**：
   - 模拟内存块的信息，包括块 ID、大小和状态。

2. **`initialize_memory` 函数**：
   - 初始化所有内存块为未分配状态。

3. **`view_memory` 函数**：
   - 显示当前内存的分配状态。

4. **`allocate_memory` 和 `free_memory` 函数**：
   - 分配或释放内存块，并更新状态。

5. **`switch` 语句**：
   - 实现不同操作之间的选择。

---



