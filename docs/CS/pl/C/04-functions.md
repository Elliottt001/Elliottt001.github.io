# 函数

### 定义、声明与调用
#### 声明
编译器一行一行编译，故调用之前应该让编译器知道函数的返回类型、参数、名称

**建议**：用声明：先读main函数干什么

**位置**
	
- C89：写在main里面也可
- C99：写在main前面

**规则：** 定义声明一致

实际上，声明中可以只写变量类型，变量名称也可以和函数定义头部不一样。因为编译器检查只检查定义和声明变量类型是否一样

#### 参数和值

**核心：**

要在函数内部对主函数的变量进行操作，则必须得把主函数中的那个变量or其地址传入函数。

**形参实参**

- 参数 & 值：实参 —— 参数；形参 —— 值（参数的值）：就是传值

**数组作为函数的参数**
```
Ctrl F 指针与函数
```

#### 变量空间：
每个函数都有他自己的变量空间；
离开一个函数f到另一个函数g里面，则会跳出f的变量空间，来到g的变量空间；
在一个函数g里面对变量操作，不会影响f里面的变量，因为不在一个变量空间；

#### 局部变量

**前置**

- 生存期：变量多会出现，多会消亡
- 作用域：在代码的什么范围内可以访问这个变量（这个变量起作用）

**定义**

![alt text](res/images/image.png)

局部变量(\==本地变量、自动变量)

概念：

每次函数运行，都产生一个独立的变量空间，这个空间中的变量是函数这次运行独有的

分类：定义在函数内部的 & 参数

规则：

定义在块内，即一个大括号{ }，进入块，变量存在；离开块，变量消失
- 函数的块内
- 语句的块内
- 甚至以单拉一个大括号定义变量

内部的变量外部不可以访问，外部的变量内部可以访问

同名变量：
- 内外同名：内部掩盖外部的
- 内部同名：编译错误redefination

本地变量不会默认初始化，但是参数进入函数时已经被初始化（参数的传递）

#### 调用函数

传递的值（实参）：常量、变量、*表达式（的值）*

**类型不匹配：** C会发生自动类型转换：即将传入的参数类型转换为定义中说的那个类型。Java、C++会严格检查类型的匹配。

**传值：** 永远是传值给函数，即参数传递的单向性：实参的值传给形参，形参的值改变了，也不会影响实参。还是变量空间的问题，swap的例子。

#### 返回值

**return作用：**

1. 结束执行函数
2. 返回一个值，将这个值给到调用它的地方：*调用它的地方那里写的函数调用就是代表该函数的返回值*。

**规则：**

1. `return;`, 
2. `return 表达式;` 将表达式的值传出去
3. 函数里面可以多个return，也可以不在函数最后。
4. *单一出口理念*：最好函数只有一个出口即只有一个return。


#### 杂项
- 没有参数
	
    `f(void)` : 不传参数，声明时写上void，别不写

- 逗号运算符
	
    `f(a, b)` : 逗号是标点符号不是运算符，这是传了俩参数
	
    `f((a, b))` : `(a, b)`是一个表达式，值是b，则这句代表传的是这个表达式的值：b
- 函数中不能定义函数，可以声明
- 函数声明可以放在自己的定义里面
- main函数
	
    return 0；返回0：正确；返回非0：异常
	
    bash : `echo $?`: 可查看main运行结束的返回值（return -1 则 stdout：255）

### 标准库

#### stdio.h

**1. `printf`**  
**功能**：格式化输出到标准输出（屏幕）。  
**函数原型**：`int printf(const char *format, ...);`  
**示例**：  
```c
printf("Hello, %s! You are %d years old.\n", "Alice", 25);
```

---

**2. `scanf`**  
**功能**：从标准输入读取格式化数据。  
**函数原型**：`int scanf(const char *format, ...);`  
**示例**：  
```c
int age;
scanf("%d", &age);
```

!!! info "scanf的工作原理"

    `scanf` 的工作原理与输入缓冲区的影响

    1. **标准输入缓冲区的作用**
    - 当用户输入内容并按下 **Enter** 键时，输入的所有字符（包括换行符 `\n`）会被存储在标准输入缓冲区中。
    - `scanf` 从缓冲区中读取数据，根据指定的格式（如 `%s`、`%c` 等）提取需要的部分，剩余的内容仍保留在缓冲区中。

    ---

    2. **`scanf` 格式说明符的行为**

    - **`%s`（读取字符串）**
    - `scanf("%s", buffer)` 会跳过缓冲区中所有的空白字符（包括空格、换行符、制表符）**作为起始位置**。
    - 然后从第一个非空白字符开始读取，直到遇到下一个空白字符（或缓冲区结尾），并将读取的字符存储到 `buffer` 中。
    - **剩下的内容**（包括分隔字符串的空白字符，如换行符）留在缓冲区中。
    
    - **`%c`（读取单个字符）**
    - `scanf("%c", &ch)` 不会跳过空白字符，而是直接读取缓冲区的下一个字符，包括换行符或空格。
    - 如果缓冲区中还有未处理的换行符，`%c` 就会直接读取它。

    ---

    ??? info "程序的输入流程分析"

        假设我们运行以下代码并输入数据：
        ```c
        char matrix[5][100];
        char ch;

        for (int i = 0; i < 5; i++) {
            scanf("%s", matrix[i]);
        }
        scanf("%c", &ch);
        ```

        **输入内容：**
        ```
        Apple
        Banana
        Avocado
        Blueberry
        Cherry
        A
        ```

        **详细流程：**

        1. **第一轮循环读取字符串**
        - 用户输入 "Apple" + 按下 **Enter**。
        - 输入缓冲区内容为：`Apple\n`
        - `scanf("%s", matrix[0]);`：
            - 跳过缓冲区中的空白字符（无）。
            - 读取 `Apple` 到 `matrix[0]`。
            - 停止在第一个空白字符（`\n`），缓冲区变为：`\n`。

        2. **第二轮循环读取字符串**
        - 用户输入 "Banana" + 按下 **Enter**。
        - 输入缓冲区内容为：`\nBanana\n`（上轮剩下的 `\n` + 新输入的 `Banana\n`）。
        - `scanf("%s", matrix[1]);`：
            - 跳过缓冲区中的空白字符（`\n`）。
            - 读取 `Banana` 到 `matrix[1]`。
            - 停止在第一个空白字符（`\n`），缓冲区变为：`\n`。

        3. **重复过程**
        - 对每一轮字符串输入，`scanf("%s", ...)` 都会读取用户输入的内容，同时将末尾的换行符 `\n` 留在缓冲区。

        4. **读取字符 `ch`**
        - 第五次循环结束后，缓冲区中剩下一个换行符 `\n`（用户按下 Enter）。
        - `scanf("%c", &ch);` 不跳过空白字符，直接读取到这个换行符 `\n`。
        - `ch` 存储的不是用户期望的字符，而是换行符。

    ---

    5. **解决方法**

    1. **清理缓冲区**
    在读取字符前手动清除输入缓冲区：
    ```c
    while (getchar() != '\n'); // 逐个读取直到清除所有残留字符：**用于清空缓存区**
    ```

    2. **修改读取方式**
    改用 `getchar` 或更高级的输入方法：
    ```c
    ch = getchar(); // 更直接地读取单个字符
    ```

    3. **结合 `fgets` 使用**
    改用 `fgets` 一次性读取一整行数据，减少缓冲区问题：
    ```c
    fgets(matrix[i], sizeof(matrix[i]), stdin);
    ```

    ---


**3. `fprintf`**  
**功能**：格式化输出到指定文件流。  
**函数原型**：`int fprintf(FILE *stream, const char *format, ...);`  
**示例**：  
```c
FILE *fp = fopen("output.txt", "w");
fprintf(fp, "Score: %d\n", 100);
fclose(fp);
```

---

**4. `fscanf`**  
**功能**：从指定文件流读取格式化数据。  
**函数原型**：`int fscanf(FILE *stream, const char *format, ...);`  
**示例**：  
```c
FILE *fp = fopen("data.txt", "r");
int score;
fscanf(fp, "%d", &score);
fclose(fp);
```

---

**5. `fopen`**  
**功能**：打开文件。  
**函数原型**：`FILE *fopen(const char *filename, const char *mode);`  
**示例**：  
```c
FILE *fp = fopen("file.txt", "r");
```

---

**6. `fclose`**  
**功能**：关闭文件流。  
**函数原型**：`int fclose(FILE *stream);`  
**示例**：  
```c
fclose(fp);
```

---

**7. `fgetc`**  
**功能**：从文件流中读取单个字符。  
**函数原型**：`int fgetc(FILE *stream);`  
**示例**：  
```c
char ch = fgetc(fp);
```

---

**8. `fputc`**  
**功能**：将单个字符写入文件流。  
**函数原型**：`int fputc(int c, FILE *stream);`  
**示例**：  
```c
fputc('A', fp);
```

---

**9. `fgets`**  
**功能**：从文件流读取一行。  
**函数原型**：`char *fgets(char *str, int n, FILE *stream);`  
**示例**：  
```c
char buffer[100];
fgets(buffer, 100, fp);
```

---

**10. `fputs`**  
**功能**：将字符串写入文件流。  
**函数原型**：`int fputs(const char *str, FILE *stream);`  
**示例**：  
```c
fputs("Hello, World!\n", fp);
```

---

**11. `getchar`**  
**功能**：从标准输入读取单个字符。  
**函数原型**：`int getchar(void);`  
**示例**：  
```c
char ch = getchar();
```

---

**12. `putchar`**  
**功能**：输出单个字符到标准输出。  
**函数原型**：`int putchar(int c);`  
**示例**：  
```c
putchar('A');
```

---

**13. `gets`** *(已不推荐使用，存在安全隐患)*  
**功能**：从标准输入读取字符串。  
**函数原型**：`char *gets(char *str);`  
**示例**：  
```c
char buffer[100];
gets(buffer);
```

---

**14. `puts`**  
**功能**：输出字符串到标准输出。  
**函数原型**：`int puts(const char *str);`  
**示例**：  
```c
puts("Hello, World!");
```

---

**15. `feof`**  
**功能**：检查文件流是否到达末尾。  
**函数原型**：`int feof(FILE *stream);`  
**示例**：  
```c
if (feof(fp)) {
    printf("End of file reached.\n");
}
```

---

**16. `ferror`**  
**功能**：检查文件流是否有错误。  
**函数原型**：`int ferror(FILE *stream);`  
**示例**：  
```c
if (ferror(fp)) {
    printf("File error occurred.\n");
}
```

---

**17. `rewind`**  
**功能**：将文件流位置指针重置到文件开头。  
**函数原型**：`void rewind(FILE *stream);`  
**示例**：  
```c
rewind(fp);
```

---

**18. `ftell`**  
**功能**：获取文件流当前位置。  
**函数原型**：`long ftell(FILE *stream);`  
**示例**：  
```c
long pos = ftell(fp);
```

---

**19. `fseek`**  
**功能**：设置文件流位置指针。  
**函数原型**：`int fseek(FILE *stream, long offset, int whence);`  
**示例**：  
```c
fseek(fp, 0, SEEK_END);
```

---

**20. `clearerr`**  
**功能**：清除文件流的错误标志和 EOF 标志。  
**函数原型**：`void clearerr(FILE *stream);`  
**示例**：  
```c
clearerr(fp);
```


#### string.h

**1. `strlen`**  
**功能**：返回字符串的长度（不包括终止符 `\0`）。  
**函数原型**：`size_t strlen(const char *str);`  
**示例**：  
```c
printf("%zu\n", strlen("Hello")); // 输出 5
```

---

**2. `strcpy`**  
**功能**：将字符串复制到另一个字符串。  
**函数原型**：`char *strcpy(char *dest, const char *src);`  
**底层**：第一个参数代表目标的起始地址，第二个参数代表源头的起始地址。   
**示例**：  
```c
char dest[20];
strcpy(dest, "Hello");
printf("%s\n", dest); // 输出 "Hello"
```

---

**3. `strncpy`**  
**功能**：复制指定长度的字符串到另一个字符串。  
**函数原型**：`char *strncpy(char *dest, const char *src, size_t n);`  
**示例**：  
```c
char dest[10];
strncpy(dest, "HelloWorld", 5);
dest[5] = '\0';
printf("%s\n", dest); // 输出 "Hello"
```

---

**4. `strcat`**  
**功能**：将字符串追加到另一个字符串的末尾。  
**函数原型**：`char *strcat(char *dest, const char *src);`  
**示例**：  
```c
char str[20] = "Hello";
strcat(str, " World");
printf("%s\n", str); // 输出 "Hello World"
```

---

**5. `strncat`**  
**功能**：将指定长度的字符串追加到另一个字符串的末尾。  
**函数原型**：`char *strncat(char *dest, const char *src, size_t n);`  
**示例**：  
```c
char str[20] = "Hello";
strncat(str, "World", 3);
printf("%s\n", str); // 输出 "HelloWor"
```

---

**6. `strcmp`**  
**功能**：比较两个字符串（区分大小写）。  
**函数原型**：`int strcmp(const char *str1, const char *str2);`  
**示例**：  
```c
if (strcmp("abc", "abc") == 0) {
    printf("Equal\n");
}
```

---

**7. `strncmp`**  
**功能**：比较指定长度的两个字符串。  
**函数原型**：`int strncmp(const char *str1, const char *str2, size_t n);`  
**示例**：  
```c
if (strncmp("abcdef", "abcxyz", 3) == 0) {
    printf("Equal\n");
}
```

---

**8. `strchr`**  
**功能**：查找字符串中首次出现的指定字符。  
**函数原型**：`char *strchr(const char *str, int c);`  
**示例**：  
```c
char *pos = strchr("Hello", 'e');
if (pos) {
    printf("Found at index %ld\n", pos - "Hello");
}
/*
查找字符第一次出现的位置。如果找到了，函数会返回指向该字符的指针；如果找不到，则返回 NULL。
"Hello" 是字符串的起始地址。
pos 是目标字符 'e' 的地址。
将两个指针相减，结果就是目标字符相对于字符串起始位置的索引。
*/

```

---

**9. `strrchr`**  
**功能**：查找字符串中最后一次出现的指定字符。  
**函数原型**：`char *strrchr(const char *str, int c);`  
**示例**：  
```c
char *pos = strrchr("Hello", 'l');
if (pos) {
    printf("Found at index %ld\n", pos - "Hello");
}
```

---

**10. `strstr`**  
**功能**：查找字符串中首次出现的子串。  
**函数原型**：`char *strstr(const char *haystack, const char *needle);`  
**示例**：  
```c
char *pos = strstr("Hello World", "World");
if (pos) {
    printf("Substring found: %s\n", pos);
}
```

---

**11. `strtok`**  
**功能**：分割字符串（以指定分隔符为界）。  
**函数原型**：`char *strtok(char *str, const char *delim);`  
**示例**：  
```c
char str[] = "Hello,World";
char *token = strtok(str, ",");
while (token) {
    printf("%s\n", token);
    token = strtok(NULL, ",");
}
/*
char *strtok(char *__restrict__ __s, const char *__restrict__ __delim)

Divide S into tokens separated by characters in DELIM.
*/

/*

 1. **`char str[] = "Hello,World";`**
   - 定义了一个字符串数组 `str`，其中包含内容 `"Hello,World"`。
   - 字符串 `str` 可被修改（不同于字符串常量）。

 2. **`char *token = strtok(str, ",");`**
   - `strtok` 函数用于将字符串 `str` 按分隔符 `","`（逗号）进行分割。
   - 第一次调用时，`strtok` 将会：
     1. 查找第一个分隔符 `','`。
     2. 将分隔符替换为 `'\0'`（字符串结束符）。
     3. 返回指向第一个子字符串（即 `Hello`）的指针。

 3. **`while (token) {`**
   - 只要 `token` 不为 `NULL`，就继续循环。
   - `strtok` 会返回每个子字符串的指针，直到字符串末尾时返回 `NULL`。

 4. **`printf("%s\n", token);`**
   - 打印当前的子字符串（token）。

 5. **`token = strtok(NULL, ",");`**
   - 继续查找下一个子字符串：
     - 第二次及之后的调用中，传入的第一个参数必须为 `NULL`，表示继续处理上一次的字符串。
     - 查找到下一个分隔符，返回对应的子字符串指针。
*/
```

---

**12. `memset`**  
**功能**：将内存的某一部分设置为指定值。  
**函数原型**：`void *memset(void *s, int c, size_t n);`  
**示例**：  
```c
char buffer[10];
memset(buffer, 'A', 10);
buffer[9] = '\0';
printf("%s\n", buffer); // 输出 "AAAAAAAAA"
```

---

**13. `memcpy`**  
**功能**：复制内存区域。  
**函数原型**：`void *memcpy(void *dest, const void *src, size_t n);`  
**示例**：  
```c
char src[] = "Hello";
char dest[10];
memcpy(dest, src, 6);
printf("%s\n", dest); // 输出 "Hello"
```

---

**14. `memmove`**  
**功能**：在内存区域重叠时安全地复制内存。  
**函数原型**：`void *memmove(void *dest, const void *src, size_t n);`  
**示例**：  
```c
char str[] = "HelloWorld";
memmove(str + 5, str, 5);
printf("%s\n", str); // 输出 "HelloHello"
```

---

**15. `memcmp`**  
**功能**：比较两个内存区域。  
**函数原型**：`int memcmp(const void *s1, const void *s2, size_t n);`  
**示例**：  
```c
if (memcmp("abc", "abc", 3) == 0) {
    printf("Memory is equal\n");
}
```

---

**16. `strdup`** *(POSIX标准，部分实现中提供)*  
**功能**：复制字符串并返回新分配的副本。  
**函数原型**：`char *strdup(const char *str);`  
**示例**：  
```c
char *copy = strdup("Hello");
printf("%s\n", copy);
free(copy);
```

---

**17. `strcspn`**  
**功能**：返回在字符串中找到的第一个不属于指定字符集的字符位置。  
**函数原型**：`size_t strcspn(const char *str1, const char *str2);`  
**示例**：  
```c
size_t pos = strcspn("Hello, World", " ,");
printf("%zu\n", pos); // 输出 5
```

---

**18. `strspn`**  
**功能**：返回字符串中连续包含指定字符集的字符数。  
**函数原型**：`size_t strspn(const char *str1, const char *str2);`  
**示例**：  
```c
size_t len = strspn("abcdef", "abc");
printf("%zu\n", len); // 输出 3
```

---

**19. `strpbrk`**  
**功能**：查找字符串中第一个包含在指定字符集中的字符。  
**函数原型**：`char *strpbrk(const char *str1, const char *str2);`  
**示例**：  
```c
char *pos = strpbrk("Hello, World", ",!");
if (pos) {
    printf("Found: %c\n", *pos); // 输出 ','
}
```

---

**20. `strrev`** *(非标准函数，部分实现中提供)*  
**功能**：反转字符串。  
**函数原型**：`char *strrev(char *str);`  
**示例**：  
```c
char str[] = "Hello";
strrev(str);
printf("%s\n", str); // 输出 "olleH"
```


#### ctype.h

**1. `isalnum`**  
**功能**：检查字符是否为字母或数字。  
**函数原型**：`int isalnum(int c);`  
**示例**：  
```c
if (isalnum('A')) {
    printf("Alphanumeric\n");
}
```

---

**2. `isalpha`**  
**功能**：检查字符是否为字母。  
**函数原型**：`int isalpha(int c);`  
**示例**：  
```c
if (isalpha('b')) {
    printf("Alphabet\n");
}
```

---

**3. `isdigit`**  
**功能**：检查字符是否为数字（0-9）。  
**函数原型**：`int isdigit(int c);`  
**示例**：  
```c
if (isdigit('5')) {
    printf("Digit\n");
}
```

---

**4. `islower`**  
**功能**：检查字符是否为小写字母。  
**函数原型**：`int islower(int c);`  
**示例**：  
```c
if (islower('a')) {
    printf("Lowercase\n");
}
```

---

**5. `isupper`**  
**功能**：检查字符是否为大写字母。  
**函数原型**：`int isupper(int c);`  
**示例**：  
```c
if (isupper('Z')) {
    printf("Uppercase\n");
}
```

---

**6. `isspace`**  
**功能**：检查字符是否为空白字符（如空格、换行、制表符）。  
**函数原型**：`int isspace(int c);`  
**示例**：  
```c
if (isspace(' ')) {
    printf("Whitespace\n");
}
```

---

**7. `iscntrl`**  
**功能**：检查字符是否为控制字符（如回车、删除等）。  
**函数原型**：`int iscntrl(int c);`  
**示例**：  
```c
if (iscntrl('\n')) {
    printf("Control character\n");
}
```

---

**8. `isprint`**  
**功能**：检查字符是否为可打印字符（包括空格）。  
**函数原型**：`int isprint(int c);`  
**示例**：  
```c
if (isprint('A')) {
    printf("Printable\n");
}
```

---

**9. `isgraph`**  
**功能**：检查字符是否为可打印字符（不包括空格）。  
**函数原型**：`int isgraph(int c);`  
**示例**：  
```c
if (isgraph('!')) {
    printf("Graphical character\n");
}
```

---

**10. `ispunct`**  
**功能**：检查字符是否为标点符号。  
**函数原型**：`int ispunct(int c);`  
**示例**：  
```c
if (ispunct('?')) {
    printf("Punctuation\n");
}
```

---

**11. `tolower`**  
**功能**：将字符转换为小写（若可能）。  
**函数原型**：`int tolower(int c);`  
**示例**：  
```c
char ch = tolower('A');
printf("%c\n", ch); // 输出 'a'
```

---

**12. `toupper`**  
**功能**：将字符转换为大写（若可能）。  
**函数原型**：`int toupper(int c);`  
**示例**：  
```c
char ch = toupper('a');
printf("%c\n", ch); // 输出 'A'
```

---

**13. `isxdigit`**  
**功能**：检查字符是否为十六进制数字（0-9, A-F, a-f）。  
**函数原型**：`int isxdigit(int c);`  
**示例**：  
```c
if (isxdigit('F')) {
    printf("Hexadecimal digit\n");
}
```

---

**14. `isblank`** *(C99标准新增)*  
**功能**：检查字符是否为空格或制表符。  
**函数原型**：`int isblank(int c);`  
**示例**：  
```c
if (isblank('\t')) {
    printf("Blank character\n");
}
```

---

**15. `isascii`** *(非标准函数，部分实现中提供)*  
**功能**：检查字符是否为ASCII字符（0-127）。  
**函数原型**：`int isascii(int c);`  
**示例**：  
```c
if (isascii(65)) {
    printf("ASCII character\n");
}
```

---

**16. `toascii`** *(非标准函数，部分实现中提供)*  
**功能**：将字符转换为ASCII值。  
**函数原型**：`int toascii(int c);`  
**示例**：  
```c
int ascii = toascii('A');
printf("%d\n", ascii); // 输出 65
```


#### stdlib.h

**1. `malloc`**  
**功能**：分配动态内存。  
**函数原型**：`void *malloc(size_t size);`  
**示例**：  
```c
int *ptr = (int *)malloc(5 * sizeof(int));
if (ptr) {
    printf("Memory allocated\n");
    free(ptr);
}
```

---

**2. `calloc`**  
**功能**：分配并初始化动态内存。  
**函数原型**：`void *calloc(size_t num, size_t size);`  
**示例**：  
```c
int *ptr = (int *)calloc(5, sizeof(int));
if (ptr) {
    printf("Memory allocated and initialized to zero\n");
    free(ptr);
}
```

---

**3. `realloc`**  
**功能**：调整动态内存大小。  
**函数原型**：`void *realloc(void *ptr, size_t size);`  
**示例**：  
```c
int *ptr = (int *)malloc(5 * sizeof(int));
ptr = (int *)realloc(ptr, 10 * sizeof(int));
if (ptr) {
    printf("Memory resized\n");
    free(ptr);
}
```

---

**4. `free`**  
**功能**：释放动态内存。  
**函数原型**：`void free(void *ptr);`  
**示例**：  
```c
int *ptr = (int *)malloc(5 * sizeof(int));
free(ptr);
```

---

**5. `abs`**  
**功能**：计算整数的绝对值。  
**函数原型**：`int abs(int n);`  
**示例**：  
```c
printf("%d\n", abs(-5)); // 输出 5
```

---

**6. `labs`**  
**功能**：计算长整数的绝对值。  
**函数原型**：`long int labs(long int n);`  
**示例**：  
```c
printf("%ld\n", labs(-123456789L)); // 输出 123456789
```

---

**7. `llabs`** *(C99标准新增)*  
**功能**：计算长长整数的绝对值。  
**函数原型**：`long long int llabs(long long int n);`  
**示例**：  
```c
printf("%lld\n", llabs(-123456789012345LL)); // 输出 123456789012345
```

---

**8. `atoi`**  
**功能**：将字符串转换为整数。  
**函数原型**：`int atoi(const char *str);`  
**示例**：  
```c
printf("%d\n", atoi("123")); // 输出 123
```

---

**9. `atof`**  
**功能**：将字符串转换为浮点数。  
**函数原型**：`double atof(const char *str);`  
**示例**：  
```c
printf("%f\n", atof("123.45")); // 输出 123.450000
```

---

**10. `atol`**  
**功能**：将字符串转换为长整数。  
**函数原型**：`long int atol(const char *str);`  
**示例**：  
```c
printf("%ld\n", atol("123456789")); // 输出 123456789
```

---

**11. `atoll`** *(C99标准新增)*  
**功能**：将字符串转换为长长整数。  
**函数原型**：`long long int atoll(const char *str);`  
**示例**：  
```c
printf("%lld\n", atoll("1234567890123")); // 输出 1234567890123
```

---

**12. `strtol`**  
**功能**：将字符串转换为长整数，支持指定进制。  
**函数原型**：`long int strtol(const char *str, char **endptr, int base);`  
**示例**：  
```c
char *end;
long int value = strtol("123abc", &end, 10);
printf("%ld\n", value); // 输出 123
```

---

**13. `strtod`**  
**功能**：将字符串转换为双精度浮点数。  
**函数原型**：`double strtod(const char *str, char **endptr);`  
**示例**：  
```c
char *end;
double value = strtod("123.45abc", &end);
printf("%f\n", value); // 输出 123.450000
```

---

**14. `rand`**  
**功能**：生成伪随机数。  
**函数原型**：`int rand(void);`  
**示例**：  
```c
printf("%d\n", rand() % 100); // 输出 0-99 的随机数
```

---

**15. `srand`**  
**功能**：设置随机数种子。  
**函数原型**：`void srand(unsigned int seed);`  
**示例**：  
```c
srand(time(NULL));
printf("%d\n", rand() % 100);
```

---

**16. `system`**  
**功能**：执行系统命令。  
**函数原型**：`int system(const char *command);`  
**示例**：  
```c
system("ls"); // 在 Unix 系统上列出文件
```

---

**17. `bsearch`**  
**功能**：在排序数组中执行二分查找。  
**函数原型**：  
```c
void *bsearch(const void *key, const void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));
```  
**示例**：  
```c
int arr[] = {1, 2, 3, 4, 5};
int key = 3;
int *res = (int *)bsearch(&key, arr, 5, sizeof(int), compare);
if (res) printf("Found: %d\n", *res);
```

---

**18. `qsort`**  
**功能**：对数组进行快速排序。  
**函数原型**：  
```c
void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));
```  
**compar函数的实现：**  
```c
int cmp(const void *a, const void* b)  // 这里在qsort函数原型中就是const void *的指针，所以不能变
{
    const char *ca = (const char*)a;  // 根据要排序的数组的类型 选择强制类型转换的目标类型
    const char *cb = (const char*)b;  // 强制类型转换
    return *ca - *cb;
}
```  
**示例**：  
```c
int arr[] = {5, 2, 3, 1, 4};
qsort(arr, 5, sizeof(int), compare);
for (int i = 0; i < 5; i++) printf("%d ", arr[i]);
```

---

**19. `exit`**  
**功能**：终止程序执行。  
**函数原型**：`void exit(int status);`  
**示例**：  
```c
printf("Exiting...\n");
exit(0);
```

---

**20. `div`**  
**功能**：执行整数除法并返回商和余数。  
**函数原型**：`div_t div(int numerator, int denominator);`  
**示例**：  
```c
div_t result = div(10, 3);
printf("Quotient: %d, Remainder: %d\n", result.quot, result.rem);
```

---

**21. `labs`**  
**功能**：计算长整数的绝对值。  
**函数原型**：`long int labs(long int n);`  
**示例**：  
```c
printf("%ld\n", labs(-123456)); // 输出 123456
```

---

**22. `getenv`**  
**功能**：获取环境变量的值。  
**函数原型**：`char *getenv(const char *name);`  
**示例**：  
```c
printf("PATH: %s\n", getenv("PATH"));
```

---

**23. `_Exit`** *(C99标准新增)*  
**功能**：立即退出程序，不执行清理操作。  
**函数原型**：`void _Exit(int status);`  
**示例**：  
```c
printf("Exiting without cleanup...\n");
_Exit(0);
```


#### math.h


**1. `sqrt`**  
**功能**：计算平方根。  
**函数原型**：`double sqrt(double x);`  
**示例**：  
```c
printf("%f\n", sqrt(16.0)); // 输出 4.000000
```

---

**2. `pow`**  
**功能**：计算 x 的 y 次幂。  
**函数原型**：`double pow(double x, double y);`  
**示例**：  
```c
printf("%f\n", pow(2.0, 3.0)); // 输出 8.000000
```

---

**3. `fabs`**  
**功能**：计算绝对值（浮点数）。  
**函数原型**：`double fabs(double x);`  
**示例**：  
```c
printf("%f\n", fabs(-5.5)); // 输出 5.500000
```

---

**4. `ceil`**  
**功能**：向上取整。  
**函数原型**：`double ceil(double x);`  
**示例**：  
```c
printf("%f\n", ceil(2.3)); // 输出 3.000000
```

---

**5. `floor`**  
**功能**：向下取整。  
**函数原型**：`double floor(double x);`  
**示例**：  
```c
printf("%f\n", floor(2.7)); // 输出 2.000000
```

---

**6. `round`**  
**功能**：四舍五入到最近的整数值。  
**函数原型**：`double round(double x);`  
**示例**：  
```c
printf("%f\n", round(2.5)); // 输出 3.000000
```

---

**7. `fmod`**  
**功能**：计算浮点数的余数。  
**函数原型**：`double fmod(double x, double y);`  
**示例**：  
```c
printf("%f\n", fmod(7.5, 2.0)); // 输出 1.500000
```

---

**8. `exp`**  
**功能**：计算 e 的 x 次幂。  
**函数原型**：`double exp(double x);`  
**示例**：  
```c
printf("%f\n", exp(1.0)); // 输出 2.718282
```

---

**9. `log`**  
**功能**：计算自然对数（以 e 为底）。  
**函数原型**：`double log(double x);`  
**示例**：  
```c
printf("%f\n", log(2.718282)); // 输出 1.000000
```

---

**10. `log10`**  
**功能**：计算常用对数（以 10 为底）。  
**函数原型**：`double log10(double x);`  
**示例**：  
```c
printf("%f\n", log10(100.0)); // 输出 2.000000
```

---

**11. `sin`**  
**功能**：计算弧度值的正弦值。  
**函数原型**：`double sin(double x);`  
**示例**：  
```c
printf("%f\n", sin(3.141592 / 2)); // 输出 1.000000
```

---

**12. `cos`**  
**功能**：计算弧度值的余弦值。  
**函数原型**：`double cos(double x);`  
**示例**：  
```c
printf("%f\n", cos(3.141592)); // 输出 -1.000000
```

---

**13. `tan`**  
**功能**：计算弧度值的正切值。  
**函数原型**：`double tan(double x);`  
**示例**：  
```c
printf("%f\n", tan(3.141592 / 4)); // 输出 1.000000
```

---

**14. `asin`**  
**功能**：计算反正弦（弧度值）。  
**函数原型**：`double asin(double x);`  
**示例**：  
```c
printf("%f\n", asin(1.0)); // 输出 1.570796
```

---

**15. `acos`**  
**功能**：计算反余弦（弧度值）。  
**函数原型**：`double acos(double x);`  
**示例**：  
```c
printf("%f\n", acos(0.0)); // 输出 1.570796
```

---

**16. `atan`**  
**功能**：计算反正切（弧度值）。  
**函数原型**：`double atan(double x);`  
**示例**：  
```c
printf("%f\n", atan(1.0)); // 输出 0.785398
```

---

**17. `atan2`**  
**功能**：计算 y/x 的反正切值（弧度值，考虑象限）。  
**函数原型**：`double atan2(double y, double x);`  
**示例**：  
```c
printf("%f\n", atan2(1.0, 1.0)); // 输出 0.785398
```

---

**18. `hypot`**  
**功能**：计算欧几里得距离（`sqrt(x^2 + y^2)`）。  
**函数原型**：`double hypot(double x, double y);`  
**示例**：  
```c
printf("%f\n", hypot(3.0, 4.0)); // 输出 5.000000
```

---

**19. `cbrt`** *(C99标准新增)*  
**功能**：计算立方根。  
**函数原型**：`double cbrt(double x);`  
**示例**：  
```c
printf("%f\n", cbrt(27.0)); // 输出 3.000000
```

---

**20. `round`**  
**功能**：返回最接近的整数（四舍五入）。  
**函数原型**：`double round(double x);`  
**示例**：  
```c
printf("%f\n", round(3.5)); // 输出 4.000000
```

---

**21. `trunc`**  
**功能**：截断小数部分，保留整数部分。  
**函数原型**：`double trunc(double x);`  
**示例**：  
```c
printf("%f\n", trunc(3.9)); // 输出 3.000000
```

---

**22. `modf`**  
**功能**：将浮点数分解为整数和小数部分。  
**函数原型**：`double modf(double x, double *iptr);`  
**示例**：  
```c
double intpart, fracpart;
fracpart = modf(3.14, &intpart);
printf("Integer: %f, Fraction: %f\n", intpart, fracpart); // 输出 "Integer: 3.000000, Fraction: 0.140000"
```

---

**23. `fmax`** *(C99标准新增)*  
**功能**：返回两个浮点数中的较大值。  
**函数原型**：`double fmax(double x, double y);`  
**示例**：  
```c
printf("%f\n", fmax(3.0, 4.5)); // 输出 4.500000
```

---

**24. `fmin`** *(C99标准新增)*  
**功能**：返回两个浮点数中的较小值。  
**函数原型**：`double fmin(double x, double y);`  
**示例**：  
```c
printf("%f\n", fmin(3.0, 4.5)); // 输出 3.000000
```

---

**25. `copysign`** *(C99标准新增)*  
**功能**：将 y 的符号赋值给 x。  
**函数原型**：`double copysign(double x, double y);`  
**示例**：  
```c
printf("%f\n", copysign(3.0, -4.0)); // 输出 -3.000000
```


