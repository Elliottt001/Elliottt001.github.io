
## 数据类型

### 变量和常量
#### 变量

- 作用：开一块内存放数据
- 定义：
    - C89：变量必须在程序一开始全部定义
    - C99：任何位置都可以定义变量
- 名字（标识符）
    
    规则：字母数字下划线组成；数字不能是第一个字符；不能是关键字

- 赋值：动态局部变量若不赋值则随机值

##### 全局变量

生存期和作用域独立于函数，都在全局。

**初始化**：

- 可以初始化，但要求是只能用编译时刻已知的值来初始化它，这里，全局变量的初始化在main函数之前。
- 不初始化：数字得到0；指针得到NULL

示例：

```c
int gAll = 12;  // 编译通过

int gAll = f();  // 编译错误

int gAll = 12;
int g2 = gAll;  // 编译错误

const int gAll;
int g2 = gAll;  // 编译通过，但是不建议这样，尤其在大程序中。

int g2 = gAll; 
const int gAll;  // 编译错误
```

**（全局）变量的覆盖**

在更小的地方定义的变量，会将更大的地方定义的同名变量覆盖

- 函数内部本地变量会掩盖全局覆盖

- 函数内部再开一个块（{ }），在里面定义一个变量，他会覆盖这个块外面的同名变量。

##### 静态本地变量

**语法：** 变量定义前面加上 `static` 修饰符。

**特点：** 

- 函数离开时，保留其值

- 和全局变量在相同的内存区域（很小的地址），而动态本地变量的地址很大

- 生存期：全局；作用域：函数内部（只有函数内部可以访问，这也是 `static` 的意思：局部作用域。

**使用**

- <span style = "color: blue;"> 函数返回本地变量的地址 / 的值 会有warning </span> ：这个变量在函数结束后就没了

- 不要使用全局变量在函数之间传递参数和结果

- 尽量避免使用全局变量，使用全局变量和静态本地变量的函数是线程不安全的。

**其他**

- C语言有很多区放变量：常量区、静态区、栈区、堆区
- 动态变量 auto
    - 特点：调用一次分配一次内存，调用结束就释放了，重来
    - 定义：在C语言中，`auto` 关键字用于声明自动存储期的局部变量。它告诉编译器，该变量应该在栈上分配，并且其生命周期仅限于声明它的函数或代码块。然而，`auto` 关键字实际上是可选的，因为在函数内部声明的变量默认就是自动存储期的。
    - 在C99标准之前，`auto` 关键字是必需的，但在C99及以后的标准中，它变得可选。
- 静态变量 static
    - 特点：整个程序运行期间存在，等程序结束后释放
- 静态全局变量
    - 作用：只可以使其在声明的文件中可见，避免与其他文件中同名变量冲突
- 静态函数 ```static int function_name(parameter_type parameter)```
    - 作用：只能在所声明的文件中调用，其他文件不可使用：辅助函数、实用函数限制在特定文件中
- 静态局部变量
    - 定义：函数内部定义的静态变量
    - 作用：类似全局变量，函数调用结束后，其值不会被销毁，而是保持存在
    - 用处：重复使用，这一次的接着上一次的值用

```c
#include<stdio.h>
//三个变量都赋初始值0
int global = 0;  //global为全局变量
void stc()
{
    int n = 0;  //n 为局部变量
    static int sta = 0;  //sta为静态局部变量
    n++; sta++; global++;  //函数每次执行都对三个变量+1
    printf("%d ", n); printf("%d ", sta); printf("%d ", global);
}
int main()
{
    int i;
    for(i = 1; i <= 5; i++){
        stc(); printf("\n");  //三次调用函数
    }
    return 0; 
}
/* 输出：
1 1 1 
1 2 2 
1 3 3 
1 4 4 
1 5 5 
全局变量和静态局部变量都延续了上次调用的结果继续+，局部变量从初始值开始
*/
```


#### 常量

**定义**

-  `const` 只读变量

    可全局/局部，eg：`const double PI = 3.1415;`
-  `#define` 宏
    
    eg：`#define PI 3.1415`

**字符串常量**

`__func__` ：表示当前函数的名称。

- 它在函数的任何地方都可以使用，不需要传递或定义额外的变量。
- __func__的值是编译器在编译时自动填充的，且是一个预定义标识符，故不能被重新定义。


**基本数据类型总表:**

| 类别   | 名称             | 类型名                | 数据长度 | 取值范围                              | 格式说明符 |
|--------|------------------|-----------------------|----------|---------------------------------------|------------|
| 整型   | \[有符号] 整型    | int                   | 32 位     | $-2^{31}$ ~ $2^{31}-1$               | %d         |
|        | \[有符号] 短整型  | short \[int]          | 16 位     | $-2^{15}$ ~ $2^{15}-1$               | %hd        |
|        | \[有符号] 长整型  | long \[int]           | 32 位     | $-2^{31}$ ~ $2^{31}-1$               | %ld        |
|        | 无符号整型       | unsigned \[int]       | 32 位     | $0$ ~ $2^{32}-1$                     | %u         |
|        | 无符号短整型     | unsigned short \[int] | 16 位     | $0$ ~ $2^{16}-1$                     | %hu        |
|        | 无符号长整型     | unsigned long \[int]  | 32 位     | $0$ ~ $2^{32}-1$                     | %lu        |
| 字符型 | 字符型           | char                 | 8 位      | $0$ ~ $255$                          | %c         |
| 浮点型 | 单精度浮点型     | float                | 32 位     | 约 $10^{-38}$ ~ $10^{38}$            | %f         |
|        | 双精度浮点型     | double               | 64 位     | 约 $10^{-308}$ ~ $10^{308}$          | %lf        |


**注**: 

- 方括号中的内容可以省略。

- bit位数：0 ~ 长度-1 位；符号位：最高位（第长度-1位）

- 	十进制Decimal 八进制Octal（%o） 十六进制Hexadecimal（%x）

    16进制：X对应A~F； x对应a~f


### 整型

**定义**

1. 整型常量 == 整数数字
2. 整型变量

**存储**

让计算机用特定byte存数字：加后缀eg：`123L`,`123UL`，但是短整型没有类似表示

**数字编码**

- 补码：

    使得数据的表示唯一：主要是0和-0统一；使得减法用加法做

    内存中按补码存储


正数：

三个码相同：符号位为 **0**，其余为其二进制

负数：

- 原码：符号位1，其他位与为绝对值的二进制
- 反码：符号位1不变，除符号位其他为原码的反
- 补码：反码 + 1

负数三码转换

- 转换原因：内存中补码存储/运算；知道原码才知道数字是多少

- 原码 —— 补码：

    - 负数 取反（符号位不变） + 1

- 补码转原码：
    
    - 负数法一：减 1，按位取反，符号位不变。
    - 负数法一：补码的补码是原码

溢出：会有进位，溢出最高位舍

**示例**

```c
int a = -1;
printf("%d, %u", a, a);
//结果：-1, 4294967295
printf("%o, %x", a, a);
//结果：37777777777, ffffffff
```

**直接利用格式说明符完成进制转换：**

```c
printf("%d, %o, %x", 10, 10, 10);
printf("%d, %d, %d", 10, 010, 0x10);
```

### 实型/浮点型
	
**定义**

表示形式：小数/科学计数法( %e )

数据精度 与 取值范围是两个不同的概念：

float x = 1234567.89;   x虽在取值范围内，但无法精确表达。 

float y = 1.2e55;   y 的精度要求不高，但超出取值范围。


**存储**

??? info "IEEE 754标准" 
	
	浮点数分三个部分,依次是：

	1. **符号位**（Sign bit）：1位，表示数值正负，0正1负数。

	2. **指数位**（Exponent）：存储指数部分，单精度为8位，双精度为11位。指数部分采用偏移量（bias）表示，单精度的偏移量为127，双精度的偏移量为1023。

	3. **尾数位**（Mantissa，也称为有效数字或 significand）：存储有效数字部分，单精度为23位，双精度为52位。尾数部分通常不包括最高位的1（隐含的前导1），除了特殊情况。

	举例

	假设有一个双精度浮点数 `3.14`，其二进制表示为 `1.1001000110100010100011110100110110`（不包括隐含的前导1），则其在内存中的存储方式如下：

	1. **符号位**：0（因为3.14是正数）
	2. **指数**：计算指数部分，3.14的二进制科学计数法为 `1.1001000110100010100011110100110110 * 2^1`，指数为1，加上偏移量1023，得到1024，二进制为 `10000000000`。
	3. **尾数**：`1001000110100010100011110100110110`（不包括隐含的前导1）

	因此，3.14在内存中的存储为：

	```
	0 10000000000 1001000110100010100011110100110110
	```


特点：不能精确存储

```c
printf("%d", 2.1 - 1 == 0.1);  //输出：0
printf("%d", 0.1 == 0.1);  //输出：1（非零）
```
```c
//判断俩实数是否相等
/*
wrong:
if(f1 == f2){}
*/
fabs(f1 - f2) < 1e-12  //其实1e-8就够了
```

### 字符型

**定义**
	
- 字符型变量

- 字符型常量：单个字符，`'A'` `'\n'` 是正确的定义方式，得加上单引号 

**存储**

存ASCII

??? info "转义字符" 

	1. **多行字符串**：
	```c
	printf("Line 1 \
	Line 2");
	//输出：Line 1 Line 2
	```

	2. **包含特殊字符的字符串**：
	```c
	char str[] = "He said, \"Hello, World!\"";
	//输出: He said, "Hello, World!"
	```

	4. **使用退格符**：
	```c
	printf("Type \bnot\b me\n");
	```
	这里，`\b` 是退格符，用于删除前一个字符。输出结果将是：
	```
	Type  me
	```

	5. **使用空字符**：
	```c
	char str[] = "Hello\0World";
	printf("%s\n", str);
	```
	这里，`\0` 是空字符，它将字符串在 `Hello` 后面截断，所以 `World` 不会被打印出来。输出结果将是：
	```
	Hello
	```

	6. **使用回车符和换行符**：
	```c
	printf("First line.\rSecond line.\n");
	```
	这里，`\r` 是回车符，将光标移动到行首，然后打印 `Second line.`，覆盖了 `First line.`。输出结果将是：
	```
	Second line.
	```

	所有字符都可以用转义字符表示（即：使用8 or 16 进制转义序列）
	eg：打印`A`
    ```c
    printf("%c\n", 'A'); //直接
    ```
    ```c
    printf("%c\n", 65); //ASCII
    ```
    ```c
    printf("%c\n", '\x41'); //使用转义序列`\x`后跟十六进制的ASCII码值打印`A`（在支持C99标准或更高版本的编译器中）
    ```
    ```c
    printf("%c\n", '\101'); //八进制的ASCII码, 注意有''单引号
    ```

**关系**: 整型和字符型可以按ASCII随便交换

### 类型转换

**零、情况**

1. 不同类型数据的混合运算
2. *整型数据除法需要得到小数*

**一、自动**

**（一）、非赋值运算**

1. 理论

	![alt text](res/images/image-4_1.png)
    
	水平方向：自动；垂直方向：低 —>高 

**（二）、赋值运算**
1. 理论

	![alt text](res/images/image-5_1.png)
	
2. 示例：
    ```c
    short bi;
    bi = 0x12345678L; //长整型十六进制
    printf("%d", bi);
    /*
    warning: overflow in conversion from ‘long int’ to ‘short int’ changes value from ‘305419896’ to ‘22136’ [-Woverflow]
    11 | bi = 0x12345678L;
        |      ^~~~~~~~~~~
    */
    ```
数值溢出时：

**截断**：由于数值超出了 `short` 类型的范围，编译器会将这个数值截断到 `short` 类型能表示的范围。具体来说，它会取这个数值的低16位。`0x12345678L` 的二进制表示是 `0001 0010 0011 0100 0101 0110 0111 1000`，取低16位是 `0101 0110 0111 1000`，即 `0x5EF8`。

**二、强制类型转换**

**语法：** (类型名)  表达式

**示例：**

```C
    printf("(double)3 = %.1f\n", (double)3); // 3.0
    printf("(int)3.8 = %d\n", (int)3.8);  //3
    printf("(int)-1.6 = %d\n", (int)-1.6);  //-1
    printf("(double)(5/2) = %.1f\n", (double)(5 / 2));  //2.0
    printf("(double)5/2 = %.1f\n", (double)5 / 2);  //2.5
    //后两个：看优先级：（）比（类型名）高。所以倒数第二个：先5/2 = 2，再(double)2 = 2.0 ，最后一个先(double)5 = 5.0，再5.0/2 = 2.5（发生了自动类型转换）

    int i;        // Integer variable
    double x;     // Double variable
    x = 3.8;      // Assign 3.8 to x
    i = (int)x;   // Cast x to int, truncating 3.8 to 3
    printf("x = %f, i = %d\n", x, i);
    // Output: x = 3.800000, i = 3
    printf("(double)(int)x = %f\n", (double)(int)x); 
    // Cast x to int (3) and then cast back to double (3.0)
    // Output: (double)(int)x = 3.000000
    printf("x mod 3 = %d\n", (int)x % 3); 
    // Cast x (3.8) to int (3), then compute 3 % 3 = 0
    // Output: x mod 3 = 0
```

### 枚举

**定义&规则：**

```c
enum 枚举名 {
    枚举常量1,
    枚举常量2,
    ...
};  //带上分号
```

- C内部 `enum` 其实就是 `int`，可以当作 `int` 做运算
- **枚举名**：是枚举类型的名字（可选，因为一般不用）。
- **枚举常量**：是一组合法的标识符，（必要，需要用）类型是`int`常量，默认从 `0` 开始依次递增。
- 枚举中的常量必须唯一

- **不能直接输入枚举常量的名字：**

    枚举常量不能通过输入输出函数直接读写。例如，不能用 `scanf` 读取枚举类型，必须通过整数变量赋值。

- **类型安全性：**

    枚举变量的值可以超出定义的范围（尽管不推荐），因为底层实现是整数。例如：

  ```c
  enum Color { RED, GREEN, BLUE };

  int main() {
      enum Color myColor = 5; // 合法，但不推荐
      printf("%d\n", myColor); // 输出 5
      return 0;
  }
  ```


**意义**：

命名的一组需要排列的整数常量，用于固定类别、状态和选项的表示。可读性，易于维护。


**使用**

```c
enum Color {
    RED,    // 默认值为 0
    GREEN,  // 默认值为 1
    BLUE    // 默认值为 2
};
```

这里定义了一个枚举类型 `Color`，它包含了三个枚举常量：`RED`、`GREEN` 和 `BLUE`。这些常量的默认值分别是 `0`、`1` 和 `2`。


**为枚举常量指定值**

可以显式为枚举常量指定值。如果未指定值，则该常量的值为前一个常量值加 `1`。

```c
enum Day {
    MON = 1,  // MON 的值是 1
    TUE,      // TUE 的值是 2
    WED = 5,  // WED 的值是 5
    THU,      // THU 的值是 6
    FRI = 10, // FRI 的值是 10
    SAT,      // SAT 的值是 11
    SUN       // SUN 的值是 12
};
```

**定义枚举变量**

```c
enum Color { RED, GREEN, BLUE };

int main() {
    enum Color myColor; // 定义一个枚举变量
    myColor = GREEN;    // 为变量初始化枚举常量
    printf("myColor = %d\n", myColor); // 输出 1
    scanf("%d", &myColor);  // 输入 5
    printf("%d", myColor);  // 输出 5
    printf("%d", GREEN); // 输出 1
    return 0;
}
//GREEN的值不会变成5啊，因为枚举常量的值是固定的，且在编译时已经确定。赋值给枚举变量（如 myColor）时，只是改变了变量的值，不会修改枚举常量的值。
```

---

**匿名枚举**

如果不需要多次引用枚举类型名称，可以省略枚举类型的名字，直接使用枚举常量。

```c
enum { MON, TUE, WED, THU, FRI, SAT, SUN };

int main() {
    int today = WED; // 直接使用枚举常量
    printf("Today is day number: %d\n", today); // 输出 2
    return 0;
}
```

**计数**

`Color{c1, c2, c3, c4, cnt};` 这里`cnt`值是4，记录了前面枚举变量的个数，可以用它来循环……

**具体使用场景**

在底层，枚举类型的常量其实是整数（`int` 类型）。因此，枚举常量可以用于任何需要整数值的地方。

```c
enum Status { OFF, ON };

int main() {
    enum Status light = OFF;

    if (light == OFF) {
        printf("Light is off\n");
    }
    return 0;
}
```


```c
//状态开关机
enum State { INIT, RUNNING, STOPPED };

void checkState(enum State s) {
    switch (s) {
        case INIT:    printf("Initializing...\n"); break;
        case RUNNING: printf("Running...\n"); break;
        case STOPPED: printf("Stopped.\n"); break;
        default:      printf("Unknown state!\n");
    }
}
```


### 结构

结构是一种数据类型，它在语法上与python中的字典、类都有相似之处。

想不清楚时，将其当作int类型。因为本质上其都是一种数据类型。

示例：

```c

#include <stdio.h>
#include <string.h>

struct student {
    char name[50];  
    int age;
    long int id;
    char gender[10]; 
    double height;
    char bloodtype;
};  //这是一条C语言定义变量的语句，别忘了最后的分号；另外这段代码的作用是“声明结构类型”

int main() {
    struct student students[3];  //这是在定义一个结构变量
    // 设置第一个学生的属性
    strcpy(students[0].name, "Alice");
    students[0].age = 20;
    students[0].id = 123456789;
    strcpy(students[0].gender, "female");
    students[0].height = 1.65;
    students[0].bloodtype = 'A';

    // 设置第二个学生的属性
    strcpy(students[1].name, "Bob");
    students[1].age = 22;
    students[1].id = 987654321;
    strcpy(students[1].gender, "male");
    students[1].height = 1.80;
    students[1].bloodtype = 'B';

    // 设置第三个学生的属性
    strcpy(students[2].name, "Charlie");
    students[2].age = 19;
    students[2].id = 555555555;
    strcpy(students[2].gender, "male");
    students[2].height = 1.75;
    students[2].bloodtype = 'O';

    // 输出每个学生的信息
    for (int i = 0; i < 3; i++) {
        const char *pronoun;
        if (strcmp(students[i].gender, "male") == 0) {
            pronoun = "his";
        } else {
            pronoun = "her";
        }
        printf("%s, a %d-year-old student, %s ID is %ld.\n", students[i].name, students[i].age, pronoun, students[i].id);
    }

    return 0;
}
```

#### 语法

- 一般情况将结构放在函数外面（全局变量的位置）
- 别的写法：

    ![alt text](res/images/image-10_1.png)

**1. 初始化**：

- 对于结构体数组，不可`students[0] = {"Alice", 20, 12345, female, 1.65, 'A'};`类似这样初始化，只能像上面范例程序一样一个一个初始化。如果想这样，只能在定义时就这样初始化，而非定义后再赋值，像这样:
```c
struct Student students[10] = {
    {"Alice", 20, 12345, female, 1.65, 'A'}, // 初始化第一个元素
    // 其他元素将自动初始化为0（对于数值类型）或空字符串（对于字符数组），但是请注意，上面的语法是在数组声明时对整个数组（或部分数组）进行初始化，而不是在数组已经声明之后对单个元素进行初始化。
};
```

示例：

```c
#include <stdio.h>
#include <string.h>

// 定义结构体
struct Person {
    char name[50];
    int age;
    float height;
};

// 通过函数初始化结构体
void initializePerson(struct Person* p, const char* name, int age, float height) {
    strcpy(p->name, name);
    p->age = age;
    p->height = height;
}

int main() {
    // 直接赋值初始化
    struct Person person1;
    person1.age = 25;
    strcpy(person1.name, "Alice");
    person1.height = 5.7;

    // 使用初始化列表初始化（C99标准及以上支持）
    struct Person person2 = {"Bob", 30, 6.0};

    // 使用初始化列表初始化，并使用类似“关键词传参”的方式
    struct Person person3 = {"zrz", .age = 18, .height = 8.0}

    // 列表初始化，若不给某int变量传值，默认0

    // 通过函数初始化
    struct Person person4;
    initializePerson(&person4, "Charlie", 22, 5.9);

    return 0;
}
```

**2. 访问结构成员**

语法：```结构变量.结构成员```

!!! warning "概念"

    结构类型：虚的，一开始定义的那个是结构类型，例如上面的Person
    结构变量：基于结构类型定义了许多结构变量，例如上面的person1, person2 ……

**3. 结构运算**

重点注意其与数组的区别

- 可以用结构变量的名字访问整个结构
- 对于整个结构，可以整体赋值，
    ```c
    person1 = (struct Person){"Bob", 30, 6.0};
    //做一个类型转换，相当于上面初始化的操作
    ```
    ```c
    person2 = person1
    //这是合法的，相当于每个元素都相等，注意这俩结构变量还是不一样的，只不过其中的成员的值是一样的
    ```

- 整个结构，可以取地址

    注意，结构变量名不是他的地址，取地址必须得用`&`

    ```c
    struct Person *p_person1 = &person1;
    ```

- 整个结构，可以作为参数传递给函数

#### 结构与函数

整个结构可以作为参数传入函数，这时是在函数内新建一个结构变量，并赋值传入的那个结构的值

结构可以作为函数的返回值

**输入结构：**

结构与数组的区别：

- 在传入函数时，结构与普通的int变量类似，要在函数内部更改它，得传地址。因为传入函数，函数接收到的实际是结构的值，不是这个变量，与原结构无关。

- 数组在传入函数时，传入的是这个数组变量。

解决方案1：在函数内部copy一个一样的临时的结构变量，讲这个结构返回

```c
struct point inputStruct(void)
{
    struct point p{/*代码块，要求与main函数里面的一样*/};
    /*代码块*/
    return p;
}

int main()
{
    struct point dest{/*代码块*/};
    dest = inputStruct();
    printf(/*语句*/)
}
```
该方法不好

解决方案2：

!!! quote "K&R"

    “lf a large structure is to be passed to a function, it is generally more efficient to pass a pointer than to copy the whole structure”


**指向结构的指针**

!!! success "指针与函数"

    常用：一个函数的参数是指针，返回值也是指针；目的是将这个值的指针输入，在函数内部更改完之后再返回出去，好处是返回的指针可以再用于其他代码，例如作为其他函数的参数，反复调用。

语法：`pointer -> member`，代表 “这个指针所指的那个结构变量里的那个成员”。

示例：
```c
/*定义一个结构变量today，里面有一个成员是month*/
struct date today;
struct date* ptoday = &today;
(*p).month = 12;
p -> month = 12;
```

**使用示例：**

```c
#include<stdio.h>
struct date {
    int month;
    int day;
};

struct date* getStruct(struct date *p);
void printSturct(const struct date* p);

int main()
{
    struct date today;
    printSturct(getStruct(&today));
    
    *getStruct(&today) = (struct date){12, 18};
    printSturct(&today);

    getStruct(&today) -> day = 19;
    printSturct(&today);
    return 0;
}

struct date* getStruct(struct date *p)
{
    scanf("%d %d", &(p -> month), &(p -> day));
    return p;
}

void printSturct(const struct date* p)
{
    printf("%d-%d\n", p -> month, p -> day);
}
```

#### 结构数组

*结构数组的本质是**数组**，只不过该数组的元素是结构体类型的数据*


**语法**

```c
struct class {
    char* name;
    int age;
    long int id;
};

int main()
{
    struct class student[26] = {{"zrz", 18, 3240105996}, {"hhh", 18, 3240100000}};
}
```

#### 结构中的结构

**语法：**还是按照普通变量来理解

**示例：**
```c
struct point {
    int x;
    int y;
};

struct rectangle {
    struct point pt1;
    struct point pt2;
};

int main()
{
    struct rectangle rt1;
    struct rectangle *prt1 = &rt1;
    scanf("%d %d", &(rt1.pt1.x), &(rt1.pt1.y));
    scanf("%d %d", &(prt1 -> pt2.x), &(prt1 -> pt2.y));
}
```



另外，结构和数组等可以无限组合嵌套，例如结构中的结构的数组

### 联合

**定义语法**：与结构很像

```c
union Person{
    char* name;
    int age;
};
```
```c
typedef union person{
    char* name;
    int age;
}Person;
//使用typedef
```

**存储**：

- 所有成员共享一个内存空间

- 同一时间只有一个成员是有效的

    即填入另一个成员的值即将前面的冲掉

- 联合的大小`sizeof(union)`是其最大的成员

**初始化**：对第一个成员初始化

**应用场景**


1. **节省内存**：   
   联合最常见的用途之一是节省内存。例如，在处理需要多种数据类型但只会使用其中一种的场景下，使用联合可以避免每种数据类型都占用单独的内存区域。
   ```c
   union Data {
       int i;
       float f;
       char str[20];
   };
   ```
   在这个例子中，`Data`联合只需要足够存储最大的成员（`char str[20]`）的内存，而不需要分别为`int`、`float`和`char[]`分配内存空间。

2. **简化存储不同格式的数据**：   
   联合可以存储不同类型的数据，在需要存储多种不同数据格式但只需存储一个格式的情况下特别有用。例如，读取网络数据时，我们可能会在同一位置存储整数、浮点数或字符串等不同数据类型。
   ```c
   union Packet {
       int data_int;
       float data_float;
       char data_string[50];
   };
   ```

3. **实现类型安全的多态（polymorphism）**：   
   在没有面向对象支持的语言（如C语言）中，可以使用联合类型模拟多态。联合类型允许函数根据需要选择合适的数据类型来操作。
   ```c
   union Value {
       int intVal;
       float floatVal;
   };

   void printValue(union Value v, int isInt) {
       if (isInt) {
           printf("Integer: %d\n", v.intVal);
       } else {
           printf("Float: %.2f\n", v.floatVal);
       }
   }
   ```
   通过使用`isInt`标识符，函数`printValue`可以根据需要处理不同类型的数据。

4. **嵌入式系统中的硬件寄存器操作**：
   在嵌入式开发中，联合可以方便地访问硬件寄存器的不同部分。例如，一个32位的硬件寄存器可以被分解为多个8位字段。
   ```c
   union Register {
       unsigned int regVal;  // 32位的寄存器值
       struct {
           unsigned char lowByte;
           unsigned char highByte;
           unsigned char midByte1;
           unsigned char midByte2;
       };
   };
   ```
   通过使用联合，程序可以以不同的方式访问寄存器的内容（如整个32位寄存器或分解后的各个字节）。

5. **类型转换（Type casting）**：
   联合在C语言中也常用于类型转换，尤其是在需要通过不同类型的视图来查看同一块内存数据时。例如，在实现某些特定算法时，可能需要通过联合来在整数和浮点数之间进行转换。
   ```c
   union Convert {
       int i;
       float f;
   };

   union Convert c;
   c.i = 10;
   printf("As float: %.2f\n", c.f);  // 通过联合将整数以浮点数显示
   ```

？？？为啥？到底是几？

6. **实现简易的自定义数据结构**：
   联合可以用于实现自定义的数据结构。例如，当数据结构中有多个可能的数据类型时，可以使用联合来减少内存占用。
   ```c
   struct Shape {
       int type;
       union {
           int radius;     // 圆形
           struct {        // 矩形
               int width;
               int height;
           };
       };
   };
   ```
   在这个例子中，`Shape`结构体根据`type`字段的不同值来区分它是圆形还是矩形，并通过联合在同一内存位置存储不同的数据类型。



1. **解析复杂的数据格式**：
   联合类型非常适合用来解析复杂的二进制数据格式。不同的数据字段可以用不同的方式解读。使用联合可以更方便地从一个字节流中提取不同类型的数据，常见于文件解析或网络数据包的处理。
   ```c
   union DataPacket {
       uint32_t integerData;
       float floatData;
       char stringData[16];
   };

   union DataPacket packet;
   packet.integerData = 0x12345678;  // 作为整数处理
   printf("Integer: %u\n", packet.integerData);
   packet.floatData = 3.14159f;       // 作为浮点数处理
   printf("Float: %.4f\n", packet.floatData);
   packet.stringData[0] = 'H';       // 作为字符串处理
   packet.stringData[1] = 'i';
   packet.stringData[2] = '\0';
   printf("String: %s\n", packet.stringData);
   ```

2. **用于操作不同数据结构**：
   联合可以用来处理包含多种不同数据结构的数据，例如，某个函数可能需要在不同情况下处理不同的数据结构。通过联合，你可以在同一个内存空间内实现这些数据结构的共享。
   ```c
   union Data {
       struct {
           int x;
           int y;
       } point;  // 用于存储坐标
       struct {
           int width;
           int height;
       } rectangle;  // 用于存储矩形尺寸
   };
   ```
   在这个例子中，`Data`联合可以存储一个坐标点或一个矩形的尺寸，但不能同时存储两者。

3. **优化内存池管理**：
   在内存池管理中，联合可用于构建高效的内存分配方案。例如，在一个内存池中管理不同类型的对象时，使用联合类型可以为每个对象节省内存。
   ```c
   union Object {
       int intValue;
       float floatValue;
       char strValue[50];
   };

   struct MemoryPool {
       union Object objects[100];
   };
   ```
   这里的内存池`MemoryPool`可以用来管理100个对象，每个对象可能是一个整数、浮点数或字符串，而不必为每种类型分配不同的内存块。

4. **简化图像处理中的像素表示**：
   在图像处理或图形编程中，像素的数据表示可以使用联合来简化处理。例如，一个像素可能包含RGB（红、绿、蓝）三个颜色通道，可以将其表示为一个整数，也可以将每个通道分开存储。
   ```c
   union Pixel {
       uint32_t rgba;  // 32位整数表示一个像素
       struct {
           unsigned char r;
           unsigned char g;
           unsigned char b;
           unsigned char a;  // alpha透明度
       };
   };
   ```

5. **模拟操作系统中的进程状态**：
   在操作系统中，可以使用联合来模拟进程的不同状态。一个进程的状态可能包含不同类型的数据结构（如寄存器值、程序计数器、堆栈指针等）。通过联合，可以根据需要访问不同的状态信息。
   ```c
   union ProcessState {
       uint32_t registers[8];  // 存储8个通用寄存器
       struct {
           uint32_t pc;  // 程序计数器
           uint32_t sp;  // 堆栈指针
       };
   };
   ```
   通过使用联合，操作系统内核可以方便地访问进程的寄存器内容或程序计数器与堆栈指针。

6. **模拟设备控制寄存器**：
   在硬件编程中，联合类型常用于模拟设备的控制寄存器，其中不同的控制位可能对应不同的控制功能。通过联合，可以以不同的视角来访问同一寄存器。
   ```c
   union ControlRegister {
       uint32_t regValue;  // 32位寄存器值
       struct {
           unsigned bit0 : 1;  // 控制位0
           unsigned bit1 : 1;  // 控制位1
           unsigned bit2 : 1;  // 控制位2
           unsigned bit3 : 1;  // 控制位3
           unsigned bit4 : 1;  // 控制位4
           unsigned reserved : 27;  // 其他保留位
       };
   };
   ```
   在这个例子中，`ControlRegister`联合让你可以直接访问控制寄存器的32位值，也可以单独操作每个控制位。

??? info "总结"

    C语言中的联合类型是一种有效的节省内存的工具，特别适合在程序中存储和操作多种类型的数据。它能够用于实现多态、硬件寄存器的高效操作、类型转换、数据结构优化等多种实际应用。通过共享内存空间，联合可以极大地减少内存消耗，尤其是在内存资源有限的嵌入式系统和其他高效计算场景中。

### 自定义数据类型（typedef）

**语法：**

```c
typedef 原类型名 自定义新类型名;
```
例如，`typedef int Length;` ：这样，`Length` 成为 `int` 的别名，可以代替 `int` 。

再如；

```c
typedef struct adate{
    int month;
    int day;
    int year;
} Date;
Date d = {12, 17, 2024};
```
`Date` 代表 `typedef` 和 `Date` 中间所有东西，`Date` $\Leftrightarrow$ `struct adate`



`typedef` 用于给现有类型定义新的别名或创建易于使用的自定义类型。

---

**1. 简化复杂类型**
为指针类型创建别名，简化代码的书写和阅读。

```c
#include <stdio.h>

// 为指针类型定义别名
typedef char* String;

int main() {
    String name = "Alice";
    printf("Name: %s\n", name);
    return 0;
}
```

**解析**：`String` 是 `char*` 的别名，简化了定义指针变量的代码。

---

**2. 定义结构体的别名**
为结构体类型创建更简洁的名称。

```c
#include <stdio.h>

// 定义结构体和别名
typedef struct {
    int x;
    int y;
} Point;

int main() {
    Point p = {10, 20};
    printf("Point: (%d, %d)\n", p.x, p.y);
    return 0;
}
```

**解析**：使用 `typedef` 后，定义变量时无需再写 `struct`，直接使用 `Point`。

---

**3. 定义枚举类型的别名**
为枚举类型起一个更直观的名字。

```c
#include <stdio.h>

// 定义枚举类型和别名
typedef enum { RED, GREEN, BLUE } Color;

int main() {
    Color favoriteColor = GREEN;
    printf("Favorite color code: %d\n", favoriteColor);
    return 0;
}
```

**解析**：`Color` 是枚举类型的别名，代码更直观。

再例，

```c
typedef enum { false, true } bool;
bool palindrome(char *s) { /*代码块*/}
```

---

**4. 定义自定义数据类型**
将常用的基础类型替换为更具语义的名字。

```c
#include <stdio.h>

// 定义一个长度类型
typedef unsigned int Length;

int main() {
    Length len = 100;
    printf("Length: %u\n", len);
    return 0;
}
```

**解析**：`Length` 是 `unsigned int` 的别名，用于表示逻辑上的长度，增加代码语义。

---

**5. 定义函数指针的别名**
为函数指针类型定义别名，简化函数指针的声明和使用。

```c
#include <stdio.h>

// 定义函数指针类型
typedef int (*Operation)(int, int);

// 函数定义
int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    Operation op;  // 使用别名定义函数指针变量

    op = add;
    printf("Add: %d\n", op(5, 3));

    op = multiply;
    printf("Multiply: %d\n", op(5, 3));

    return 0;
}
```

**解析**：`Operation` 是函数指针 `int (*)(int, int)` 的别名，简化了函数指针的声明。

---

**6. 定义数组类型的别名**
为数组定义一个别名，用于统一管理数据类型。

```c
#include <stdio.h>

// 定义数组类型别名
typedef int Matrix[3][3];

int main() {
    Matrix mat = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

**解析**：`Matrix` 是一个 3x3 整数数组的别名，简化了矩阵类型的声明。

---

**7. 定义位域类型的别名**
为包含位域的结构体定义一个易用的别名。

```c
#include <stdio.h>

// 定义位域类型
typedef struct {
    unsigned int isAvailable : 1;
    unsigned int isReadOnly  : 1;
    unsigned int isHidden    : 1;
} FileAttributes;

int main() {
    FileAttributes file = {1, 0, 1};

    printf("Available: %u, ReadOnly: %u, Hidden: %u\n",
           file.isAvailable, file.isReadOnly, file.isHidden);
    return 0;
}
```

**解析**：`FileAttributes` 是带有位域的结构体的别名，用于简化属性定义。

---

**8. 定义通用数据类型**
为便于跨平台开发，将特定平台的基础类型定义为通用类型。

```c
#include <stdio.h>

// 定义跨平台的整型别名
typedef unsigned long long int U64;

int main() {
    U64 largeNumber = 1234567890123456789ULL;
    printf("Large number: %llu\n", largeNumber);
    return 0;
}
```

**解析**：`U64` 是 `unsigned long long int` 的别名，用于表示 64 位无符号整数。

---

??? info "总结"
    
    `typedef` 的用法非常灵活，常见场景包括：
    1. 简化复杂类型的声明。
    2. 提高代码可读性和语义性。
    3. 增强代码的可维护性和可移植性。

    在不同的场景中，根据需求使用 `typedef` 可以使代码更加清晰简洁。

### 杂项

??? info "ASCII"
        
    | 字符 | 中文名称   | 十进制 | 十六进制 | 八进制 | 二进制       |
    |------|------------|--------|----------|--------|--------------|
    | NUL  | 空字符     | 0      | 0x00     | 000    | 00000000     |
    | SOH  | 标题开始   | 1      | 0x01     | 001    | 00000001     |
    | STX  | 正文开始   | 2      | 0x02     | 002    | 00000010     |
    | ETX  | 正文结束   | 3      | 0x03     | 003    | 00000011     |
    | EOT  | 传输结束   | 4      | 0x04     | 004    | 00000100     |
    | ENQ  | 请求       | 5      | 0x05     | 005    | 00000101     |
    | ACK  | 确认       | 6      | 0x06     | 006    | 00000110     |
    | BEL  | 响铃       | 7      | 0x07     | 007    | 00000111     |
    | BS   | 退格       | 8      | 0x08     | 010    | 00001000     |
    | TAB  | 水平制表符 | 9      | 0x09     | 011    | 00001001     |
    | LF   | 换行       | 10     | 0x0A     | 012    | 00001010     |
    | VT   | 垂直制表符 | 11     | 0x0B     | 013    | 00001011     |
    | FF   | 换页符     | 12     | 0x0C     | 014    | 00001100     |
    | CR   | 回车       | 13     | 0x0D     | 015    | 00001101     |
    | SO   | 禁止切换   | 14     | 0x0E     | 016    | 00001110     |
    | SI   | 允许切换   | 15     | 0x0F     | 017    | 00001111     |
    | SP   | 空格       | 32     | 0x20     | 040    | 00100000     |
    | !    | 感叹号     | 33     | 0x21     | 041    | 00100001     |
    | "    | 双引号     | 34     | 0x22     | 042    | 00100010     |
    | #    | 井号       | 35     | 0x23     | 043    | 00100011     |
    | $    | 美元符     | 36     | 0x24     | 044    | 00100100     |
    | %    | 百分号     | 37     | 0x25     | 045    | 00100101     |
    | &    | 和号/商标符| 38     | 0x26     | 046    | 00100110     |
    | '    | 单引号     | 39     | 0x27     | 047    | 00100111     |
    | (    | 左括号     | 40     | 0x28     | 050    | 00101000     |
    | )    | 右括号     | 41     | 0x29     | 051    | 00101001     |
    | *    | 星号       | 42     | 0x2A     | 052    | 00101010     |
    | +    | 加号       | 43     | 0x2B     | 053    | 00101011     |
    | ,    | 逗号       | 44     | 0x2C     | 054    | 00101100     |
    | -    | 减号       | 45     | 0x2D     | 055    | 00101101     |
    | .    | 句号       | 46     | 0x2E     | 056    | 00101110     |
    | /    | 斜杠       | 47     | 0x2F     | 057    | 00101111     |
    | 0    | 数字0      | 48     | 0x30     | 060    | 00110000     |
    | 1    | 数字1      | 49     | 0x31     | 061    | 00110001     |
    | 2    | 数字2      | 50     | 0x32     | 062    | 00110010     |
    | 3    | 数字3      | 51     | 0x33     | 063    | 00110011     |
    | 4    | 数字4      | 52     | 0x34     | 064    | 00110100     |
    | 5    | 数字5      | 53     | 0x35     | 065    | 00110101     |
    | 6    | 数字6      | 54     | 0x36     | 066    | 00110110     |
    | 7    | 数字7      | 55     | 0x37     | 067    | 00110111     |
    | 8    | 数字8      | 56     | 0x38     | 070    | 00111000     |
    | 9    | 数字9      | 57     | 0x39     | 071    | 00111001     |
    | :    | 冒号       | 58     | 0x3A     | 072    | 00111010     |
    | ;    | 分号       | 59     | 0x3B     | 073    | 00111011     |
    | <    | 小于号     | 60     | 0x3C     | 074    | 00111100     |
    | =    | 等号       | 61     | 0x3D     | 075    | 00111101     |
    | >    | 大于号     | 62     | 0x3E     | 076    | 00111110     |
    | ?    | 问号       | 63     | 0x3F     | 077    | 00111111     |
    | @    | 电子邮件符  | 64     | 0x40     | 100    | 01000000     |
    | A    | 字母A       | 65     | 0x41     | 101    | 01000001     |
    | B    | 字母B       | 66     | 0x42     | 102    | 01000010     |
    | C    | 字母C       | 67     | 0x43     | 103    | 01000011     |
    | D    | 字母D       | 68     | 0x44     | 104    | 01000100     |
    | E    | 字母E       | 69     | 0x45     | 105    | 01000101     |
    | F    | 字母F       | 70     | 0x46     | 106    | 01000110     |
    | G    | 字母G       | 71     | 0x47     | 107    | 01000111     |
    | H    | 字母H       | 72     | 0x48     | 110    | 01001000     |
    | I    | 字母I       | 73     | 0x49     | 111    | 01001001     |
    | J    | 字母J       | 74     | 0x4A     | 112    | 01001010     |
    | K    | 字母K       | 75     | 0x4B     | 113    | 01001011     |
    | L    | 字母L       | 76     | 0x4C     | 114    | 01001100     |
    | M    | 字母M       | 77     | 0x4D     | 115    | 01001101     |
    | N    | 字母N       | 78     | 0x4E     | 116    | 01001110     |
    | O    | 字母O       | 79     | 0x4F     | 117    | 01001111     |
    | P    | 字母P       | 80     | 0x50     | 120    | 01010000     |
    | Q    | 字母Q       | 81     | 0x51     | 121    | 01010001     |
    | R    | 字母R       | 82     | 0x52     | 122    | 01010010     |
    | S    | 字母S       | 83     | 0x53     | 123    | 01010011     |
    | T    | 字母T       | 84     | 0x54     | 124    | 01010100     |
    | U    | 字母U       | 85     | 0x55     | 125    | 01010101     |
    | V    | 字母V       | 86     | 0x56     | 126    | 01010110     |
    | W    | 字母W       | 87     | 0x57     | 127    | 01010111     |
    | X    | 字母X       | 88     | 0x58     | 130    | 01011000     |
    | Y    | 字母Y       | 89     | 0x59     | 131    | 01011001     |
    | Z    | 字母Z       | 90     | 0x5A     | 132    | 01011010     |
    | \[    | 左方括号    | 91     | 0x5B     | 133    | 01011011     |
    | \\   | 反斜杠     | 92     | 0x5C     | 134    | 01011100     |
    | ]    | 右方括号    | 93     | 0x5D     | 135    | 01011101     |
    | ^    | 插入符号    | 94     | 0x5E     | 136    | 01011110     |
    | _    | 下划线      | 95     | 0x5F     | 137    | 01011111     |
    | `    | 反引号      | 96     | 0x60     | 140    | 01100000     |
    | a    | 字母a       | 97     | 0x61     | 141    | 01100001     |
    | b    | 字母b       | 98     | 0x62     | 142    | 01100010     |
    | c    | 字母c       | 99     | 0x63     | 143    | 01100011     |
    | d    | 字母d       | 100    | 0x64     | 144    | 01100100     |
    | e    | 字母e       | 101    | 0x65     | 145    | 01100101     |
    | f    | 字母f       | 102    | 0x66     | 146    | 01100110     |
    | g    | 字母g       | 103    | 0x67     | 147    | 01100111     |
    | h    | 字母h       | 104    | 0x68     | 150    | 01101000     |
    | i    | 字母i       | 105    | 0x69     | 151    | 01101001     |
    | j    | 字母j       | 106    | 0x6A     | 152    | 01101010     |
    | k    | 字母k       | 107    | 0x6B     | 153    | 01101011     |
    | l    | 字母l       | 108    | 0x6C     | 154    | 01101100     |
    | m    | 字母m       | 109    | 0x6D     | 155    | 01101101     |
    | n    | 字母n       | 110    | 0x6E     | 156    | 01101110     |
    | o    | 字母o       | 111    | 0x6F     | 157    | 01101111     |
    | p    | 字母p       | 112    | 0x70     | 160    | 01110000     |
    | q    | 字母q       | 113    | 0x71     | 161    | 01110001     |
    | r    | 字母r       | 114    | 0x72     | 162    | 01110010     |
    | s    | 字母s       | 115    | 0x73     | 163    | 01110011     |
    | t    | 字母t       | 116    | 0x74     | 164    | 01110100     |
    | u    | 字母u       | 117    | 0x75     | 165    | 01110101     |
    | v    | 字母v       | 118    | 0x76     | 166    | 01110110     |
    | w    | 字母w       | 119    | 0x77     | 167    | 01110111     |
    | x    | 字母x       | 120    | 0x78     | 170    | 01111000     |
    | y    | 字母y       | 121    | 0x79     | 171    | 01111001     |
    | z    | 字母z       | 122    | 0x7A     | 172    | 01111010     |
    | {    | 左花括号    | 123    | 0x7B     | 173    | 01111011     |
    | \|    | 竖线       | 124    | 0x7C     | 174    | 01111100     |
    | }    | 右花括号    | 125    | 0x7D     | 175    | 01111101     |
    | ~    | 波浪号      | 126    | 0x7E     | 176    | 01111110     |
    | DEL  | 删除       | 127    | 0x7F     | 177    | 01111111     |


    单个数字0(0)（ASCII的0位）就是'\0'；带引号的字符0('0') 是ASCII的48位
	

## 运算符和表达式

!!! success "牢记几句话"

    表达式的值

**表达式定义：**

运算符 + 运算对象

运算对象：常量、变量和函数等表达式

**分类**

算术表达式、赋值表达式、关系表达式、逻辑表达式、条件表达式和逗号表达式 


### 优先级

最好都加上括号

![alt text](res/images/image_1_1.png)
![alt text](res/images/image-1_1.png)
![alt text](res/images/image-2_1.png)


- 逻辑表达式：C赋值：真1 假0

- 循环判断：非零真

- ++ --
    - 数据的值一样，表达式的值不一样
        - a++：表达式：a+1之前的值，把表达式的值赋给其他
        - ++a：表达式：a+1之后的值，把表达式的值赋给其他

- 只能对变量不能对表达式用

- 左右结合：先从哪边算

- x = y = 3 : 不能在变量定义处用，可以后面用，结合顺序
- 复合赋值：i+=1：更高效

- 逻辑运算短路：
    - ||：前面真后面不算
    - &&：前面假后面不算

- 逗号运算符：值是最后一个子表达式的值

### 位运算
结果是表达式的值

!!! warning "重点"

    计算机中，数字的储存、运算都是以 补码 形式

    `Ctrl F 数字编码`


#### 位逻辑运算

**~按位取反**


**`&` 按位与**

**特点：** 全1才1

**应用：**

1. 让某一位或者某些位为0

    示例：`x & 0xFE`：将最后一位变成0

2. 取一个数中的一段

    示例：`x & 0xFF`：取出最后两个字节中的内容

**`|` 按位或**

**特点：** 有1则1

**应用：**

1. 将某些位变为1：或上那一位为1的数

    示例：`x | 0x01`最右边一位为1

2. 将两个数拼起来

    示例：`0x00FF | 0xFF00`

逻辑运算（`&&`、`||`）相当于将所有非0值都变成1，然后做按位对应运算

**`^` 按位异或**

**特点** ：

- 两个位相同得0，不同得1
- `x ^ y ^ y 变回到 x`

#### 移位运算

箭头朝向即为移动方向

移动的位数为正

`i << j` 对x的所有位左移j个位置，右边填入0

- `x <<= n` 大多数情况下等价于 `x *= $2^n$`
    - 当左移的位数超过位宽（`sizeof(int) * 8`）或有符号数符号位变化时，将导致未定义行为

    - 位移导致舍弃前面的位的情况也不是


`i >> j` 对x的所有位右移j个位置

- 对于unsigned类型，左边填0
- 对于signed类型，符号位保持不变，原来的高位移到地位
- `x >>= n` 大多数情况下等价于 `x /= $2^n$`
   

   直接遗弃超出范围的位

#### 复合位赋值运算

   - `&=`, `|=`, `^=`, `>>=`, `<<=`

   `a &= b` 等价于 `a = a & b`； `a >>= 3` 等价于 `a = a >> 3`

#### 应用

1. 伪转换二进制
    ```c
    include<stdio.h>
    int main()
    {
        int num;
        printf("please enter your number: ");
        scanf("%x", &num);
        unsigned int mask = 1u << 31;
        printf("the binary of your number is: ");
        for(; mask; mask >>= 1){
            printf("%d", num & mask ? 1 : 0);
        }
        printf("\n");
        return 0;
    }
    ```

2. 单片机



#### 位段

**语法：**

```c
struct 位段名 {
    数据类型 成员名 : 位宽;
    数据类型 成员名 : 位宽;
    /*重复上述*/
};
```

- 可以直接用位段的成员名访问


**注意事项：**

- 存储大小与对齐：

    位段的存储大小通常以 int 或 unsigned int 为单位，且会受编译器的内存对齐策略影响。
    
    多个位段成员**可能共享同一个存储单元**（如果其总位宽小于存储单元大小），但如果超出单元大小，会分配下一个单元。

    - 即，所需的位超过一个int时会采用多个int

    - 因此，**访问位段成员的地址的操作是有语法错误的**

- 数据类型的限制：

    位段成员通常只能是 int 或 unsigned int，具体限制依赖于编译器。

- 移植性问题：

    不同编译器和平台对位段的实现（如存储顺序、对齐方式）可能不同，可移植性较差。

-   位宽限制：

    位宽不能超过存储单位的大小。例如，如果 int 是 32 位，位宽不能大于 32。


**示例：**

```c
struct U0 {
    unsigned int leading: 3;
    unsigned int FLAG1: 1;
    unsigned int FLAG2: 1;
    int trailing: 27;
};

void toBinary(int num)
{
    unsigned int mask = 1u << 31;
    for(; mask; mask >>= 1){
        printf("%d", num & mask ? 1 : 0);
    }
}

int main()
{
    struct U0 num1, num2;
    num2.leading = 2;
    num2.FLAG1 = 1;
    num2.FLAG2  =0;
    num2.trailing = 0;
    printf("please enter your number_1: ");
    scanf("%x", &*(int*)&num1);
    printf("the binary of your number_1 is: ");
    toBinary(*(int*)&num1);
    printf("\n");
    printf("the binary of your number_1 is: ");
    toBinary(*(int*)&num2);
    printf("\n");
    return 0;
}
```



**应用场景：** 底层，对硬件的操作

- 嵌入式开发：

    在嵌入式系统中，用位段模拟硬件寄存器的各个位字段。
- 网络协议：

    用位段解析网络协议的标志字段（如 TCP/IP 报头）。
- 标志集合：
    
    用位段压缩存储多个布尔标志，以节省内存。



## 循环和分支
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



## 函数

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


## 数组

### 一维数组

**定义和引用**

- 数组长度必须得是一个数字，不能放变量，即使那个变量有值也不行。
	即：
    ```c
    //situation 1: ERROR
    int n = 5;
    int arr[n];

    //situation 2: ERROR
    int n;
    scanf("%d", &n);
    int arr[n];

    //situation 3: right
    int arr[10];
    ```
- 引用时只能引用单个值，不能一次引用整个数组。引用其实就是*访问和操作*那个东西

- 数组下标越界：不可越界访问；越界访问，随意赋值

- 在内存中的存放
	与前后数据：见下神奇的try：不一定
	内部：index从小到大地址依次增大。从下到上排
	
**初始化**

- C语言规定只能对静态存储的数组初始化，但是课本允许对动态数组+静态数组初始化
	eg：
    ```c
    static int arr[5] = {1, 2, 3, 4, 5}
    ```
- 不初始化：

	静态数组 `static arr[5]`：不初始化则全是0

	动态数组 ` arr[5]`：不初始化则随机数
- 部分初始化：

	初始化前几个，后面没有初始化的元素默认赋值为0

- 全部元素都赋值则可以省略数组长度（不建议）

??? info "神奇的try看着玩玩"

    ```c
    //按照书上的标准，这个定义方式是错的，但是不带了改代码了......
    #include<stdio.h>
    int main()
    {
        int a = 4;
        int arr[a];
        for(int i = 0; i < a; i++){
            arr[i] = i;
        }
        int b = 3;
        printf("%p\n", &a); printf("%p\n", &b); printf("%p\n", &arr);  //打印三个的地址
        printf("%p\n",&arr[0]); printf("%p\n",&arr[3]); printf("%p\n",&arr[4]); printf("%p\n",&arr[7]); //越界访问，且发现&arr[7] ==&a
        printf("%d\n",*&arr[7]);
        printf("%d\n",*&a);  //发现上面那个之后试试a和arr[7]是什么，发现arr[7]被赋值为a的值4
        printf("%d\n",arr[9]); printf("%d\n",arr[10]); //越界访问，随意赋值
        int try[5] = {1, 2};
        printf("%d\n", try[3]); //初始化部分元素，后面的自动赋值0
        return 0;
    }
    /*
    输出：
    a's ptr:0x7ffc2289afe4  b's ptr:0x7ffc2289afe8  arr's ptr0x7ffc2289afd0  arr[0]'s ptr:0x7ffc2289afd0  arr[3]'s ptr:0x7ffc2289afdc 
    arr[4]'s ptr:0x7ffc2289afe0  arr[7]'s ptr:0x7ffc2289afec  
    arr[7]:4  *&a:4
    arr[9]:0  arr[10]:579448784
    try[3]:0
    ```

**示例**

- 用数组计算斐波那契数列，每行打印5个数字，最后一行不满5个也要换行

    ```c
    # include <stdio.h>
    # define MAXN 46                    /* 定义符号常量MAXN */
    int main(void)
    {
        int i, n;
        int fib[MAXN] = {1, 1};         /* 初始化前两个 */
        printf ("Enter n: ");    
        scanf ("%d", &n);
        if(n >= 1 && n <= 46 ){
            for(i = 2; i < n; i++){  
                fib[i] = fib[i - 1] + fib[i - 2];
            }  
            /* 学学人家怎么输出：*/
            for(i = 0; i < n; i++){
                printf("%6d", fib[i]);
                if((i + 1) % 5 == 0){   
                /* 每5个换行：循环变量i+1是5的倍数；注意细节i+1 */
                    printf("\n");
                }  
            }
            if(n % 5 != 0){
            /* 最后不满5个换行：数学转化：最后一行和总数mod5同余 */ 
                printf("\n");
            }
        }else{
            printf("Invalid Value.\n"); 
        }
        return 0;
    }
    ```

- 选择法排序

    ```c
    # include <stdio.h>
    # define MAXN 10                    
    int main(void)
    {
        /* 排序 */
        for(k = 0; k < n-1; k++){
            index = k;                      
            /* 直接用index记录最小值,因为后面交换需要用到index，替换我的min = arr[k] */
            for(i = k + 1; i < n; i++){     
            /* 寻找最小值所在下标 */
                if(a[i] < a[index]){
                    index = i;  
                }
            }
            temp = a[index];
            a[index] = a[k];
            a[k] = temp;
        }
    }
    ```


### 字符串

**定义与初始化**

1. 结束符

    - 有效长度：不包含‘\0' : 计算字符串长度不包括末尾0
    - 结束符：'\0'
        
        `char arr[] = {'h', 'i'}` 不是字符串
        
        `char arr[] = {'h', 'i', '\0'}` or `char arr[] = {'h', 'i', 0}` 是字符串

    - 定义字符串长度 >= 字符串有效长度 + 1

        因为有结束符'\0'

        开大数组：只对前面的赋值，'\0'后面的与字符串无关，字符串到'\0'即结束，故不会影响字符串的处理。

2. 定义方法

- 数组 & 指针：    
`char str[]` or `char* str` 都可以用来定义数组，但是两个不一样。如果要用指针：不能之后再赋值，否则将导致segmentation fault ~
    ```c
    char* str;
    str[0] = 'h';
    str[1] = 'i';
    // 编译器输出:[1]    122420 segmentation fault (core dumped)  ./pta11_7
    char* str2 = "hi";  // OK
    ```


- 放在一维数组中
    ```c
    static char str[6] = {'h', 'a', 'p', 'p', 'y', '\0'}
    ```

- 使用字符串常量
    ```c
    static char str[6] = {"happy"}
    ```
    ```c
    static char str[6] = "happy"
    ```
    - 字符串常量：就是双引号括起来的一个字符串，两种定义方式：`char str[]` or `char* str`

        `char* str` ：只读

        `char str[]`：也是只读，不过在堆栈区会copy一份跟他一样的字符串，这个是可以修改的

        
    - 字符串常量不能修改（但是不能写 `const`）
    - 相同的字符串字面量初始化两不同名字的字符串常量，在一样的地址上（在代码段，是只读的）

    ??? info "字符串常量"

        在C语言中，用数组和指针定义的字符串的区别主要在于它们的存储位置和是否可以修改。

        1. **`char* str1 = "hi";`**
        - 这里 `str1` 是一个指向字符的指针，它指向一个字符串字面量。字符串字面量存储在程序的只读数据段中，这意味着你不能修改 `str1` 指向的内容。尝试修改 `str1` 指向的字符串将导致未定义行为，通常是程序崩溃。
        - 例如，以下代码是不允许的：
            ```c
            str1[0] = 'H'; // 错误：不能修改字符串字面量
            ```

        2. **`char str2[] = "hi";`**
        - 这里 `str2` 是一个字符数组，它在栈上分配了足够的空间来存储字符串 "hi" 及其结尾的空字符 `\0`。`str2` 存储的是数组的第一个元素的地址，这意味着你可以修改 `str2` 中的字符。
        - 例如，以下代码是允许的：
            ```c
            str2[0] = 'H'; // 正确：可以修改数组中的字符
            ```

        - **字符串字面量（`str1`）**：字符串字面量存储在只读数据段中，这是C语言规范的一部分。编译器将字符串字面量放在只读内存区域，以防止程序修改它们。这样做的好处是可以节省内存，因为多个相同的字符串字面量可以共享同一块内存区域。

        - **字符数组（`str2`）**：字符数组是在栈上分配的，它们的生命周期仅限于定义它们的函数或代码块。字符数组的内容可以被修改，因为它们不是存储在只读内存区域。

        在你提供的两个例子中：

        - `char* str1 = "hi";`
        - 这里的 `"hi"` 是一个字符串常量，而 `str1` 是一个指向这个字符串常量的指针。

        - `char str2[] = "hi";`
        - 这里的 `"hi"` 也是一个字符串常量，但 `str2` 是一个字符数组，它在栈上分配了空间，并且包含了字符串常量的内容。尽管 `str2` 本身不是一个字符串常量，它包含了字符串常量的内容，并且这些内容在数组中是可以被修改的。

        为什么 `str2` 不是字符串常量？

        `str2` 不是字符串常量，因为它是一个字符数组，它包含了字符串常量的内容，但存储在栈上，并且其内容是可以被修改的。字符串常量本身是存储在只读内存区域的，而 `str2` 只是包含了这些内容的一个可修改的副本。


**访问**

- 可以用数组，可以用指针，多用指针

- 通常涉及'\0'，用它来控制

**输入输出**

1. 用 `getchar()`，特定字符控制

- 直接读一个字符串

    ```c
    int str[100];
    int k;
    printf("Enter your string:"); //输入提示
    k = 0;
    while((str[k] = getchar()) != '\n'){ //用getchar逐个获取字符，不到'\n'不停
        k++;  //统计字符数量
    }
    str[k] = '\0'; //输入结束符'\0'
    ```

- 先读一个在读一个字符串

    ```C
    scanf("%c", &ch);
    getchar(); // 再getchar消耗掉第一个'\n', 清理缓冲区
    while((str[k] = getchar()) != '\n'){
        k++;
    }
    str[k] = '\0';
    ```


2. 用`scanf()`

- 读取（可能）含有空格的字符串：目的是通过含有空格字符串的测试点

    这种方法不可以用于读取单个字符

    ```C
    scanf("%c", ch);
    getchar(); //何时都要有
    /*如果前面需要先读一个则加上面这部分*/
    scanf("%[^\n]", str);
    ```

- scanf读一个单词：到空格/tab/回车 为止，即见到那三个就停止读入了

    ```c
    char str\[8]; 
    scanf("%s", str); //input: 123 45678
    printf("%s", str);  //output: 123
    ```
- %ns  (n为一个整数)：这次输入最多输入$n$个值，其他的内容停在输入流中，等待下一个scanf，这些scanf依然遵循上一条

    ```c
    char str1[8];
    char str2[8];
    scanf("%3s", str1);
    scanf("%s", str2);
    printf("%s##%s", str1, str2);
    /*
    input 1234 56 --> output 123##4
    input 12 345 --> output 12##345
    input 12 34567789835374 --> *** stack smashing detected ***: terminated \ [1]    25177 IOT instruction (core dumped)  ./wk
    input 123456 --> output 123##456
    ```

**程序参数**

main函数原型：`int main(int argc, char const *argv[])`

1. `int argc`
    - **含义**: 表示命令行参数的数量（argument count）。
    - **值**: 
        - 包括程序名在内的参数总数。
        - 至少为1（即使没有其他参数，程序名也会作为第一个参数）。
   

2. `char const *argv[]`
    - **含义**: 表示命令行参数的数组（argument vector）。
    - **值**:
        - `argv[0]`: 通常是程序的名称（包括路径，取决于操作系统）。
        - `argv[1]` 到 `argv[argc-1]`: 由用户提供的其他命令行参数。
    - **类型**:
        - `const char* argv[]` 是一个字符串指针数组，表示每个参数是一个以空字符 `\0` 结尾的字符串。
    - **用法**:
        - 可以通过索引访问每个参数。
        - 如果需要将字符串参数转换为数字，可以使用函数如 `atoi` 或 `strtol`。

---

**示例**

```c
#include <stdio.h>

int main(int argc, char const *argv[]) {
    printf("Number of arguments: %d\n", argc);
    for (int i = 0; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    return 0;
}
```

**运行**

假设编译生成的可执行文件为 `program`：

```bash
./program arg1 arg2
```

输出：
```
Number of arguments: 3
Argument 0: ./program
Argument 1: arg1
Argument 2: arg2
```


**程序链接：**

![alt text](res/images/image-8_1.png)


### 二维数组

**定义和引用**

- 先行数后列数
- 在内存中的存放
	
    按行 —— 列顺序存放：先0行，再1行……每行按列顺序存放
	
    从上到下：00,01,02,10,11,12,20,21,22……

**初始化**

- 分行赋值

	- 按顺序每行一个括号

	- 部分赋值
		- 括号在：内部也可像一维的一样只赋前面几个的值，空括号代表全0
		- 没or少括号：代表全0
- 顺序赋值
	全写出 or 部分写出，
- 如果完整赋值，可以省略行长度

**矩阵的术语**

```c
for(i = 0; i < n; i++){
	for(j = 0; j < n; j ++){
		// 见下
		}
}
```

- 主对角线：` if(i == j)`
- 上三角： ` if(i <= j)`
- 下三角：` if(i >= j)`
- 副对角：` if(i + j == n - 1)`
- 遍历上三角：`/*j的循环体：*/ j = i; j < n; j++`

## 指针
### 概念与定义

**基本定义**
```c
int i;
int *p = &i;
int* p = &i;
```

理解：有一个整型变量i，p这个变量的值是变量i地址的变量，称p为指针变量
```c
int*p, q;
```
易错：其中，q只是普通int变量；要想定义多个指针变量得分别指定

### 规则

- 输出：得用%p，不能转换成整数再%x（16进制），因为这俩值一不一样取决于编译器、64or32位架构

- 取址符右边只能是变量；`&(++i)`,`&(i + j)`均不合法

### 指针运算
`q - p`：同类型指针相减，表示差的元素个数

`(int)p - (int)q` ：表示差的字节数


`p + 1` / `p-1`:指向下一个存储单元 / 指向上一个存储单元

其他都非法：指针相加、相乘和相除，指针加or减浮点数

可以++，--，+=，-=：注意对应的表达式值&变量值

!!! info
   
    ++i（表达式值+1） 大于 *，i++（表达式值不变） 等于 * 但从右向左结合：意味着俩都先于\*，那么\*其实是对表达式的值取\*

    例如

    ```c
    int main()
    {
    int arr[5] = {1, 2, 3, 4, 5};
    int* p = arr;
    int* q = arr;
    printf("*p++ : %d\n", *p++); //输出*p++ : 1
    printf("p : %p\n", p); //输出p : 0x7ffd12243564
    printf("*++q : %d\n", *++q); //输出*++q : 2
    printf("q : %p\n", q); //输出q : 0x7ffd12243564
    return 0;
    }
    ```


**应用**

\*p++ : 取出原本这个位置的值再把p+1

指针比较
	<, <=, >, >=, =, != 
	比较地址大小
	数组中元素地址 *线性递增*


### 应用
#### 指针与函数

**数组作参数**

函数定义：

- 常用：指针 例如 `*arr` or `arr[]`

- !!! info "其他"

      ```c
      // 1. 不指定大小，单独传递数组名（等价于指针）
      void func(int arr[]);

      // 2. 带有形参大小的语义化声明（仅作提示，与1等价）
      void func(int arr[length]);

      // 3. 传递数组和大小（常用方式）
      void func(int arr[], int size);

      // 4. 使用指针的方式（与1等价）
      void func(int *arr);

      // 5. 传递指针和大小（常用方式，等价于3）
      void func(int *arr, int size);

      // 6. 使用通用指针（适合泛型处理）
      void func(void *arr) {
          int *intArr = (int *)arr; // 需要显式转换
      }
      /*
      1. 参数 void *arr 的含义
      void * 是一种通用指针类型，表示它可以指向任意类型的数据（int、float、char 等）。
      它不能直接用于解引用或进行算术运算，因为编译器不知道它指向的具体数据类型。
      2. 显式类型转换 (int *)arr
      int *intArr = (int *)arr; 将 void * 指针显式转换为 int * 指针。
      这样，编译器就知道 intArr 指向的是一个 int 类型数据，允许后续进行解引用和算术运算。
      */

      // 7. 多维数组，必须指定列数（编译器需要推导数组布局）
      void func(int arr[][N]);  // 适用于静态二维数组
      void func(int arr[M][N]); // 如果固定行数，也可显式指定

      // 8. 多维数组同时传递行数（灵活处理，但需要列数固定）
      void func(int arr[][N], int rows);

      // 9. 动态分配的二维数组（需传递指针数组）
      void func(int **arr, int rows, int cols);

      // 10. const修饰符，保护数组内容（适合只读操作）
      void func(const int arr[], int size);
      void func(const int *arr, int size);

      // 11. restrict关键字（优化提示，避免指针别名）
      void func(int *restrict arr, int size);

      // 12. 使用stddef.h的size_t定义大小（推荐规范写法）
      #include <stddef.h>
      void func(int arr[], size_t size);
      void func(int *arr, size_t size);

      // 13. 使用指针加偏移处理子数组
      void func(int *arr, int startIndex, int length);

      // 14. 同时传递数组和数据类型信息（处理泛型或多类型场景）
      void func(void *arr, size_t elementSize, size_t length);
      ```


函数调用：

- 常用：数组名 `arr` 
- !!! info "其他"

    ```c
    // 1. 直接传递数组名
    int arr[10] = {0};
    func(arr);  // 对应 void func(int arr[]); 或 void func(int *arr);

    // 2. 带有大小参数
    int arr[10] = {0};
    func(arr, 10);  // 对应 void func(int arr[], int size); 或 void func(int *arr, int size);

    // 3. 传递多维数组
    int arr[3][4] = {{0}};
    func(arr);          // 对应 void func(int arr[][4]); 或 void func(int arr[M][4]);
    func(arr, 3);       // 对应 void func(int arr[][4], int rows);

    // 4. 动态分配的一维数组
    int *arr = malloc(10 * sizeof(int));
    func(arr);          // 对应 void func(int *arr);
    func(arr, 10);      // 对应 void func(int *arr, int size);

    // 5. 动态分配的二维数组（指针数组）
    int **arr = malloc(3 * sizeof(int *));
    for (int i = 0; i < 3; i++) arr[i] = malloc(4 * sizeof(int));
    func(arr, 3, 4);    // 对应 void func(int **arr, int rows, int cols);

    // 6. 传递通用指针
    void *arr = malloc(10 * sizeof(int));
    func(arr);          // 对应 void func(void *arr);

    // 7. 传递子数组（指针偏移）
    int arr[10] = {0};
    func(arr + 5, 5);   // 对应 void func(int *arr, int size); 或子数组操作

    // 8. 常量数组传递
    const int arr[10] = {0};
    func(arr, 10);      // 对应 void func(const int arr[], int size);

    // 9. 使用 restrict 修饰的数组
    int arr[10] = {0};
    func(arr, 10);      // 对应 void func(int *restrict arr, int size);

    // 10. 传递多类型数据
    double darr[10] = {0};
    func((void *)darr, sizeof(double), 10);  // 对应 void func(void *arr, size_t elementSize, size_t length);

    // 11. 多维数组的动态分配模拟
    int *arr = malloc(3 * 4 * sizeof(int));
    func(arr, 3, 4);    // 对应 void func(int *arr, int rows, int cols);

    // 12. 直接传递字符数组（字符串）
    char str[] = "hello";
    func(str);          // 对应 void func(char arr[]); 或 void func(char *arr);

    ```


!!! info "经典交换"

    === "1"
 
        ```c
        void swap1 (int x, int y)
        {   
        int t;
        t = x; 
        x = y; 
        y = t;
        } 
        ```
 
    === "2"
 
        ```c
        void swap2 (int *px, int *py)
        {    
        int t;
        t = *px; 
        *px = *py; 
        *py = t;
        } 
        ```
 
    === "3"
 
        ```c
        void swap3 (int *px, int *py)
        {    
        int *pt;
        pt = px; 
        px = py; 
        py = pt;
        } 
        ```
 
不理解就记住只有第二个能成功


??? info "试图理解"

    函数：仍然是参数的传递

    变量作参数：将那个变量的值给到函数的形参，而函数结束后，形参消失，原来的变量仍然是原来的值

    指针做参数：将那个变量的值给到函数的形参，这里，值是地址值，通过地址，可以在函数内部访问外面那个值


##### 函数多返回值 

**原理**

通过传入指针变量，更改对应地址上的值，实现“多返回值”。

**形式**

函数定义：参数例如 `int* p`

函数调用：参数例如 `&num`

例子：
```c
#include<stdio.h>
void minmax(int arr[], int *min, int *max) 
/*
传入参数有讲究：要在定义的函数中对main函数输入/定义的数组进行处理，就必须得传入它，这是函数参数传递的基本内容;
传入指针变量，因为定义的函数内部要对main函数中的min，max变量进行处理，原理同上面;
**核心：要在函数内部对主函数的变量进行操作，则必须得把主函数中的那个变量or其地址传入函数**
*/
{
    int i, j;
    *min = arr[0];
    *max = arr[0];
    for(i = 0; i < 5; i++){
        if(arr[i] >= *max) *max = arr[i];
        if(arr[i] <= *min) *min = arr[i];
    }
    printf("min = %d\n", *min);
    printf("max = %d", *max);
}
int main()
{
    int min; int max;
    int arr[5] = {1,4,7,5,0};
    minmax(arr, &min, &max);
    return 0;
}
```
注：
	函数参数表中的数组是什么？
		答：指针。
		形式：`int a[]` `int *a` 都行

**其他场景**

函数返回状态：return返回运算的状态，指针返回运算结果

#### 数组与指针

!!! success "牢记几句话"

    “数组名是指向数组首元素的指针”

    “同类型指针直接加减是加一个sizeof，实现移位的功能”

##### 几组等价表示
```c
int arr[10];
int* p = arr;
```
那么，
```c
arr , &arr[0] , &*arr , p , &p[0] , &*p
/*注意：
不包含&arr: 他是整个数组的地址；
他的类型：int (*)[10]，即一个指向包含 10 个 int 元素的数组的指针。
&arr + 1 ：加一个数组的大小
arr + 1 ：加一个元素的大小
*/
arr[i] , *(arr + i) , p[i] , *(p + i)
```
不等价：数组名是常量指针，不可赋值运算例如 `arr++`

```c
    int n, i;
    scanf("%d", &n);
    int* arr = (int* )malloc(n * sizeof(int));
    for(i = 0; i < n; i++) scanf("%d", &arr[i]); 
    for (i = 0; i < n; i++) printf("%d#", arr[i]);
    return 0;
```

##### 用法

遍历：`p++`

法一：
```c
int arr[] = {1,2,3,4,5,6,-1};
int* p = arr;
while(*p != -1){
    printf("%d\n", *p++);
}
```
法二：
```c
int arr[] = {1,2,3,4,5,6,-1};
int* p = arr;
for(p = arr; p < arr + n; p++){
   sum += *p;
   }
```



##### 其他

2. 数组变量是const类型指针:常量指针
   即：`int b[]` <=>`int* const b`
   故数组变量不能直接赋值, 即：
```c
int arr1[3] = {1,2,3};
int arr2;
arr2 = arr1;  //ERROR
```

#### const与指针
1. 指针可以是const(指针不可修改：`const` 在 `*` 后面)：这个指针变量的值（地址）不能变了，不能再指向其他变量

    ```c
    int* const q = &i    //q is const
    q++   //ERROR
    i = 20    //OK
    ```

2. 所指的是const(通过指针不可修改：`const` 在 `*` 前面)：表示不能通过这个指针去修改那个变量，但是这个指针和那个变量都不是const都可以修改.用处：大的结构用const结构的指针
    ```c
    const int *p = &i    
    i = 20; i++    //OK
    p++    //OK
    p = &j    //OK
    *p = 30    //ERROR
    ```

3. const数组

    `const int a\[] = {1,2,3,4,5,6}` : 这里的const表示每个元素都是const int

    用处：防止函数对数组修改：`int func(const int arr[], int len)`


### 动态分配内存
C99中的代替方法：可变长度数组
C89中：malloc函数：`#include<stdlib.h>`

**语法**

`int* a = malloc(n * sizeof(int))`

!!! info "malloc() & free()"
	
    函数原型：
		
    `void* malloc(size_t size);`
		
    `void free(void *ptr);`


free() and malloc() is 绑定使用的

参数：内存大小; 

返回值：void* ：一个指针，指向一块内存，单位为字节

之后需要强制类型转换 `(int*)malloc(n * sizeof(int))`

之后将malloc产生的那个指针当数组来用即可

之后要free(a)  //a 是那个指针

必须得是malloc申请来的内存才能被free，其他不行。
好习惯：定义指针先赋值0，最后在free(0)

合理设计程序结构以找到合适地方进行free

如果没有内存了：返回0 orNULL
	
   
**示例**
```c
    int n, i;
    scanf("%d", &n);
    int* arr = (int* )malloc(n * sizeof(int));
    for(i = 0; i < n; i++) scanf("%d", &arr[i]);
    for (i = 0; i < n; i++) printf("%d#", arr[i]);
    free(arr);
    return 0;
```

### 数组与指针

### 指针数组

### 函数指针



`char **a` : a是一个指针，指向另一个指针，那个指针指向一个字符串

`char *a[]` : 

![alt text](res/images/image-6_1.png)


![alt text](res/images/image-15_1.png)

### 杂项
1. NULL与0地址
![alt text](res/images/image-3_1.png)
1. 指针一定要现初始化！
2. 指针类型转换
	- 原理：换一种视角去看那些内存空间
	- 普通指针
		- 事实上，指针的大小都是一样的，可以进行强制类型转换
		- 理解：用内存格格来看：原来这堆格格代表A类型的数据，强制类型转换后代表B类型的数据，按照数据存储的规则进行“翻译”即可
		例子：
??? info "不同类型指针的相互赋值"

    在C语言中，`int` 类型和 `char` 类型的指针可以相互赋值，因为它们通常具有相同的大小（在大多数平台上，`char` 是1字节，`int` 是4字节，但指针的大小是固定的，通常是4字节或8字节，取决于系统架构）。然而，这种赋值通常是不安全的，因为 `int` 和 `char` 指针指向的数据大小不同，解引用这些指针可能会导致未定义行为。

    以下是一些示例和说明：

    示例1：将 `int*` 赋值给 `char*`
    ```c

        int i = 10;
        int* intPtr = &i;
        char* charPtr = (char*)intPtr; // 将int*转换为char*

        // 打印charPtr指向的值
        printf("%d\n", *charPtr); // 打印i的最低字节

    ```
    在这个例子中，我们将 `int` 类型的指针转换为 `char` 类型的指针，并打印出指向的值。这里打印的是 `int` 值的最低字节，因为 `char` 类型是1字节的。

    示例2：将 `char*` 赋值给 `int*`
    ```c

        char chars[4] = {'a', 'b', 'c', 'd'};
        char* charPtr = chars;
        int* intPtr = (int*)charPtr; // 将char*转换为int*

        // 打印intPtr指向的值
        printf("%c\n", *intPtr); // 打印chars数组的前4个字节作为一个整数

    ```
    在这个例子中，我们将 `char` 类型的指针转换为 `int` 类型的指针，并打印出指向的值。这里打印的是 `char` 数组的前4个字节作为一个整数的ASCII值。

    注意事项
    虽然这些赋值在技术上是可能的，但它们可能会导致未定义行为，特别是当你尝试解引用这些指针并访问它们指向的数据时。这是因为 `int` 和 `char` 类型的数据在内存中的表示和对齐方式可能不同。

    - **对齐问题**：许多系统要求 `int` 类型的数据必须在4字节边界上对齐，而 `char` 类型的数据没有这样的要求。将 `char*` 赋值给 `int*` 可能会导致对齐问题，从而导致程序崩溃或数据损坏。
    - **数据解释**：将 `int*` 赋值给 `char*` 或反之，可能会导致数据解释错误，因为 `int` 和 `char` 类型的数据在内存中的布局不同。

    因此，除非完全清楚这样做的后果，否则应避免将 `int` 和 `char` 类型的指针相互赋值。在实际编程中，最好使用相同类型的指针来操作相同类型的数据。



## 编译预处理和宏
### 编译预处理
"\#"：编译预处理指令，这不是C语言，其他语言都有！所以后面不加分号！
例子：`#include<stdio.h>`，`#define PI 3.14`
### 宏
`#define PI 3.14`：定义一个宏（是一个符号），PI为名称，3.14是值


范例程序见下
#### 规范
- 语法：没有等号，没有分号（因为不是一条C语句，其他语言都是用\#编译预处理）
- 值：可以是任何东西，可以空格、标点等：名字再空格后面所有东西
- 其中可以有注释，该注释不会被替换进去
- 没有值的宏：
	
- 位置：
	普通：源代码文件的顶部，或者放在头文件中

??? info "宏的所有定义位置"

    在C或C++中，定义宏（Macro）通常有两种方式：

    1. **预处理器指令**：
    - 宏定义通常写在源代码文件的顶部，或者放在头文件中。它们使用预处理器指令`#define`来定义。
    - 例如，在源文件或头文件中定义一个宏：
        ```c
        #define MY_MACRO 123
        ```
    - 这种方式定义的宏在编译器进行预处理阶段之前就会被处理。

    2. **命令行参数**：
    - 你也可以在编译时通过命令行参数定义宏。这在编译器（如GCC）的命令行参数中使用`-D`选项来实现。
    - 例如，在GCC中定义一个宏：
        ```zsh
        gcc -DMY_MACRO=123 source_file.c
        ```
    - 这种方式定义的宏会在预处理阶段被识别和替换。

    3. **配置文件**：
    - 在某些项目中，宏定义可能被放在一个专门的配置文件中，然后通过包含该文件来使用这些宏定义。

    4. **Makefile**：
    - 在使用Makefile构建项目时，可以在Makefile中定义宏，并通过`-D`选项传递给编译器。

    5. **构建系统**：
    - 在使用现代构建系统（如CMake或Bazel）时，宏定义可以在构建脚本中设置，并在编译时传递给编译器。

    宏定义的位置取决于你的项目结构和个人偏好。通常，如果宏是项目中多个文件共享的，最好将它们定义在头文件中。如果宏是特定于单个文件的，可以直接在该文件中定义。如果宏的值需要在不同的构建之间改变，那么在命令行或构建系统中定义宏可能更灵活。

    当然，让我们更详细地探讨在C/C++项目中定义宏的第2、4和5点：

    2. 命令行参数

    在编译时，你可以通过编译器的命令行参数来定义宏。这通常通过`-D`选项来实现，后面跟着宏的名称和可选的值。这种方法特别适用于：

    - **编译时配置**：根据不同的编译选项启用或禁用特定的代码段。
    - **环境变量**：在不同的开发环境或部署环境中使用不同的宏值。

    **示例**：

    ```bash
    gcc -DDEBUG -DMAX_THREADS=4 -o my_program my_program.c
    ```

    在这个例子中，`DEBUG`和`MAX_THREADS`被定义为宏，`DEBUG`没有指定值（通常用来启用调试代码），而`MAX_THREADS`被赋予了值`4`。

    4. Makefile

    在Makefile中定义宏可以在构建过程中提供灵活性，特别是当你需要根据不同的目标或平台调整编译选项时。你可以在Makefile中设置宏，然后在编译命令中使用这些宏。

    **示例**：

    ```makefile
    CFLAGS += -DUSE_FEATURE -DVERSION='"1.2.3"'

    all:
        gcc $(CFLAGS) -o my_program my_program.c
    ```

    在这个Makefile中，`CFLAGS`变量被用来添加编译器标志，包括定义宏`USE_FEATURE`和`VERSION`。当你运行`make`命令时，这些宏会被传递给GCC编译器。

    5. 构建系统

    现代构建系统如CMake提供了强大的宏和变量管理功能，允许你在构建过程中定义和使用宏。这些宏可以用于控制编译选项、源文件包含、依赖关系等。

    **示例**：

    ```cmake
    # CMakeLists.txt

    # 定义一个宏
    add_definitions(-DENABLE_DEBUG)

    # 设置一个变量，可以作为宏的值
    set(MY_VERSION "1.2.3")

    # 将变量转换为宏
    add_definitions(-DVERSION=${MY_VERSION})

    # 指定C++标准
    set(CMAKE_CXX_STANDARD 11)

    # 构建目标
    add_executable(my_program my_program.cpp)
    ```

    在这个CMake配置文件中，我们使用`add_definitions`来定义宏和添加编译器标志。`set`命令用于设置变量，这些变量可以被用作宏的值。`add_executable`定义了一个可执行文件目标，它将使用前面定义的宏和设置。

    使用构建系统定义宏的好处包括：

    - **跨平台支持**：构建系统通常提供了跨平台的构建配置。
    - **依赖管理**：自动处理源文件和库的依赖关系。
    - **可重用性**：构建脚本可以在多个项目中重用，只需少量修改。

    这些方法提供了在不同层面上控制宏定义的灵活性，使得项目构建更加模块化和可配置。


- 注释：依然作为C语言注释

范例程序：
```c
#include<stdio.h>
#define PI 3.14
#define PI2 2 * PI  //不能写成2PI，因为不是合法的标识符 //一个宏中包含另一个宏
#define FORMAT "%f\n" //宏的值可以是任何东西
#define PRT printf("%f\n", PI); \
			printf(FORMAT, PI2 * 3)  //上面那一行"\"后面不能有任何东西空格、注释啥也不行 FORMAT文本替换，多行，第一行得有分号，因为被替换处需要分号
int main()
{
PRT;
return 0;
}
/*
也可以这样：
#define PRT printf("%f\n", PI); \
			printf(FORMAT, PI2 * 3);
int main()
{
PRT
return 0;
}
注意分号
*/
```

- 原理: **特别简单的原始的文本替换**：编译之前，编译预处理程序（cpp）把文件中所有宏的名字换成值



	shell查看gcc编译预处理过程中的文件
    ```shell
    gcc -g try.c -o try --save-temps
    ```
    ```zsh
    ls -l
    ```
    ```zsh
    tail try.i
    ```

![alt text](res/images/image-11_1.png)

??? info ".c，.i， .o，.s 分别是什么"

    这些文件扩展名代表了C/C++编程和编译过程中的不同阶段和类型的文件：

    1. **.c**：
    - 这是C语言源代码文件的扩展名。它包含了用C语言编写的程序代码。例如，`main.c`就是一个C语言源文件。

    2. **.i**：
    - 这是预处理后的源代码文件的扩展名。当你使用编译器的`-E`选项时，它会生成一个包含了预处理指令（如宏展开、条件编译指令、头文件包含等）后的文件。这个文件通常用于调试预处理阶段。

    3. **.o**：
    - 这是目标文件（Object file）的扩展名。目标文件是编译器编译源代码后生成的中间文件，包含了源代码对应的机器码，但还没有进行链接。目标文件可以被链接器用来生成最终的可执行文件。

    4. **.s**：
    - 这是汇编代码文件的扩展名。当你使用编译器的`-S`选项时，它会生成一个包含了源代码对应的汇编语言代码的文件。这个文件可以被汇编器进一步转换成目标文件。

    5. **.a**：
    - 这是静态库文件的扩展名。静态库是一组目标文件的集合，它们被打包在一起，可以在编译时被链接到程序中。静态库通常用于共享代码或资源，而不需要在运行时动态加载。

    6. **.so**：
    - 这是共享库文件（在Linux系统中）的扩展名。共享库是一种特殊的库，它们在运行时被动态加载和链接到程序中。这允许多个程序共享同一份库代码，节省内存并减少磁盘空间。

    7. **.exe**：
    - 这是可执行文件的扩展名，在Windows系统中使用。可执行文件是编译后的程序，可以直接在操作系统中运行。

    8. **a.out**：
    - 这是一个传统的可执行文件的名称，在Unix和类Unix系统中使用。在早期的Unix系统中，编译器默认生成的可执行文件被命名为`a.out`。尽管现代编译器允许你指定可执行文件的名称，但`a.out`仍然被用作默认名称，尤其是在某些特定的编译环境或教学示例中。

    这些文件类型和扩展名是C/C++编程和编译过程中的基本组成部分，了解它们有助于更好地理解程序的构建和运行过程。

预定义宏：
即C帮我定义好了，我直接使用

`__LINE__`， `__FILE__`， `__DATE__`， `__TIME__`， `__STDC__`

示例：

```c
printf("%s:%d\n", __FILE__, __LINE__);
printf("%s, %s\n", __DATE__, __TIME__);
```

#### 用法

##### 带参数的宏

**语法**

```c
#define cube(x) ((x) * (x) * (x)) //后面会被替换
```

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

```c
#define PRINT(msg) printf(msg)
//使用：
printf("hello world");
```

**注意**：

- 定义语句括号内不需要参数类型
- 可以多个参数
- 可以嵌套组合使用



调用，与C函数调用相同。



**易错点**：“未理解原始文本替换”

所以：一切都要右括号：整个值要有；参数出现的每个地方都要有。

示例：
```c
#define f(x) ((x) * 5)  //对
#define f(x) (x * 5)  //错
#define f(x) (x) * 5  //错
```
杂项：

- 非常常见
- 用`#` `##`两个运算符实现复杂功能，例如产生函数
- 部分宏会被`inline`函数代替
- 西方程序员比中国人爱用
- 其他编译预处理指令：
    - 条件编译
    - error


## 可变数组

功能：可增大、可获取大小、可访问

[查看原码](https://github.com/Elliottt001/Code/tree/main/C/Practice/changeable-array)

设计思想：

- 自定义类型一般不定义指针
- free 的对象是Array结构里面的数组

## 链表

可变数组的缺陷：内存受限场景下，反复重新申请大内存会有内存不够的情况

方法：申请block大小的内存，再次申请一个，将他俩链起来（告诉编译器下一块内存在哪里）

![alt text](res/images/image-14_1.png)

结点包含：数据、指向下一个的指针

![alt text](res/images/image-16_1.png)

![alt text](res/images/image-17_1.png)

**语法：**

```c
typedef struct _node {
    int value;
    struct _node* next;
} Node;
```

=== "python链表"

    在 Python 中，链表可以用类和对象来实现，因为 Python 本身没有像 C++ 或 Java 那样的内置链表数据结构。链表有两种主要类型：**单向链表**和**双向链表**。以下是关于它们的实现和操作的详细说明。

    ---

    **单向链表实现**

    **定义单向链表：**

    ```python
    class Node:
        def __init__(self, data):
            self.data = data  # 存储节点数据
            self.next = None  # 指向下一个节点

    class LinkedList:
        def __init__(self):
            self.head = None  # 初始化头节点为空

        # 向链表末尾添加节点
        def append(self, data):
            new_node = Node(data)
            if not self.head:  # 如果链表为空
                self.head = new_node
                return
            current = self.head
            while current.next:  # 找到最后一个节点
                current = current.next
            current.next = new_node

        # 打印链表
        def print_list(self):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

        # 删除值等于 data 的节点
        def delete(self, data):
            current = self.head

            # 如果要删除的是头节点
            if current and current.data == data:
                self.head = current.next
                current = None
                return

            # 找到要删除的节点
            prev = None
            while current and current.data != data:
                prev = current
                current = current.next

            if not current:  # 未找到节点
                print("Node not found")
                return

            prev.next = current.next
            current = None
    ```

    **使用示例：**

    ```python
    # 创建链表
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    # 打印链表
    ll.print_list()  # 输出: 1 -> 2 -> 3 -> None

    # 删除节点
    ll.delete(2)
    ll.print_list()  # 输出: 1 -> 3 -> None
    ```

    ---

    **双向链表实现**

    **定义双向链表：**

    ```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None  # 指向下一个节点
            self.prev = None  # 指向前一个节点

    class DoublyLinkedList:
        def __init__(self):
            self.head = None  # 初始化头节点为空

        # 在链表末尾添加节点
        def append(self, data):
            new_node = Node(data)
            if not self.head:  # 如果链表为空
                self.head = new_node
                return
            current = self.head
            while current.next:  # 找到最后一个节点
                current = current.next
            current.next = new_node
            new_node.prev = current

        # 从链表头部打印链表
        def print_list(self):
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

        # 从链表尾部打印链表（反向）
        def print_reverse(self):
            current = self.head
            while current and current.next:
                current = current.next
            while current:
                print(current.data, end=" <-> ")
                current = current.prev
            print("None")

        # 删除值等于 data 的节点
        def delete(self, data):
            current = self.head

            # 如果要删除的是头节点
            if current and current.data == data:
                self.head = current.next
                if self.head:
                    self.head.prev = None
                current = None
                return

            # 找到要删除的节点
            while current and current.data != data:
                current = current.next

            if not current:  # 未找到节点
                print("Node not found")
                return

            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

            current = None
    ```

    **使用示例：**

    ```python
    # 创建双向链表
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    # 打印链表
    dll.print_list()  # 输出: 1 <-> 2 <-> 3 <-> None

    # 反向打印链表
    dll.print_reverse()  # 输出: 3 <-> 2 <-> 1 <-> None

    # 删除节点
    dll.delete(2)
    dll.print_list()  # 输出: 1 <-> 3 <-> None
    ```

    ---

    **链表操作总结**

    - **插入操作：** 可以在头部、尾部或中间插入节点。
    - **删除操作：** 需要更新相邻节点的指针。
    - **遍历操作：** 从头节点开始，依次访问每个节点。

    链表的实现非常灵活，适合存储动态数据结构，适用于需要频繁插入和删除操作的场景。

=== "C链表"

    在 C 中，链表可以用结构体和指针来实现。以下是单向链表和双向链表的实现和常用操作的详细说明。

    ---

    **单向链表**

    **定义单向链表节点**

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    // 定义节点结构
    struct Node {
        int data;              // 节点数据
        struct Node* next;     // 指向下一个节点的指针
    };

    // 创建新节点
    struct Node* createNode(int data) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->next = NULL;
        return newNode;
    }
    ```

    **单向链表操作**

    1. **插入节点到链表末尾**

    ```c
    void append(struct Node** head, int data) {
        struct Node* newNode = createNode(data);
        if (*head == NULL) {  // 如果链表为空
            *head = newNode;
            return;
        }
        struct Node* temp = *head;
        while (temp->next != NULL) {  // 遍历到链表末尾
            temp = temp->next;
        }
        temp->next = newNode;
    }
    ```

    !!! success "append函数超详解"

        **函数原型**

        ```c
        void append(List* plist, int num);
        ```

        **参数说明**：

        1. **`plist`**：指向链表结构的指针，用于表示要操作的链表。
        - `List` 是一个结构体，包含指向链表头节点的指针 `head`。
        - 通过传入 `List*`，函数能够直接操作链表的内容（比如添加节点）。
        2. **`num`**：要添加到链表的新节点的值。

        ---

        **函数实现**

        ```c
        void append(List* plist, int num)
        {
            // 1. 创建一个新的节点并初始化
            Node* p = (Node*)malloc(sizeof(Node)); // 为新节点分配内存
            p->value = num; // 设置新节点的值
            p->next = NULL; // 新节点的 next 指针初始化为 NULL

            // 2. 找到链表的最后一个节点
            Node* last = plist->head; // 从链表头开始遍历
            if (last) {
                // 如果链表不为空，找到最后一个节点
                while (last->next) {
                    last = last->next; // 循环向下，直到最后一个节点
                }
                // 3. 将新节点连接到最后一个节点
                last->next = p;
            } else {
                // 如果链表为空，将新节点作为头节点
                plist->head = p;
            }
        }
        ```

        ---

        **详细分步解析**

        **1. 创建新节点**

        ```c
        Node* p = (Node*)malloc(sizeof(Node));
        p->value = num;
        p->next = NULL;
        ```

        - **动态内存分配**：
        - 使用 `malloc` 分配一段内存，用于存储新节点。
        - 返回值是 `void*`，需要强制类型转换为 `Node*`。
        - **初始化新节点**：
        - `p->value = num`：将新节点的 `value` 字段设置为传入的值 `num`。
        - `p->next = NULL`：将新节点的 `next` 指针设置为 `NULL`，表示它暂时是链表的最后一个节点。

        ---

        **2. 查找链表的最后一个节点**

        ```c
        Node* last = plist->head;
        if (last) {
            while (last->next) {
                last = last->next;
            }
        }
        ```

        - **指针 `last` 的作用**：
        - `last` 是一个临时指针，用于遍历链表，找到当前链表的最后一个节点。
        - 初始时，`last` 指向链表的头节点（`plist->head`）。
        - **判断链表是否为空**：
        - 如果 `plist->head` 为 `NULL`，说明链表为空，直接跳到 `else` 部分。
        - 如果 `plist->head` 不为 `NULL`，说明链表中至少有一个节点，进入 `while` 循环。
        - **`while` 循环**：
        - `last->next` 表示当前节点的下一节点是否存在。
        - 循环条件 `last->next` 为真时，将指针 `last` 移动到下一个节点。

        ---

        **3. 连接新节点**

        ```c
        last->next = p;
        ```

        - 当找到链表的最后一个节点时，将其 `next` 指针指向新创建的节点 `p`，这样 `p` 成为新的最后一个节点。

        ---

        **4. 处理空链表**

        ```c
        else {
            plist->head = p;
        }
        ```

        - 如果链表为空（`plist->head == NULL`），新节点 `p` 直接成为链表的头节点。

        ---

        **函数工作原理举例**

        假设链表初始状态为空，依次调用 `append` 函数，插入 3 个值：`10`、`20`、`30`。

        **初始状态**

        - 链表为空：`plist->head = NULL`

        **第一步**：添加 `10`
        
        1. 创建新节点 `p`，值为 `10`，`p->next = NULL`。
        2. 因为链表为空（`plist->head == NULL`），将 `plist->head` 指向 `p`。
        - 链表状态：`10 -> NULL`

        **第二步**：添加 `20`
        
        1. 创建新节点 `p`，值为 `20`，`p->next = NULL`。
        2. 遍历链表，找到最后一个节点（`10`）。
        3. 将最后一个节点（`10`）的 `next` 指针指向新节点 `p`。
        - 链表状态：`10 -> 20 -> NULL`

        **第三步**：添加 `30`
        
        1. 创建新节点 `p`，值为 `30`，`p->next = NULL`。
        2. 遍历链表，找到最后一个节点（`20`）。
        3. 将最后一个节点（`20`）的 `next` 指针指向新节点 `p`。
        - 链表状态：`10 -> 20 -> 30 -> NULL`

        ---

        **总结**
        
        `append` 函数的核心功能是向链表末尾添加一个新节点。主要步骤：
        
        1. 创建新节点，动态分配内存并初始化。
        2. 判断链表是否为空：
        - 如果为空，将新节点设为头节点。
        - 如果不为空，遍历链表找到最后一个节点，并将新节点连接到最后。


    2. **打印链表**

    ```c
    void printList(struct Node* head) {
        struct Node* temp = head;
        while (temp != NULL) {
            printf("%d -> ", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
    ```

    3. **删除节点**

    ```c
    void deleteNode(struct Node** head, int key) {
        struct Node* temp = *head;
        struct Node* prev = NULL;

        // 如果头节点需要删除
        if (temp != NULL && temp->data == key) {
            *head = temp->next;
            free(temp);
            return;
        }

        // 查找要删除的节点
        while (temp != NULL && temp->data != key) {
            prev = temp;
            temp = temp->next;
        }

        // 如果未找到节点
        if (temp == NULL) {
            printf("Node with data %d not found.\n", key);
            return;
        }

        prev->next = temp->next;  // 删除节点
        free(temp);
    }
    ```

    **单向链表完整示例**

    ```c
    int main() {
        struct Node* head = NULL;

        // 插入节点
        append(&head, 10);
        append(&head, 20);
        append(&head, 30);

        // 打印链表
        printf("Linked List: ");
        printList(head);

        // 删除节点
        deleteNode(&head, 20);
        printf("After Deletion: ");
        printList(head);

        return 0;
    }
    ```

    ---

    **双向链表**

    **定义双向链表节点**

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    // 定义双向链表节点结构
    struct Node {
        int data;              // 节点数据
        struct Node* next;     // 指向下一个节点
        struct Node* prev;     // 指向前一个节点
    };

    // 创建新节点
    struct Node* createNode(int data) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->next = NULL;
        newNode->prev = NULL;
        return newNode;
    }
    ```

    **双向链表操作**

    1. **插入节点到链表末尾**

    ```c
    void append(struct Node** head, int data) {
        struct Node* newNode = createNode(data);
        if (*head == NULL) {  // 如果链表为空
            *head = newNode;
            return;
        }
        struct Node* temp = *head;
        while (temp->next != NULL) {  // 遍历到链表末尾
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }
    ```

    2. **从头部打印链表**

    ```c
    void printList(struct Node* head) {
        struct Node* temp = head;
        while (temp != NULL) {
            printf("%d <-> ", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
    ```

    3. **从尾部打印链表**

    ```c
    void printReverse(struct Node* head) {
        struct Node* temp = head;
        if (temp == NULL) return;

        // 遍历到链表末尾
        while (temp->next != NULL) {
            temp = temp->next;
        }

        // 从尾部向头部打印
        while (temp != NULL) {
            printf("%d <-> ", temp->data);
            temp = temp->prev;
        }
        printf("NULL\n");
    }
    ```

    4. **删除节点**

    ```c
    void deleteNode(struct Node** head, int key) {
        struct Node* temp = *head;

        // 找到要删除的节点
        while (temp != NULL && temp->data != key) {
            temp = temp->next;
        }

        if (temp == NULL) {  // 未找到节点
            printf("Node with data %d not found.\n", key);
            return;
        }

        if (temp->prev != NULL) {
            temp->prev->next = temp->next;
        } else {  // 删除头节点
            *head = temp->next;
        }

        if (temp->next != NULL) {
            temp->next->prev = temp->prev;
        }

        free(temp);
    }
    ```

    **双向链表完整示例**

    ```c
    int main() {
        struct Node* head = NULL;

        // 插入节点
        append(&head, 10);
        append(&head, 20);
        append(&head, 30);

        // 正序打印链表
        printf("Doubly Linked List: ");
        printList(head);

        // 倒序打印链表
        printf("Reverse List: ");
        printReverse(head);

        // 删除节点
        deleteNode(&head, 20);
        printf("After Deletion: ");
        printList(head);

        return 0;
    }
    ```

    ---

    **总结**

    - 单向链表适合基本操作，结构简单。
    - 双向链表可以在两个方向上遍历，适合需要频繁前后移动的操作。
    - 操作中要特别注意指针的正确操作，避免内存泄漏或段错误 (`segmentation fault`)。


=== "C++链表"

    在 C++ 中，可以使用类和指针来实现链表结构。以下是单向链表和双向链表的实现及常用操作的详细说明。

    ---

    **单向链表**

    **定义单向链表节点**

    ```cpp
    #include <iostream>
    using namespace std;

    // 定义单向链表节点
    class Node {
    public:
        int data;        // 节点数据
        Node* next;      // 指向下一个节点的指针

        Node(int val) : data(val), next(nullptr) {}  // 构造函数
    };
    ```

    **定义单向链表类**

    ```cpp
    class LinkedList {
    private:
        Node* head;  // 指向头节点的指针

    public:
        LinkedList() : head(nullptr) {}  // 构造函数

        // 添加节点到链表末尾
        void append(int data) {
            Node* newNode = new Node(data);
            if (head == nullptr) {
                head = newNode;
                return;
            }
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }

        // 打印链表
        void printList() {
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->data << " -> ";
                temp = temp->next;
            }
            cout << "NULL" << endl;
        }

        // 删除指定值的节点
        void deleteNode(int key) {
            Node* temp = head;
            Node* prev = nullptr;

            // 删除头节点
            if (temp != nullptr && temp->data == key) {
                head = temp->next;
                delete temp;
                return;
            }

            // 查找要删除的节点
            while (temp != nullptr && temp->data != key) {
                prev = temp;
                temp = temp->next;
            }

            // 未找到节点
            if (temp == nullptr) {
                cout << "Node with value " << key << " not found." << endl;
                return;
            }

            // 删除节点
            prev->next = temp->next;
            delete temp;
        }

        // 析构函数：释放所有节点
        ~LinkedList() {
            Node* temp;
            while (head != nullptr) {
                temp = head;
                head = head->next;
                delete temp;
            }
        }
    };
    ```

    **单向链表完整示例**

    ```cpp
    int main() {
        LinkedList list;

        // 添加节点
        list.append(10);
        list.append(20);
        list.append(30);

        // 打印链表
        cout << "Linked List: ";
        list.printList();

        // 删除节点
        list.deleteNode(20);
        cout << "After Deletion: ";
        list.printList();

        return 0;
    }
    ```

    ---

    **双向链表**

    **定义双向链表节点**

    ```cpp
    class Node {
    public:
        int data;        // 节点数据
        Node* next;      // 指向下一个节点
        Node* prev;      // 指向前一个节点

        Node(int val) : data(val), next(nullptr), prev(nullptr) {}  // 构造函数
    };
    ```

    **定义双向链表类**

    ```cpp
    class DoublyLinkedList {
    private:
        Node* head;  // 指向头节点

    public:
        DoublyLinkedList() : head(nullptr) {}  // 构造函数

        // 添加节点到链表末尾
        void append(int data) {
            Node* newNode = new Node(data);
            if (head == nullptr) {
                head = newNode;
                return;
            }
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
            newNode->prev = temp;
        }

        // 从头部打印链表
        void printList() {
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->data << " <-> ";
                temp = temp->next;
            }
            cout << "NULL" << endl;
        }

        // 从尾部打印链表（反向）
        void printReverse() {
            Node* temp = head;
            if (temp == nullptr) return;

            // 找到尾节点
            while (temp->next != nullptr) {
                temp = temp->next;
            }

            // 从尾节点向头打印
            while (temp != nullptr) {
                cout << temp->data << " <-> ";
                temp = temp->prev;
            }
            cout << "NULL" << endl;
        }

        // 删除指定值的节点
        void deleteNode(int key) {
            Node* temp = head;

            // 找到要删除的节点
            while (temp != nullptr && temp->data != key) {
                temp = temp->next;
            }

            // 未找到节点
            if (temp == nullptr) {
                cout << "Node with value " << key << " not found." << endl;
                return;
            }

            // 更新前后节点的指针
            if (temp->prev != nullptr) {
                temp->prev->next = temp->next;
            } else {  // 删除头节点
                head = temp->next;
            }

            if (temp->next != nullptr) {
                temp->next->prev = temp->prev;
            }

            delete temp;
        }

        // 析构函数：释放所有节点
        ~DoublyLinkedList() {
            Node* temp;
            while (head != nullptr) {
                temp = head;
                head = head->next;
                delete temp;
            }
        }
    };
    ```

    **双向链表完整示例**

    ```cpp
    int main() {
        DoublyLinkedList list;

        // 添加节点
        list.append(10);
        list.append(20);
        list.append(30);

        // 正序打印链表
        cout << "Doubly Linked List: ";
        list.printList();

        // 反序打印链表
        cout << "Reverse List: ";
        list.printReverse();

        // 删除节点
        list.deleteNode(20);
        cout << "After Deletion: ";
        list.printList();

        return 0;
    }
    ```

    ---

    **总结**

    单向链表优点

    - 结构简单，占用内存少。
    - 适合只需要从头到尾遍历的场景。

    双向链表优点

    - 支持从头部和尾部两个方向遍历，操作更加灵活。
    - 适合需要频繁插入、删除以及双向遍历的场景。

    链表的实现中要特别注意内存管理，防止内存泄漏。在 C++ 中，可以使用智能指针（如 `std::unique_ptr` 或 `std::shared_ptr`）来简化内存管理工作。





























## 大程序结构

[浅谈VScode中多文件项目的编译
-博客园](https://www.cnblogs.com/Roboduster/p/15315817.html)

将不同功能（函数）放到很多个.c文件中

文件结构与内容：

main.c，其中 `#include"func.h"`

func.h，其中写func函数的原型声明

- 作用：“合同”，里面是func的原型

func.c，其中 `#include"func.h"`，下面写函数的body

### 头文件

示例：
```c
// hello.h
#ifndef HELLO_H
#define HELLO_H
​
#include <stdio.h>
​
extern void greet(const char *name);
​
#endif // HELLO_H
​
// hello.c
#include "hello.h"
​
void greet(const char *name)
{
    printf("Hello, %s!\n", name);
}
​
// main.c
#include "hello.h"
​
int main(){
    greet("各位大佬!");
}
```

**知识**

把*函数原型*放到一个头文件(以.h结尾)中，在需要调用这个函数的源代码文件(.c文件)中#include这个头文件，就能让编译器在编译的时候知道函数的原刑

`#include`:编译预处理指令，和宏一样，在编译之前就处理了

它把include后面那个文件的全部文本内容 原封不动地插入到include语句所在的地方，所以也不是一定要在.c文件的最前面#include

**注意：** 在定义和使用这个函数的地方都要
`include"func.h"`；一般情况：任何.c都有同名的.h，把所有*对外公开的*函数原型和全局变量的声明都放进去。

**补充**：不对外公开：加 `static` 函数前面加它代表只有他在的这个.c文件（编译单元）可以用它，其他不行；全局变量前面加它代表他只是这个.c文件（编译单元）中可以使用的全局变量。

![alt text](res/images/image-9_1.png)

**语法**：

- `""` or `<>`
    - `""` 先在当前目录下找这个文件，找不到再去别的目录下找，一般用于自己写的

    - `<>` 不会在当前目录下找，一般用于系统的标准库头文件(在/usr/include目录下，另外有c++目录里面是cpp的头文件)

    命令行可以`more stdio.h` 一点点看，`code stdio.h` 的效果和`ctrl + click` 相同hhh

- 标准头文件结构

    ```c
    #ifndef __FILENAME_H__
    #define __FILENAME_H__

    //代码块

    #endif
    ```


**理解**：include不是在引入库，只是文本替换

### 声明

对于在一个.c文件（不是main.c，假设是func.c）定义的全局变量，要想在main.c访问它，需要在对应的func.h声明（声明变量）；

**语法**:

func.h： `extern int VARIBLENAME` 

func.c：`int VARIBLENAME = 12` (在全局变量的位置，最外面)



## 文件

### 格式化输入输出

`printf : %[flags][width][.prec][hlL]type`

| **部分**             | **说明**                                                                                   | **示例代码**                                                                                             | **输出**              |
|-----------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------|
| **`%`**              | 格式说明符的起始标志。                                                                    | `printf("Value: %d\n", 42);`                                                                              | `Value: 42`          |
| **`[flags]`**         | 可选标志，用于修改输出格式：                                                              |                                                                                                          |                       |
| - `-`                | 左对齐输出（默认右对齐）。                                                                | `printf("\|%-10d\|\n", 42);`                                                                               | `\|42        \|`        |
| - `+`                | 输出符号（正数带`+`，负数带`-`）。                                                        | `printf("%+d\n", 42); printf("%+d\n", -42);`                                                             | `+42` `-42`          |
| - `空格`             | 正数前加空格，负数前加`-`。                                                               | `printf("\|% d\|\n", 42); printf("\|% d\|\n", -42);`                                                         | `\| 42\|` `\|-42\|`       |
| - `0`                | 用`0`填充宽度（在数字前有效）。                                                           | `printf("%05d\n", 42);`                                                                                | `00042`            |
| - `#`                | 启用格式依赖的功能（例如八进制/十六进制前缀）。                                           | `printf("%#x\n", 42); printf("%#o\n", 42);`                                                              | `0x2a` `052`         |
| **`[width]`**         | 最小输出宽度（整数）。输出不足时用空格填充，超过时无影响。                               | `printf("\|%10d\|\n", 42); printf("\|%3d\|\n", 12345);`                                                      | `\|        42\|` `\|12345\|` |
| - `*`                | 下一个参数是字符占位数（那个参数替换`*`）                                                          | `printf("%0*d\n", 7, 42);`                                                                                | `0000042`            |
| **`[.prec]`**         | 精度控制：                                                                                 |                                                                                                          |                       |
| - `.`                | 指定浮点数的小数位数或字符串最大字符数。                                                  | `printf("%.2f\n", 3.14159); printf("%.3s\n", "Hello");`                                                  | `3.14` `Hel`         |
| - 整数部分           | 对整数无影响（不推荐使用）。                                                              | `printf("%.5d\n", 42);`                                                                                  | `00042`              |
| - `.*`                | 下一个参数是小数点后的位数                                                           | `printf("%*lf\n", 5, 0.5);`                                                                                | `0.50000`            |
| **`[hIL]`**           | 长度修饰符：控制输入数据的大小。                                                          |                                                                                                          |                       |
| - `h`                | 短整数类型（`short`）。                                                                  | `short s = 42; printf("%hd\n", s);`                                                                      | `42`                 |
| - `l`                | 长整数类型（`long`）。                                                                   | `long l = 123456789; printf("%ld\n", l);`                                                                | `123456789`          |
| - `ll`               | 长长整数类型（`long long`）。                                                            | `long long ll = 123456789012345; printf("%lld\n", ll);`                                                  | `123456789012345`    |
| - `L`                | 长浮点类型（`long double`）。                                                            | `long double ld = 3.141592653589; printf("%Lf\n", ld);`                                                  | `3.141593`           |
| **`type`**            | 数据类型，定义如何解释数据并输出：                                                        |                                                                                                          |                       |
| - `d`/`i`            | 带符号整数（十进制）。                                                                   | `printf("%d\n", 42); printf("%d\n", -42);`                                                               | `42` `-42`           |
| - `u`                | 无符号整数（十进制）。                                                                   | `printf("%u\n", 42);`                                                                                    | `42`                 |
| - `f`                | 浮点数（小数形式）。                                                                     | `printf("%.2f\n", 3.14159);`                                                                             | `3.14`               |
| - `x`/`X`            | 无符号整数（十六进制）。                                                                 | `printf("%x\n", 42); printf("%X\n", 42);`                                                                | `2a` `2A`            |
| - `o`                | 无符号整数（八进制）。                                                                   | `printf("%o\n", 42);`                                                                                    | `52`                 |
| - `c`                | 单个字符。                                                                               | `printf("%c\n", 'A');
| - `s`                | 字符串。                                                                                 | `printf("%s\n", "Hello");`                                                                               | `Hello`              |
| - `p`                | 指针地址。                                                                               | `printf("%p\n", (void*)&main);`                                                                          | 类似于 `0x7ffc...`   |
| - `%`                | 输出百分号本身。                                                                         | `printf("100%% Complete\n");`                                                                            | `100% Complete`      |
| - `e`                | 科学计数法表示的浮点数（小写）。                                                          | `printf("%e\n", 12345.6789);`                                                                             | `1.234568e+04`       |
| - `E`                | 科学计数法表示的浮点数（大写）。                                                          | `printf("%E\n", 12345.6789);`                                                                             | `1.234568E+04`       |
| - `n`                | 将到目前为止读入/写出的字符数存储到指定的变量中。                                              | `int n; printf("Hello%n\n", &n); printf("Chars: %d\n", n);`                                               | `Hello` 和 `Chars: 5` |
| - `a`                | 十六进制表示的浮点数（小写），符合 C99 标准。                                              | `printf("%a\n", 123.45);`                                                                                 | `0x1.edp+06`         |
| - `A`                | 十六进制表示的浮点数（大写），符合 C99 标准。                                              | `printf("%A\n", 123.45);`                                                                                 | `0X1.EDP+06`         |
| - `G`                | 根据值自动选择`%E`或`%f`格式（大写）。                                                    | `printf("%G\n", 12345.6789);`                                                                             | `12345.7`            |
| - `g`                | 根据值自动选择`%e`或`%f`格式（小写）。                                                    | `printf("%g\n", 12345.6789);`                                                                             | `12345.7`            |

```c
printf("%9.3f\n", 123.0)
//连带小数点前后总共占9位
```

![alt text](res/images/image-12_1.png)

**printf scanf的返回值**

- scanf：读入的字符数
- printf：输出的字符数

大型程序中，应该判断每次调用scanf和printf的返回值，从而了解程序运行中是否存在问题。


### 基本概念

在C语言中，文件操作是一种将程序数据持久化到存储设备（如硬盘）中的方式，可以读取和写入数据到文件中。文件操作的核心思想是通过**文件指针**来访问文件，文件指针是一个连接程序和文件的桥梁。

---

#### 文件与流
- **文件（File）**  
  文件是存储在存储设备上的数据集合，可以是文本文件（如 `.txt`）或二进制文件（如 `.bin`）。C语言通过文件操作函数访问文件内容。

- **流（Stream）**  
  流是文件与程序之间数据传输的抽象。通过流，数据可以从程序写入文件，或从文件读取到程序。

---

#### 文件指针
- 类型为 `FILE*` 的指针，定义在 `stdio.h` 中，用于标识程序与文件之间的连接。

使用：

1. 使用 `fopen` 打开文件并获取指针。
2. 操作文件（读/写/定位）。
3. 使用 `fclose` 关闭文件并释放资源。



**文件指针会随着在文件中写入内容而移动**。

- **`fprintf`、`fwrite` 等写操作**：文件指针会移动到写入数据的末尾。
- **`fseek` 和 `ftell`**：可以用于手动调整和检查文件指针的位置。

---

### 示例代码
以下代码演示了文件指针如何随着写入内容而移动：

```c
#include <stdio.h>

int main() {
    FILE* fp = fopen("test.txt", "w+");  // 读写模式
    if (fp == NULL) {
        perror("Failed to open file");
        return 1;
    }

    // 初始文件指针位置
    printf("Initial position: %ld\n", ftell(fp));  // 输出 0

    // 写入内容
    fprintf(fp, "Hello, ");
    printf("After first write: %ld\n", ftell(fp)); // 输出 7（"Hello, " 有 7 个字符）

    // 写入更多内容
    fprintf(fp, "world!");
    printf("After second write: %ld\n", ftell(fp)); // 输出 13（"Hello, world!" 有 13 个字符）

    // 关闭文件
    fclose(fp);
    return 0;
}
```

**输出示例：**
```
Initial position: 0
After first write: 7
After second write: 13
```

---

文件指针移动规则

1. **写入操作后**：
   - 文件指针移动到写入内容的末尾。
   - 例如，写入 `"Hello"` 后，文件指针移动到 `5` 处（字符数为 `5`）。

2. **读操作后**：
   - 文件指针移动到读取内容的末尾。

3. **手动移动指针**：
   - 可以通过 `fseek` 或 `rewind` 函数调整指针位置。例如：
     ```c
     fseek(fp, 0, SEEK_SET);  // 将文件指针移动到文件开头
     ```


### 常用函数

#### 1. 文件的打开与关闭

**文件打开：`fopen`**

- **函数原型**：
    ```c
    FILE *fopen(const char *filename, const char *mode);
    ```
- **功能**：打开一个文件并返回一个指向该文件的指针。
- **参数**：
    - `filename`：要打开的文件名。
    - `mode`：文件打开模式。常用模式有：
    在 C 语言中，文件操作模式也可以结合二进制模式进行操作。二进制模式通过在文件模式字符串中添加一个字符 `'b'` 实现，具体格式如 `"rb"`, `"wb"`, 等等。以下是补充二进制相关内容后的完整表格：

| 模式      | 作用                                              | 文件存在      | 文件不存在 |
|-----------|---------------------------------------------------|---------------|------------|
| `"r"`     | 打开只读                                          | 成功打开      | 返回 NULL  |
| `"w"`     | 打开只写，文件存在则清空原文件内容                | 成功打开      | 创建新文件 |
| `"a"`     | 打开追加模式，文件指针位于末尾                    | 成功打开      | 创建新文件 |
| `"r+"`    | 以读写模式打开文件，不清空文件内容                | 成功打开      | 返回 NULL  |
| `"w+"`    | 打开读写，文件存在则清空原文件内容                | 成功打开      | 创建新文件 |
| `"a+"`    | 以读写模式打开文件，文件指针位于末尾              | 成功打开      | 创建新文件 |
| `"rb"`    | 打开二进制文件只读                                | 成功打开      | 返回 NULL  |
| `"wb"`    | 打开二进制文件只写，文件存在则清空原文件内容      | 成功打开      | 创建新文件 |
| `"ab"`    | 打开二进制文件追加模式，文件指针位于末尾          | 成功打开      | 创建新文件 |
| `"r+b"`   | 打开二进制文件读写，不清空文件内容                | 成功打开      | 返回 NULL  |
| `"w+b"`   | 打开二进制文件读写，文件存在则清空原文件内容      | 成功打开      | 创建新文件 |
| `"a+b"`   | 打开二进制文件读写，文件指针位于末尾              | 成功打开      | 创建新文件 |
| `"wx"`    | 只创建新文件写入模式，文件已存在则返回 NULL       | 返回 NULL     | 创建新文件 |
| `"wbx"`   | 只创建新二进制文件写入模式，文件已存在则返回 NULL | 返回 NULL     | 创建新文件 |



- **返回值**：成功时返回文件指针，失败时返回 `NULL`。

---

**文件关闭：`fclose`**

- **函数原型**：
    ```c
    int fclose(FILE *stream);
    ```
- **功能**：关闭文件，释放相关资源。
- **参数**：
    - `stream`：文件指针。
- **返回值**：成功时返回 `0`，失败时返回 `EOF`。

---

#### 2. 文件读取操作

##### 文本文件读取

**`fgetc`**

- **函数原型**：
    ```c
    int fgetc(FILE *stream);
    ```
- **功能**：从文件中读取一个字符。
- **参数**：
    - `stream`：文件指针。
- **返回值**：返回读取的字符，如果到达文件末尾，返回 `EOF`。

**`fgets`**

- **函数原型**：
    ```c
    char *fgets(char *str, int n, FILE *stream);
    ```
- **功能**：从文件中读取一行字符（包括空格）并存入 `str` 中，最多读取 `n-1` 个字符。
- **参数**：
    - `str`：存储读取内容的缓冲区。
    - `n`：缓冲区的大小。
    - `stream`：文件指针。
- **返回值**：返回 `str`，如果读取到文件末尾返回 `NULL`。

##### 二进制文件读取

**`fread`**

- **函数原型**：
    ```c
    size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
    ```
- **功能**：从文件中读取二进制数据，存入内存中。
- **参数**：
    - `ptr`：数据存储缓冲区。
    - `size`：每个元素的大小（字节）。
    - `count`：要读取的元素个数。
    - `stream`：文件指针。
- **返回值**：成功读取的元素个数。

---

#### 3. 文件写入操作

##### 文本文件写入

**`fputc`**

- **函数原型**：
    ```c
    int fputc(int c, FILE *stream);
    ```
- **功能**：向文件写入一个字符。
- **参数**：
    - `c`：要写入的字符。
    - `stream`：文件指针。
- **返回值**：成功返回写入的字符，失败返回 `EOF`。

**`fputs`**

- **函数原型**：
    ```c
    int fputs(const char *str, FILE *stream);
    ```
- **功能**：向文件写入一个字符串（不包含 `\0` 结束符）。
- **参数**：
    - `str`：要写入的字符串。
    - `stream`：文件指针。
- **返回值**：成功返回非负值，失败返回 `EOF`。

##### 二进制文件写入

**`fwrite`**

- **函数原型**：
    ```c
    size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
    ```
- **功能**：向文件写入二进制数据。
- **参数**：
    - `ptr`：数据源（内存中的数据）。
    - `size`：每个元素的大小（字节）。
    - `count`：要写入的元素个数。
    - `stream`：文件指针。
- **返回值**：成功写入的元素个数。

---

#### 4. 文件定位

**`fseek`**

- **函数原型**：
    ```c
    int fseek(FILE *stream, long offset, int whence);
    ```
- **功能**：将文件指针移动到指定位置。
- **参数**：
    - `stream`：文件指针。
    - `offset`：偏移量，单位为字节。可以是正值、负值或零。
    - `whence`：偏移基准位置。常用值有：
        - `SEEK_SET`：文件开头。
        - `SEEK_CUR`：当前位置。
        - `SEEK_END`：文件末尾。
- **返回值**：成功时返回 `0`，失败时返回非零值。

**`ftell`**

- **函数原型**：
    ```c
    long ftell(FILE *stream);
    ```
- **功能**：返回当前文件指针的偏移量（从文件开头开始计）。
- **参数**：
    - `stream`：文件指针。
- **返回值**：返回当前文件指针的位置（以字节为单位），失败时返回 `-1L`。

**`rewind`**

- **函数原型**：
    ```c
    void rewind(FILE *stream);
    ```
- **功能**：将文件指针重置到文件开头。
- **参数**：
    - `stream`：文件指针。
- **返回值**：无返回值。

---

#### 5. 错误处理

**`feof`**

- **函数原型**：
    ```c
    int feof(FILE *stream);
    ```
- **功能**：判断是否到达文件末尾。
- **参数**：
    - `stream`：文件指针。
- **返回值**：非零值表示文件结束，返回 `0` 表示未到达文件末尾。

**`ferror`**

- **函数原型**：
    ```c
    int ferror(FILE *stream);
    ```
- **功能**：检查文件是否发生错误。
- **参数**：
    - `stream`：文件指针。
- **返回值**：非零值表示发生错误，返回 `0` 表示没有错误。

---

#### 6. 文件清空与创建

**`freopen`**

- **函数原型**：
    ```c
    FILE *freopen(const char *filename, const char *mode, FILE *stream);
    ```
- **功能**：关闭当前文件并重新打开文件。
- **参数**：
    - `filename`：文件名。
    - `mode`：打开模式（如 `"r"`, `"w"`, `"a"` 等）。
    - `stream`：当前打开的文件指针。
- **返回值**：成功返回新的文件指针，失败返回 `NULL`。

---

#### 7. 文件缓冲与同步

**`setbuf`**

- **函数原型**：
    ```c
    void setbuf(FILE *stream, char *buffer);
    ```
- **功能**：为文件流设置缓冲区。
- **参数**：
    - `stream`：文件指针。
    - `buffer`：缓冲区指针。若为 `NULL`，则禁用缓冲。
- **返回值**：无返回值。

**`setvbuf`**

- **函数原型**：
    ```c
    int setvbuf(FILE *stream, char *buffer, int mode, size_t size);
    ```
- **功能**：为文件流设置缓冲区，支持不同的缓冲模式。
- **参数**：
    - `stream`：文件指针。
    - `buffer`：缓冲区指针。
    - `mode`：缓冲模式，通常为 `_IOFBF`（全缓冲）、`_IONBF`（无缓冲）或 `_IOLBF`（行缓冲）。
    - `size`：缓冲区大小。
- **返回值**：成功返回 `0`，失败返回非零值。

**`fflush`**

- **函数原型**：
    ```c
    int fflush(FILE *stream);
    ```
- **功能**：强制刷新文件缓冲区，将缓冲区中的内容写入文件。
- **参数**：
    - `stream`：文件指针。如果为 `NULL`，则刷新所有打开的输出流。
- **返回值**：成功返回 `0`，失败返回 `EOF`。

---

#### 8. 临时文件处理

**`tmpfile`**
- **函数原型**：
    ```c
    FILE *tmpfile(void);
    ```
- **功能**：创建一个临时文件并返回文件指针。该文件在程序结束时自动删除。
- **返回值**：成功返回临时文件指针，失败返回 `NULL`。

---

### 缓冲区


在 C 语言中，**文件缓冲区（Buffer）**是用来临时存储数据的一块内存区域，用于优化文件的输入和输出操作。缓冲区的引入可以减少实际文件操作的次数，从而提高程序的效率。

---

!!! question "输入内容怎样到达输出？"

    **用户输入 → 输入缓冲区 → 程序处理 → 输出缓冲区 → 输出设备**

    1. **用户输入**    
    当程序需要从用户获取输入时（例如通过键盘），数据首先由用户输入到操作系统的输入设备（如键盘缓冲区）。操作系统会将这些输入数据暂存，等待程序读取。

    ---

    2. **标准输入（stdin）**   
    C语言通过标准输入流（`stdin`）读取用户输入。`stdin`是一个指向标准输入设备的文件指针，通常与键盘输入关联。常用的输入函数包括：

    - `scanf()`：读取格式化输入。
    - `getchar()`：读取单个字符。
    - `fgets()`：读取一行字符串。

    3. **输入缓冲区**   
    - 当用户输入数据并按下回车键时，数据会被送入**输入缓冲区**。
    - 输入缓冲区是内存中的一块区域，用于临时存储用户输入的数据。
    - 程序从输入缓冲区中读取数据，而不是直接从键盘读取。

    ---

    4. **程序处理**   
    程序通过标准库函数（如`scanf()`或`getchar()`）从输入缓冲区中读取数据，并将其存储到程序的变量或内存中。程序可以对数据进行处理、计算或转换。

    ---

    5. **输出缓冲区**   
    当程序需要输出数据时（例如通过`printf()`），数据首先被写入**输出缓冲区**。输出缓冲区是内存中的一块区域，用于临时存储待输出的数据。

    6. **输出缓冲区的类型**   
    - **行缓冲**：当遇到换行符（`\n`）或缓冲区满时，数据会被刷新到输出设备（如屏幕）。
    - **全缓冲**：当缓冲区满时，数据才会被刷新（通常用于文件输出）。
    - **无缓冲**：数据立即输出，不经过缓冲区（通常用于标准错误输出`stderr`）。

    ---

    7. **标准输出（stdout）**   
    C语言通过标准输出流（`stdout`）将数据输出到标准输出设备（通常是屏幕）。常用的输出函数包括：

    - `printf()`：格式化输出。
    - `putchar()`：输出单个字符。
    - `puts()`：输出字符串。

    8. **输出缓冲区的刷新**    
    - 当输出缓冲区满、遇到换行符（`\n`）或调用`fflush(stdout)`时，缓冲区中的数据会被刷新到输出设备。
    - 如果程序正常结束，所有未刷新的缓冲区数据也会被自动刷新。

    ---

    9. **操作系统和硬件设备**    
    - 操作系统负责管理输入输出设备（如键盘、屏幕等）。
    - 当数据从输出缓冲区刷新时，操作系统会将数据传递给硬件设备（如屏幕），最终显示给用户。

---



??? info "**缓冲区的基本概念**"

    1. **缓冲的作用**：

    - 文件操作（如读写）通常涉及磁盘 I/O，这是一种相对慢的操作。
    - 为了减少磁盘 I/O 的频率，C 标准库在内存中分配了一块缓冲区。
    - 程序在读取或写入文件时，先将数据存储到缓冲区，达到一定量后再进行磁盘 I/O 操作。

    2. **缓冲区的分类**：

    - **全缓冲（Fully Buffered）**：当缓冲区填满时才进行实际的 I/O 操作。适用于文件。
    - **行缓冲（Line Buffered）**：每次遇到换行符或缓冲区满时，进行一次 I/O 操作。适用于标准输入输出（如 `stdin`、`stdout`）。
    - **无缓冲（Unbuffered）**：不使用缓冲区，每次 I/O 操作都直接访问设备或文件。适用于 `stderr`。

    ---

    **缓冲区在文件中的应用**

    - 文件操作函数如 `fopen()`、`fwrite()`、`fread()`、`fprintf()`、`fgets()` 等都会使用缓冲区。
    - 在写入时：
    - 数据先写入缓冲区。
    - 当缓冲区满、手动刷新缓冲区（`fflush()`）、或文件关闭时，数据被写入磁盘。
    - 在读取时：
    - 文件数据被读取到缓冲区，程序再从缓冲区中获取数据。

---

**常用函数与缓冲区相关操作**

1. **`fflush()`**
`fflush()` 用于清空缓冲区，将缓冲区中的数据立即写入文件或设备。
```c
int fflush(FILE *stream);
```
- 参数：
  - `stream`：文件流指针，表示需要刷新的文件。如果传递 `NULL`，则刷新所有输出流。
- 典型应用：
  - 在程序中强制写入文件。
  - 确保日志或调试信息及时输出。

示例：
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(file, "Hello, world!");
    fflush(file);  // 立即将缓冲区内容写入文件

    fclose(file);
    return 0;
}
```

2. **`setvbuf()`**
`setvbuf()` 用于设置文件的缓冲区模式及大小。
```c
int setvbuf(FILE *stream, char *buffer, int mode, size_t size);
```
- 参数：
    - `stream`：文件流指针。
    - `buffer`：自定义缓冲区（传递 `NULL` 表示使用默认缓冲区）。
    - `mode`：缓冲区模式，可选值：
        - `_IOFBF`：全缓冲模式。
        - `_IOLBF`：行缓冲模式。
        - `_IONBF`：无缓冲模式。
    - `size`：缓冲区大小（以字节为单位）。
- 返回值：
    - 成功返回 0，失败返回非零值。

示例：设置自定义缓冲区
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    char buffer[1024];  // 自定义缓冲区
    setvbuf(file, buffer, _IOFBF, sizeof(buffer));  // 设置全缓冲模式

    fprintf(file, "Buffered data.");
    fclose(file);  // 文件关闭时，缓冲区中的数据会写入文件

    return 0;
}
```

3. **`setbuf()`**
`setbuf()` 是 `setvbuf()` 的简单版本，用于设置文件流为全缓冲或无缓冲。
```c
void setbuf(FILE *stream, char *buffer);
```
- 参数：
    - `stream`：文件流指针。
    - `buffer`：缓冲区指针。如果为 `NULL`，文件流设置为无缓冲模式。

示例：设置无缓冲模式
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    setbuf(file, NULL);  // 设置文件流为无缓冲模式

    fprintf(file, "This will be written immediately.");
    fclose(file);

    return 0;
}
```

---

**缓冲区的默认行为**

1. **标准流的默认缓冲模式**：
    - `stdout`：行缓冲模式。
    - `stdin`：行缓冲模式。
    - `stderr`：无缓冲模式。
2. **文件流的默认缓冲模式**：
    - 通常是全缓冲模式，缓冲区大小一般由操作系统决定（通常为 4KB 或 8KB）。

---

**缓冲区可能引发的问题**

1. **未及时刷新缓冲区**：
    - 如果程序异常退出，缓冲区中的数据可能未被写入文件，导致数据丢失。
2. **并发操作冲突**：
    - 多线程或多进程同时操作同一文件时，缓冲区可能引发数据竞争，需要特别注意同步操作。

---

**总结**

- **缓冲区的作用**：提高文件 I/O 的效率，通过减少磁盘读写次数来优化性能。
- **关键操作**：
    - 使用 `fflush()` 手动刷新缓冲区。
    - 使用 `setvbuf()` 或 `setbuf()` 自定义缓冲区行为。
- **文件默认缓冲模式**：文件通常是全缓冲，标准流根据类型可能是行缓冲或无缓冲。
  





### 文件的输入输出

方法一：shell的重定向 

- `>` 将输出定向值后面的文件
- `<` 从后面的文件中读取输入

方法二：FILE

```c
int main()
{
    FILE* fp = fopen("try.c", "r");
    if(fp){
        fscanf(fp, "%d", &num);
        printf("%d\n", num);
        fclose(fp);
    }
    else{
        printf("文件打开失败");
    }
}
```

`fopen` : `FILE *fopen(const char *__restrict__ __filename, const char *__restrict__ __modes)`

- Open a file and create a new stream for it.
- 参数是两个字符串，第二个如下：

    ![alt text](res/images/image-13_1.png)


`fclose`: `int fclose(FILE *__stream)`

- Close STREAM.

对文本文件的读和写：

1. `fscanf` : `int fscanf(FILE *__restrict__ __stream, const char *__restrict__ __format, ...)`

 - Read formatted input from STREAM.
- 只是在`scanf`前面加一个FILE*的指针，其他都一样。

2. `fprintf` : `int fprintf(FILE *__restrict__ __stream, const char *__restrict__ __format, ...)`

- Write formatted output to STREAM.

对二进制文件的读和写

1. `fread` : `size_t fread(void *__restrict__ __ptr, size_t __size, size_t __n, FILE *__restrict__ __stream)`

    - Read chunks of generic data from STREAM.

2. `fwrite` : `size_t fwrite(const void *__restrict__ __ptr, size_t __size, size_t __n, FILE *__restrict__ __s)`

    - Write chunks of generic data to STREAM.

- FILE指针是最后一个参数

- 返回值是成功读写的字节数

- 对二进制文本的读写一般是通过对一个结构变量的操作进行的，因此，`__size` 代表一个结构的大小；`__n` 代表读写几个结构变量

### 在文件中定位

`ftell` : `long ftell(FILE *__stream)`
- Return the current position of STREAM.

`fseek` : `int fseek(FILE *__stream, long __off, int __whence)`
- Seek to a certain position on STREAM.
- 用来调整文件指针的位置。它适用于文本文件和二进制文件。通过 fseek，可以在文件中快速定位到某个特定的位置，以便后续读取或写入。
- 第三个参数：基准量：从哪里开始的第一步确定初始位置
    - `SEEK_SET` ：从头开始
    - `SEEK_CUR` ：从当前位置开始
    - `SEEK_END` ：从尾开始（倒过来）
- 第二个参数：偏移量：在第三个参数的基础上移动几个字节作为开始的seek的地方


未解决可移植性的问题：用文本

处理数据的方式：数据库 / 第三方库 （用C底层的文件/数据操作方式的少了）






## MISC

### 标签与goto

**label（标签）** 是一种标识符，用于标记一个特定的代码位置，通常与 `goto` 语句配合使用。标签是定义在函数内部的局部标识符，作用范围仅限于所在的函数。

---

**标签的定义语法**

```c
label_name:
    statement;
```

- **`label_name`** 是标签的名字，必须是一个合法的标识符。
- 冒号 `:` 表示这是一个标签。

**标签的作用**：标签通常与 `goto` 语句一起使用，实现程序流程的无条件跳转。

---

**示例**

```c
#include <stdio.h>

int main() {
    int x = 1;

start: // 标签 start
    printf("x = %d\n", x);
    x++;
    if (x <= 5) {
        goto start; // 跳转到标签 start
    }

    return 0;
}
```

**运行结果：**
```
x = 1
x = 2
x = 3
x = 4
x = 5
```

在上面的代码中，`goto start` 语句使程序跳转回 `start` 标签所在的位置，形成了一个循环结构。

---

**标签的特性**

1. **局部性：** 标签只能在定义它的函数内使用。
2. **唯一性：** 在一个函数内，标签名必须唯一。
3. **与`goto`配合：** 通常通过 `goto` 来跳转到标签，但仅仅定义标签并不会改变程序的执行顺序。

---

**使用场景**

虽然标签和 `goto` 提供了无条件跳转功能，但它们的使用会影响程序的可读性，容易导致“spaghetti code（意大利面条代码）”，因此应尽量避免使用。  

标签和 `goto` 通常在以下特殊场景中有用：

1. **错误处理：**
   当函数中出现复杂的嵌套逻辑时，可以使用标签和 `goto` 实现统一的错误处理。
   ```c
   #include <stdio.h>
   #include <stdlib.h>

   int main() {
       FILE *file = fopen("test.txt", "r");
       if (!file) {
           goto error; // 文件打开失败
       }

       // 正常处理文件
       fclose(file);
       return 0;

   error: // 错误处理
       printf("Error: Unable to open file.\n");
       return 1;
   }
   ```

2. **跳出多重嵌套：**
   标签可以直接跳出多层嵌套，而不需要复杂的条件判断。
   ```c
   #include <stdio.h>

   int main() {
       for (int i = 0; i < 3; i++) {
           for (int j = 0; j < 3; j++) {
               if (i == 1 && j == 1) {
                   goto end; // 跳出多重循环
               }
               printf("i = %d, j = %d\n", i, j);
           }
       }
   end:
       printf("Loop exited.\n");
       return 0;
   }
   ```

---

注意事项
1. **尽量避免滥用 `goto` 和标签**，尤其是可以通过结构化控制语句（如 `for`、`while`、`break`、`continue` 等）实现的逻辑，不要用 `goto`。
2. 标签和 `goto` 的过度使用会使代码难以阅读、难以维护，因此应谨慎使用。

替代方案
大多数情况下，可以通过函数调用、循环、条件语句（如 `if`）和异常处理机制代替标签和 `goto`。



[编程语言热度榜](https://www.tiobe.com/tiobe-index/)

<!-- ## 计算机基础
程序的执行
	解释
	编译
告诉计算机干什么：编程语言
与计算机交谈：命令行
计算的步骤：算法
让计算机做的事情：计算
C用处
底层（服务器、操作系统）：C
前端（网站前端）：其他语言 -->