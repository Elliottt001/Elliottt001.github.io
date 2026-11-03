
# C 语言错题与心得

## 数组的定义和传参

```c
int arr[3] = {1, 2, 3};
int arr2[] = {1, 2, 3};  // 有初始化，长度可以省略
```

`int arr[];` 没有初始化也没有长度，不能这样定义局部数组。`int arr;` 本身是合法的，只不过定义的是一个整数，不是数组。

变长数组：C99 的 `int arr[n]` 要求 n 是已经求出、且大于 0 的值。不能先 `int n;` 不赋值，就直接拿 n 开数组；C++ 标准也不支持这种变长数组写法。

函数参数：

```c
void sort(int arr[], int size);
// 调用：sort(arr, 3);
```

传数组名，另外传长度。`sort(arr[3], 3)` 传的是一个元素，还越界了；`int arr[3]` 的有效下标只有 0、1、2。

### 理论

- 循环 if 条件内部将 == 写成 = ：
	变量被重新赋值，返回新的值给括号内判断真假：0则假， 非0则真；<font color="#00b0f0">其实就是看括号内表达式的真假</font>
	真则执行它，假则执行后面的
	
	int x = 2, y;
	if(x = 5) y = 5;
	else y = 6;
	printf("%d %d", x,y);
	
	int x, y;
	if(x = 0) y = 6;
	else y = 5;
	printf("%d %d", x,y);
	
	int x = 0, y;
	if(x++) y = 5;
	else y = 6;
	printf("%d %d", x,y);
	
	int x = 0, y;
	if(++x) y = 5;
	else y = 6;
	printf("%d %d", x,y);
	
	以上程序段执行后，x和y分别是多少呢？


- 循环内外用相同的循环变量：
	1      # include<stdio.h>
	2       int main()
	3       {
	4               int i;
	5               for(i = 1; i < 20; i++)
	6               {
	7                       for(i = 1; i<= 10; i++)
	8                       {
	9                               printf("hi");
	10                      }
	11              }
	12      }

- 循环的执行过程
	上面那个程序到gdb里面run一下
	`for`：初始化 → 判断条件 → 循环体 → i++ → 再判断。不是看见整个 for 语句就先加 1。内外循环复用 i 会互相改状态，这个例子会让外层 i 反复回到 12，无法正常结束。
- int 和 double

4-4问一下

### 实验

- 循环与分支
	循环：while和for，两种
	分支：if和switch
	if 不是循环！
	while不是判断！
	***if 和 while 别混***
	

- 学会用flag

- 函数
	- 别忘了 return 
	- 别忘了函数定义处的参数类型

- scanf函数

	scanf 别忘&
- 循环
	while比for更加灵活好像！后面再想想
	while（1）为无限循环

- 单双引号

    - 字符都是单引号，字符串双引号
	- `isxdigit`, `toupper`之类的函数的参数为字符
	- `atoi` 函数参数为字符串

- 数字比较大（例如阶乘、斐波那契），先看类型范围。`long long` 比 int 大，但也有限；`double` 能表示更大的数量级，却不能精确表示所有大整数。C 的有符号整数溢出是未定义行为，不能认定它一定变成负数。要求精确的大整数，要用高精度表示。

#### string.h中的函数

- `strcpy` & `strncpy`

	```c
    if (len % 2 == 1) {
        // 长度为奇数：删除中间字符
        int mid = len / 2;
        strncpy(dest2, dest1, mid);                  // 拷贝前半部分
        strcpy(dest2 + mid, dest1 + mid + 1);        // copy后半部分
        dest2[len - 1] = '\0'; // 新长度
	}
	/* 代码解析
	将 dest1 的中间字符之后的部分（从 mid + 1 开始）复制到 dest2 的中间字符位置。
	dest2 + mid 表示从 dest2 的 mid 索引位置开始放置数据。
	dest1 + mid + 1 表示从 dest1 的 mid + 1 索引位置开始读取数据。
	例如：

	若 dest1 = "abcde"，mid = 2：
	dest1 + mid + 1 是 "de"（从索引 3 开始）。
	dest2 在完成此操作后为 "abde"。
	*/
	```

## Thought & Summary

### 存在的问题：
version1.0
程序填空题想不到
基础理论知识完全空白

version1.5
理论杂项仍有缺漏
细节
对知识的理解
<font color="#ff0000">没有一步一步仔细读程序，没有耐心去静下来读程序，而是据自己的感觉推理：上一步是啥下一步就照着他来</font>
# Methods

### Exams：

//计科机考：
//上来先看编程题
//有思路则立马写注释，
//没思路就过，中间想想


第一题5min拿下
一定相信自己做的出来！
先想好再写！先想好再写！先想好再写！
用草稿纸！用草稿纸！用草稿纸！
先把所有思路想到想完整，
别一上来就写，

在草稿纸上：
	写出来所有要用的函数，
	写一下函数怎样实现
