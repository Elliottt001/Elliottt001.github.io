## 资源

[YL](https://www.yuque.com/u26596123/re4lmd?)

- [Python基础语法](https://www.yuque.com/u26596123/re4lmd/glsgkqzrtygbmugy)

- [Python进阶语法-判断, 循环与函数](https://www.yuque.com/u26596123/re4lmd/zcvm1zlsdnagtbd2)

- [Python进阶语法-数据容器](https://www.yuque.com/u26596123/re4lmd/lqgrxxcmboh41glw)

- [Python高阶语法](https://www.yuque.com/u26596123/re4lmd/on3q87t95utuea4o)

[骆昊](https://github.com/jackfrued/)

- [Python-100-Days](https://github.com/jackfrued/Python-100-Days)

- [Python-Core-50-Courses](https://github.com/jackfrued/Python-Core-50-Courses/)

[官方文档](https://docs.python.org/zh-cn/3.13/)

[极客教程](https://geek-docs.com/)
- [python](https://geek-docs.com/python/python-top-tutorials/)

## 工具

### IPython

启动
```shell
python3 -m IPython
```
退出
```shell
exit  # or: exit()
```

查看帮助

```shell
help()
# follow the guidence: 
'''
To get a list of available modules, keywords, symbols, or topics, type "modules", "keywords", "symbols", or "topics".  Each module also comes with a one-line summary of what it does; to list the modules whose name or summary contain a given string such as "spam", type "modules spam".
'''
q  # to quit one spesific item
quit  # to quit the help file 
```

编程：按正常的一行一行输进去即可。

## 编程风格

### 变量命名

PEP 8要求：

- 用小写字母拼写，多个单词用下划线连接。
- 受保护的实例属性用单个下划线开头。
- 私有的实例属性用两个下划线开头。

## 语言元素

#### 指令和程序

计算机的硬件系统通常由五大部件构成，包括：运算器、控制器、存储器、输入设备和输出设备。其中，运算器和控制器放在一起就是我们通常所说的中央处理器，它的功能是执行各种运算和控制指令以及处理计算机软件中的数据。我们通常所说的程序实际上就是指令的集合，我们程序就是将一系列的指令按照某种方式组织到一起，然后通过这些指令去控制计算机做我们想让它做的事情。今天我们大多数时候使用的计算机本质来说仍然属于[“冯·诺依曼结构”](https://zh.wikipedia.org/wiki/%E5%86%AF%C2%B7%E8%AF%BA%E4%BC%8A%E6%9B%BC%E7%BB%93%E6%9E%84)的计算机。“冯·诺依曼结构”有两个关键点，一是指出要将存储设备与中央处理器分开，二是提出了将数据以二进制方式编码。

### 变量和类型

在程序设计中，变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。

- 整型：支持二进制（如`0b100`）、八进制（如`0o100`）、十进制（`100`）和十六进制（`0x100`）的表示法。
- 浮点型：数学写法（如`123.456`）& 科学计数法（如`1.23456e2`）。
- 字符串型：
	- 单引号或双引号，如`'hello'`和`"hello"`
	- 原始字符串表示法：子啊字符串前加上 `r` 或 `R` 来实现，效果：忽略转义字符，直接按照字面内容处理字符串。场景：处理正则表达式、文件路径等需要保留反斜杠的场景。
		```python
		# 正则表达式
		import re
		pattern = r"\bword\b"
		match = re.search(pattern, "This is a word.")
		print(match)  # 输出: <re.Match object; span=(10, 14), match='word'>

		# 文件路径
		path = r"C:\Users\Name\Documents"
		print(path)  # 输出: C:\Users\Name\Documents
		```
	- 字节字符串表示法

	??? info "字节字符串表示法"

		在 Python 中，字符串可以表示为普通的 Unicode 字符串（`str` 类型），也可以表示为字节字符串（`bytes` 类型）。字节字符串是一种以字节为单位的数据表示形式，通常用于处理二进制数据或编码后的文本数据。

		以下是 Python 中字符串的字节字符串表示法的详细说明：

		---

		1. **字节字符串的类型**
		字节字符串的类型是 `bytes`，它是不可变的序列，每个元素是一个字节（0 到 255 之间的整数）。

		---

		2. **创建字节字符串**
		可以通过以下方式创建字节字符串：

		方法 1：使用 `b` 前缀
		在字符串前加 `b` 前缀，可以创建一个字节字符串：
		```python
		byte_string = b"hello"
		print(byte_string)  # 输出: b'hello'
		print(type(byte_string))  # 输出: <class 'bytes'>
		```

		方法 2：使用 `bytes()` 函数
		将字符串或可迭代对象转换为字节字符串：
		```python
		# 从字符串创建字节字符串
		byte_string = bytes("hello", encoding="utf-8")
		print(byte_string)  # 输出: b'hello'

		# 从整数列表创建字节字符串
		byte_string = bytes([104, 101, 108, 108, 111])
		print(byte_string)  # 输出: b'hello'
		```

		方法 3：使用字符串的 `.encode()` 方法
		将普通字符串编码为字节字符串：
		```python
		text = "hello"
		byte_string = text.encode("utf-8")  # 使用 UTF-8 编码
		print(byte_string)  # 输出: b'hello'
		```

		---

		3. **字节字符串的操作**
		字节字符串支持许多与普通字符串类似的操作，例如索引、切片、拼接等。

		示例：
		```python
		byte_string = b"hello"

		# 索引
		print(byte_string[0])  # 输出: 104（字节的整数值）

		# 切片
		print(byte_string[1:4])  # 输出: b'ell'

		# 拼接
		new_byte_string = byte_string + b" world"
		print(new_byte_string)  # 输出: b'hello world'
		```

		---

		4. **字节字符串与普通字符串的转换**
		字节字符串和普通字符串之间可以通过编码和解码相互转换。

		将字节字符串解码为普通字符串
		使用 `.decode()` 方法：
		```python
		byte_string = b"hello"
		text = byte_string.decode("utf-8")  # 使用 UTF-8 解码
		print(text)  # 输出: hello
		```

		将普通字符串编码为字节字符串
		使用 `.encode()` 方法：
		```python
		text = "hello"
		byte_string = text.encode("utf-8")  # 使用 UTF-8 编码
		print(byte_string)  # 输出: b'hello'
		```

		---

		5. **字节字符串的表示法**
		字节字符串在 Python 中以 `b'...'` 的形式表示。如果字节的值对应可打印的 ASCII 字符，则直接显示字符；否则显示 `\x` 开头的十六进制值。

		示例：
		```python
		byte_string = b"hello\x80world"
		print(byte_string)  # 输出: b'hello\x80world'
		```

		- `h`, `e`, `l`, `l`, `o` 是可打印的 ASCII 字符，所以直接显示。
		- `\x80` 是不可打印的字符，所以显示为 `\x80`。

		---

		6. **字节字符串的应用场景**
		- **处理二进制数据**：例如读取图片、音频、视频等文件。
		- **网络通信**：在网络传输中，数据通常以字节形式发送和接收。
		- **编码转换**：处理不同编码的文本数据。

		---

		7. **注意事项**
		- 字节字符串是不可变的，如果需要修改，可以转换为 `bytearray`（可变类型）。
		- 字节字符串和普通字符串不能直接拼接或比较，需要先进行编码或解码。

		---

		示例代码
		```python
		# 创建字节字符串
		byte_string = b"hello"
		print("Byte string:", byte_string)

		# 解码为普通字符串
		text = byte_string.decode("utf-8")
		print("Decoded text:", text)

		# 编码为字节字符串
		new_byte_string = text.encode("utf-8")
		print("Encoded byte string:", new_byte_string)

		# 处理非 ASCII 字符
		byte_string = b"hello\x80world"
		print("Byte string with non-ASCII:", byte_string)
		```

		**输出**：
		```
		Byte string: b'hello'
		Decoded text: hello
		Encoded byte string: b'hello'
		Byte string with non-ASCII: b'hello\x80world'
		```


	- Unicode字符串表示法：默认情况（即 str 类型）
	- 写成多行的形式：用三个单引号或三个双引号开头&结尾。

- 布尔型：`True`、`False`
	- 直接用`True`、`False`表示
	- 通过布尔运算计算出来（如`3 < 5`产生`True`）

- 复数型：形如`3+5j`

可以使用`type()`函数对变量的类型进行检查

可以使用Python中内置的函数对变量类型进行转换。

- `int()`：数值 or 字符串 $\to$ 整数，*可以指定进制*。

	??? info "int()函数进制转换"

		`int()` 函数的基本用法
		```python
		int(x, base=10)
		```

		- **`x`**：要转换的值，可以是字符串或数字。
		- **`base`**：进制数，默认为 10（十进制）。取值范围是 **2 到 36**。

		---

		指定进制的规则
		1. **`base=2`**：二进制（字符串只能包含 `0` 和 `1`）。
		2. **`base=8`**：八进制（字符串只能包含 `0` 到 `7`）。
		3. **`base=10`**：十进制（字符串只能包含 `0` 到 `9`）。
		4. **`base=16`**：十六进制（字符串可以包含 `0` 到 `9` 和 `a` 到 `f`，不区分大小写）。
		5. **其他进制**：支持 2 到 36 之间的任意进制。

		---

		示例

		自定义进制（例如 5 进制）
		```python
		custom_str = "20"
		decimal_num = int(custom_str, base=5)
		print(decimal_num)  # 输出: 10
		```

		---

		注意事项
		1. **字符串前缀**：
		- 如果字符串以 `0b`、`0o` 或 `0x` 开头，Python 会自动识别为二进制、八进制或十六进制，此时不需要指定 `base`。
		- 示例：
			```python
			binary_str = "0b1010"
			decimal_num = int(binary_str, base=0)  # base=0 表示自动识别
			print(decimal_num)  # 输出: 10
			```

		2. **非法字符**：
		- 如果字符串中包含不符合指定进制的字符，会抛出 `ValueError`。
		- 示例：
			```python
			invalid_str = "12"
			try:
				decimal_num = int(invalid_str, base=2)  # 2 进制不能包含 2
			except ValueError as e:
				print("Error:", e)
			```

		3. **负数**：
		- 如果字符串表示负数，可以直接转换。
		- 示例：
			```python
			negative_str = "-1010"
			decimal_num = int(negative_str, base=2)
			print(decimal_num)  # 输出: -10
			```

		---

		综合示例
		```python
		# 二进制转十进制
		binary_str = "1010"
		print(int(binary_str, base=2))  # 输出: 10

		# 八进制转十进制
		octal_str = "12"
		print(int(octal_str, base=8))  # 输出: 10

		# 十六进制转十进制
		hex_str = "A"
		print(int(hex_str, base=16))  # 输出: 10

		# 自动识别前缀
		prefix_str = "0b1010"
		print(int(prefix_str, base=0))  # 输出: 10

		# 负数
		negative_str = "-1010"
		print(int(negative_str, base=2))  # 输出: -10
		```



- `float()`：字符串 $\to$ 浮点数。
- `str()`：指定的对象 $\to$ 字符串形式，*可以指定编码*。
- `chr()`：整数 $\to$ 该编码对应的字符串（一个字符）。
- `ord()`：字符串（一个字符） $\to$ 对应的编码（整数）。

下面的代码通过键盘输入两个整数来实现对两个整数的算术运算。

```Python
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))

print('%d / %d = %f' % (a, b, a / b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
```

> 用了占位符语法，`%%`表示百分号（带占位符的字符串中要表示百分号必须写成`%%`）

### 运算符

#### 优先级

| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]` `[:]`                                                   | 下标，切片                     |
| `**`                                                         | 指数                           |
| `~` `+` `-`                                                  | 按位取反, 正负号               |
| `*` `/` `%` `//`                                             | 乘，除，模，整除               |
| `+` `-`                                                      | 加，减                         |
| `>>` `<<`                                                    | 右移，左移                     |
| `&`                                                          | 按位与                         |
| `^` `\|`                                                      | 按位异或，按位或               |
| `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                                    | 等于，不等于                   |
| `is`  `is not`                                               | 身份运算符                     |
| `in` `not in`                                                | 成员运算符                     |
| `not` `or` `and`                                             | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|`=` `^=` `>>=` `<<=` | （复合）赋值运算符             |

转义字符 `\`

### 逻辑运算符

`and` $\Leftrightarrow$ `$$`
`or` $\Leftrightarrow$ `||`
`not` $\Leftrightarrow$ `!`
两边连布尔值


```Python
flag0 = 1 == 1  # 比较运算符的优先级高于赋值运算符
print('flag0 =', flag0)    # flag0 = True

```

> **说明**：`print`函数可以输出多个值，多个值之间可以用`,`进行分隔，输出的内容之间默认以空格分开。

> 格式化字符串: 
> - `print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')` 
> - `print("%.1f华氏度 = %.1f摄氏", % (f, c))`



## 分支结构

### 应用场景

迄今为止，我们写的Python代码都是一条一条语句顺序执行，这种代码结构通常称之为顺序结构。然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的通关条件是玩家获得1000分，那么在完成本局游戏后，我们要根据玩家得到分数来决定究竟是进入第二关，还是告诉玩家“Game Over”，这里就会产生两个分支，而且这两个分支只有一个会被执行。类似的场景还有很多，我们将这种结构称之为“分支结构”或“选择结构”。给大家一分钟的时间，你应该可以想到至少5个以上这样的例子，赶紧试一试。

### if语句的使用

在Python中，要构造分支结构可以使用`if`、`elif`和`else`关键字。所谓**关键字**就是有特殊含义的单词，像`if`和`else`就是专门用于构造分支结构的关键字，很显然你不能够使用它作为变量名（事实上，用作其他的标识符也是不可以）。下面的例子中演示了如何构造一个分支结构。

```Python
"""
用户身份验证

Version: 0.1
Author: 骆昊
"""
username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
```

需要说明的是和C/C++、Java等语言不同，Python中没有用花括号来构造代码块而是**使用了缩进的方式来表示代码的层次结构**，如果`if`条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。换句话说**连续的代码如果又保持了相同的缩进那么它们属于同一个代码块**，相当于是一个执行的整体。**缩进**可以使用任意数量的空格，但**通常使用4个空格**，建议大家**不要使用制表键**或者**设置你的代码编辑工具自动将制表键变成4个空格**。

当然如果要构造出更多的分支，可以使用`if...elif...else...`结构或者嵌套的`if...else...`结构，下面的代码演示了如何利用多分支结构实现分段函数求值。

![$$f(x)=\begin{cases} 3x-5&\text{(x>1)}\\x+2&\text{(-1}\leq\text{x}\leq\text{1)}\\5x+3&\text {(x<-1)}\end{cases}$$](./res/formula_1.png)

```Python
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
```

当然根据实际开发的需要，分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出等级（比如点亮两颗或三颗星星），那么我们就需要在`if`的内部构造出一个新的分支结构，同理`elif`和`else`中也可以再构造新的分支，我们称之为嵌套的分支结构，也就是说上面的代码也可以写成下面的样子。

```Python
"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

Version: 0.1
Author: 骆昊
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
```

> **说明：** 大家可以自己感受一下这两种写法到底是哪一种更好。在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”，之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，所以能使用扁平化的结构时就不要使用嵌套。





## 函数
### 变量的作用域

全局变量可以在函数体内访问，但是内部不能修改！

如果尝试修改，会报错

如果想要修改：
	用global关键字 : 不建议！！！
```python
y = 10
def func():
	global y
	y = 20
	return
func()
print("y = ", y)
```

修改：用调用函数，返回值赋给要修改的那个变量
eg：
```python
y = 10
def func(y):
	#对y一番操作
	return y
y = func(y)
```

### 函数的多返回值
```python
def func(pra):
	# 代码块
	return ret1, ret2
# 返回的是一个元组，当然可以多个
	# 如果直接print函数调用的那个，输出一个带括号的数对，即元组
	# 也可以用几个变量去接收函数的返回值：a1, a2 = func(pram) : 实际是元组的解包
	# 即：
a, b = func_name(pra)
```
### 传参
- 关键词传参：形参名 = 实参值

- 位置传参：按位置

- 混合使用
	- 可以，不建议，会被辞退
	- 如果位置的出现在关键词的后面，会报错

- 默认参数：给默认参数的全放在不给默认参数的后面，否则会报错

### 函数作为参数传递
形参那里写一个形参代表函数

实参写函数名字！不能带括号，因为带了括号的意思是调用那个函数，则会报错（少参数）

作用：
- 回调
- 可以通过改变传入的作为参数的函数（即：回调函数），灵活的改变我在这个函数中调用哪个函数（比函数的嵌套灵活）
```python
def add(x, y):
    return x + y
def min(x, y):
    return x - y
def mul(x, y):
    return x * y
def calculator(x, y, operator):
    return operator(x, y)
print(f"{calculator(3, 5, add)}\n")
print(calculator(3, 5, min))
print(calculator(3, 5, mul))
```

## 数据容器

### 数据容器总结
![[63178ff0bddb8b3d19ff53ae8417e90.jpg]]
![[767def4f0bdfa79420e48fb7b1c3371.jpg]]
#### .方法
	new_name = sorted(name, reverse)
		reverse: 不传默认False : 不倒序即正序
		reverse = True : 倒序
			对字典用sorted：对key进行排序，返回包含所有键的列表
			对字符串用sorted：返回一个包含所有拆开了字符的列表
	max_item = max(name)
	min_item = min(name)

#### 比大小
ASCII, UTF-8

逻辑：一个一个比，到不一样的那个开始出大小，跟长度没关系
### 序列sequence
#### 序列总结
![[e3aa546b6378288f581c530b96df6b4.jpg]]

##### 序列的切片
定义：取出一个子序列

语法：sequence_name\[start: stop: step]

- 语法：


	- start : 省略默认0

	- stop : 省略默认值为len(sequence_name)，前取后不取

	- step : 省略默认1；负数：正负决定取值顺序（输出和读取从前到后or从后到前）；跳过stop-1个去取

- 超限：不报错，到最后

- 逻辑：读到start，看step（正负&大小），按他在序列里面找到stop

- 应用：
	倒序输出：print(序列名\[ : : -1]) : 如果前面两个都没填，则默认第一个是-1，最后一个是0

#### 列表list
##### 定义
方法1. list_name = \["任意类型的数据", 123, 4 + 5j, \["甚至可以放列表", 5.3], None, True]

方法2. list_name = list( "里面什么都能装")
##### 访问
list_name\[index] : index从0开始
超过限制：报错

index是负数：反向index：最后一个-1，倒数第二个-2，依此类推

二维列表（列表·里面有列表）：list_name\[index1]\[index2]
##### 修改
list_name\[index] = new_item_which_can_be_any_type
##### 点操作
访问对象的属性和方法

每一种数据类型都是一个类，当用这种数据类型，就是引出一个对象，就可以用这个对象的属性和方法
因此，list后面跟.就可以访问他的方法（函数）

有这些：

	list_name.index(item) 
		返回item的从小到大第一个匹配到的index，默认是正下标
		如果没有这个item，报错
	list_name.count(item)
		返回item在这个list中出现的次数
	len()
		是内置函数，不是list的方法
		用于返回任意可迭代对象的长度
			len("Hi hi")
			len(my_list)  若其中有一个列表，他算一个元素
	list_name.insert(aiming_position, the_inserted_intem)
		要插入到哪里，第一个参数就写几
	list_name.append(the_inserted_intem)
		在末尾添加the_inserted_intem这个元素
	list_name.extend(the_extended_list_name)
		将一个列表the_extended_list_name并入另一个列表list_name，就是元素插在后面
		完全等价于：list_name += the_extended_list_name
		改变了list_name这个列表
	list_name.remove(item)
		作用是删除从前到后匹配到的第一个item
		如果想都删：遍历 for item in list_name: list_name.remove(item)
	list_name.pop(index)
		删除那个下标对应的元素
		完全等于：del list_name\[index]
			del是一个python内置函数
	list_name.clear()
		清除列表中所有元素
	list_name.sort()
		排序

##### 循环遍历
```python
index = 0
while(index < len(list_name)):
	# 代码块
	index += 1
```
```python
for item in list_name:
	# 代码块
```
```python
index = 0
for index in range(0, len(lit_name)):
	# 代码块
```
PS: range(start, stop, step)
- start : 省略默认0
- stop : 前取后不取
- step : 省略默认1

#### 元组tuple
##### 跟list：
定义：把\[]变成()即可

不同：不能修改！所以.方法没有添加删除那几个

相同：

	.index()
	.count()
	len()
##### 元组的解包
```python
tuple_name = (item1, item2, item3) #多个item，可以是任意数据类型
a, b, c = tuple_name
# 现在，a是item1， 依此类推
```
##### 作用
保护数据，不可修改
函数的多返回值是个元组

##### tips
```python
my_tuple = (124, 'hello', ["a", "b", 89])
my_tuple[2][0] = 'A'
print(my_tuple)
# 被修改了
```

#### 字符串string
##### 跟list相同点
	.index()
	.count()
	len()
##### 跟list不同
不可直接修改！

如果要修改，换新的字符串：见下，用.方法: new_str = ori_str.func(pra)
##### .方法（修改必须新字符串+调用函数）

原字符串永远不可能被修改

	new_str_name = ori_str_name.replace("ori_char", "new_char")
		把所有ori_char都换成new_char
		常用的方法：
			new_str_name = ori_str_name.replace("ori_char", "") ：删除所有ori_char
				例如：new_str_name = ori_str_name.replace(" ", "")：删除所有空格
	new_str_list = ori_str_name.split("flag_char")
		按照flag_char分割字符串，将分割后的碎片存入数组，同时结果中没有flag_char
		![[d60d854b590e526d3b54f08e2bdbaf7.jpg]]
		找到所有单词：new_str_list = ori_str_name.split(" ") or new_str_list = ori_str_name.split()
		不传参数默认是空格
		不能传空字符串
		传入string中没有的东西，返回一个列表，里面有一个元素是ori_str_name
		将每一个char都分开：强制类型转换
			new_str_list = list(ori_str_name)
	new_str_name = ori_str_name.strip("aiming_char")
		字符串的规整：把ori_str_name前后两端的aiming_char删掉
		不传参数：默认空格：想删除前后空格则new_str_name = ori_str_name.strip()
			场景：用AI聊天式办公：前后的空格都占用AI的算力，故删除

### 另外两个
#### 集合set
##### 特点：
不重复、无序、无索引index！
可以修改！
##### 定义：
方法一：set_name = {item1, item2, item3, ......}

方法二：set_name = set(item1, item2, item3, ......)
##### .方法
	len(set_name)也适用
	set_name.add(added_item)
		追加元素，当然，没有顺序随机放置，甚至每次打印那些个元素的顺序都不一样
		如果多次add()同一个元素，则只加一次
	set_name.remove(added_item)
		删除指定元素
	set_name.pop()
		随机删除一个元素
	set_name.clear()
		清空集合

##### 集合的运算(也是.方法)
并集
- 方法一：new_set = set1 | set2
- 方法二：new_set = set1.union(set2)

交集
- 方法一：new_set = set1 & set2
- 方法二：new_set = set1.intersection(set2)

差集
- 方法一：new_set = set1 - set2
- 方法二：new_set = set1.difference(set2)

##### 遍历
只能用for：for item in set_name:

while不行: 因为没有index

##### 应用
给列表去重

	引用：爬去豆瓣排名前100的导演，去分析他们的合作关系之类的东西
```python
my_list = [……]
my_list = list(set(my_list))
```

#### 字典dict
##### 定义
方法1：dict_name = {key1: value1, key2: value2, key3: value3 ……} ：元素为键值对

方法2：dict_name = dict()
##### 规范
数据类型：除键不能是字典外，对key和value其他随便啥数据类型都行

key要唯一：如果不唯一则后面覆盖前面（即按最后一个算）
##### 访问
查找：dict_name\[key_name]

新增：dict_name\[new_key_name] = new_value

修改：dict_name\[key_name] = new_value
	<!--可以通过这种方式修改高考分数：各省考试院对数据库重视程度不一样，有些存在漏洞，故可以修改-->
	<!--在ZJU，可以黑进教务网修改考试成绩，但是你的技术没达到那种超级tmd顶尖的水平，留痕是不可避免的，可溯源，抓到直接……-->
	<!--“我干过别的……嘿嘿嘿……”看看人家大学四年的技术水平，本科毕业直接工作，报价3000的爬虫小项目-->
	<!--by YL-->
没有下标索引
##### .方法
	dict_name.pop(key_name)
		删除指定元素
	dict_name.clear()
		清空字典
	len(dict_name)
		元素个数
	dict_name.keys()
		获取所有的key
		字典的遍历
			方法一：for key in dict_name.keys()
			方法二：for key in dict_name
				print(dict_name\[key]) : 打印出所有值，是个列表
	dict_name.values()
		获取所有value
		返回为dict_values(\[……])：是dict_value类型（用print(dict_name.values())即可），可以print(list(dict_name.values()))直接类型转换
			字典的遍历
				方法三：for value in dicyt_name.values()
	dict_name.items()
		获取所有键值对
		返回值将每个键值对存入一个元组
		所以：优雅的遍历获取键值对方法：
			for key, value in key_name.items()
			这里同时完成了元祖的解包，可以打印：print(f"key:{key}, value:{value}")

## 异常的捕获和处理

[Python高阶语法](https://www.yuque.com/u26596123/re4lmd/on3q87t95utuea4o)

### 定义语法
```python
# 方法一
try:
  # 可能出现异常的代码
except:
  # 出现异常的话要执行的代码
finally:
  # 无论出没出异常，做什么
# 后面要继续执行的代码

# 执行逻辑：执行try后面的很多行代码，如果出现报错，则执行except后面的代码；不管出没出现异常，都执行finally画面的
```
```python
# 方法二：最常用
try:
  # 可能出现异常的代码
except Exception as error: # 其中错误类型是python关键字，error是我指定的临时变量
  # 出现异常的话要执行的代码例如：
  print(f"出错了！错误类型是：{error}")
finally:
  # 无论出没出异常，做什么
# 后面要继续执行的代码
```
```python
# 方法三
try:
  # 可能出现异常的代码
except 错误类型 as e: # 其中错误类型是python关键字，e是我指定的临时变量
  # 出现异常的话要执行的代码例如：
  print(f"出错了！错误类型是：{e}")
finally:
  # 无论出没出异常，做什么
# 后面要继续执行的代码
```

其中错误类型：

- 如果有需求说特定错误需要干特定的事情：看这张指定错误表，按方法三
	![[ad2f337607ec191678ce5e5a1b21fdc.jpg]]
- 如果没有知道并打印具体错误类型的需求：按方法一
- 如果想打印错误类型，没有不同错误打印不同东西的需求：按方法二
也不一定是打印，就特定的需求吧

例子：
```python
def div(a, b):
    return a/b
def calculator(a, b, op):
    try:
        result = op(a, b)
    except Exception as e:
        return f"出错了，错误类型是：{e}"
    return result
a = int(input())
b = int(input())
print(calculator(a, b, div))
```
### 杂项
1. 异常捕获具有传递性
	随着*程序执行的过程*（函数的参数传递和调用过程……）进行传递
		看：YL 7.32 2:28:00
2. except后面得有一个return
	目的是*跳出函数*（结束这一段的执行），跳出之后可以继续执行下面的，如果没有，就跳不出，将会报错并在函数这里停下

## 类和对象

[Python高阶语法](https://www.yuque.com/u26596123/re4lmd/on3q87t95utuea4o)

### 类的定义方法（不够简便）
### 类的构造方法（最简便的）
```python
class Animal():
    def __init__(self, name, age, sound, species = "动物", love_status = False):
        self.name = name
        self.age = age
        self.sound = sound
        self.species = species
        self.__love_status = love_status
    def eat(self):
        print(f"{self.name} is eating")
    def make_sound(self):
        print(f"{self.name}'s sound is {self.sound}")
    def __str__(self):
        return f"我是一只{self.species}"
    def __repr__(self):
        return f"nme:{self.name}, age:{self.age}, sound:{self.sound}, species:{self.species}, love_status:{self.love_status}"
    def __add__(self, other):
        if(self.__love_status and other.__getlove_status):  # 类内的方法可以访问(利用）类内的私有属性__love_status
            return f"{self.name} and {other.name} both have a spouse"
        print(f"{self.name} fells in love with {other.name}")
        return f"their kid's name is {self.name[0] + other.name[0]}"
    def __sub__(self, other):
        return f"{self.name} and {other.name} are not friends"
    def __call__(self):
        self.make_sound()
        # return self.__str__() : 不建议
    def __len__(self):
        return self.age
    def __getitem__(self, index):
        return self.sound[index]
    def __setitem__(self, index, value):
        self.sound[index] = value
    def __getlove_status(self):
        return self.__love_status
# 别看这里的类的继承，AI写的好像有错
class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound, love_status="单身")
    def call(self):
        print(f"{self.name} is barking")
  
dog = Dog(name="公子", age=10, sound="wangwang")
tiger = Animal(name = "齐威王", age=10, sound="roar", species="老虎")
cat = Animal(name = "男爵", age=10, sound="miaomiao", love_status=True, species="猫")
  
animals = [dog, tiger, cat]
for animal in animals:
    animal.make_sound()
  
print(dog)
print(dog + tiger) # 类内的方法可以访问类内的私有属性__love_status
print(dog - cat)
print(tiger())
print(len(tiger))
print(tiger[0])
print(tiger.__love_status) # AttributeError: 'Animal' object has no attribute '__love_status'
print(tiger.__getlove_status()) # AttributeError: 'Animal' object has no attribute '__getlove_status'.
```

^f2109a

类，有成员，成员分为：属性（变量）、方法（函数）
当用类创建对象，该对象自动具有该类的成员，包括变量&函数
第一个关键词就是self规定
**借助self.什么什么在函数体内调用任意类内的成员（属性、方法），一定别忘了self.，否咋报错未定义**
想想其他数据类型
	list(), dict(), tuple(), str(), int(), double(), etc.
	都是啊：
		my_list = list() : 用list类定义对象my_list
		那么，可以：my_list.append(), my_list.remove(), etc.

### 魔术方法
魔术方法的调用通常是隐式的，即由Python解释器在特定操作发生时自动调用，而不是直接由用户代码显式调用
魔术方法的显式调用：可以但是不建议，会被辞退
	另一个方法（可以是自定义也可以是另一个魔术方法）的返回值写例如：return self.\_\_str__()  
 1. \_\_str\_\_()
	 将对象转化成指定字符串并易于打印，如果直接打印则输出该对象的地址
	 调用：print(object)  or  print(str(object))
<details>
<summary>click to view __str__ </summary>
在Python中，`__str__` 是一个魔术方法（也称为特殊方法或双下方法），它定义了当调用内置函数 `str()` 或者在打印对象时，对象应该如何被转换成字符串。简单来说，`__str__` 方法用于提供一个对象的“非正式”或“可读性”字符串表示。

当你定义一个类时，可以重写 `__str__` 方法来返回一个字符串，这个字符串将被用来表示对象。例如：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# 创建对象
p = Person("Alice", 30)

# 打印对象
print(p)  # 输出: Person(name=Alice, age=30)
```

在这个例子中，当我们打印 `p` 对象时，`__str__` 方法被调用，并返回一个格式化的字符串。

</details>
2. \_\_repr\_\_()
	类似于\_\_str\_\_
	调用：print(repr(object))
<details>
<summary> click to view__repr__</summary>
与 `__repr__` 的区别

`__str__` 通常用于提供一个用户友好的字符串表示，而 `__repr__` 方法则用于提供一个更正式的、开发者友好的字符串表示，通常用于调试。如果一个类没有定义 `__str__` 方法，Python 会尝试调用 `__repr__` 方法。如果两者都没有定义，Python 会使用一个默认的表示，通常包含对象的类型和内存地址。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(str(p))  # 使用 str() 函数调用 __str__
print(repr(p))  # 使用 repr() 函数调用 __repr__
```

在这个例子中，`__str__` 提供了一个更易读的字符串，而 `__repr__` 提供了一个更详细的字符串，包括引号和类型信息。

使用场景

1. **用户友好性**：当你想让对象的字符串表示更易于理解时，可以重写 `__str__` 方法。
2. **调试**：`__repr__` 通常用于调试，因为它提供了一个更详细的字符串表示，但也可以通过 `__str__` 来提供一个更友好的调试信息。
3. **日志记录**：在日志记录中，使用 `__str__` 可以提供一个简洁的字符串表示，而 `__repr__` 可以提供更多的上下文信息。

注意事项

- 当你重写 `__str__` 方法时，确保返回的是一个字符串类型。
- 如果你的类需要同时支持 `__str__` 和 `__repr__`，通常建议两者都定义，以提供不同的表示形式。

通过重写 `__str__` 方法，你可以控制对象如何被转换成字符串，这在很多情况下都是非常有用的，特别是在需要将对象的信息以字符串形式展示给用户时。
</details>
3. \_\_add\_\_(self, other)
	调用：object1 + object2   eg : print(object1 + object2)
	定义
		参数：self, other
		内部：self.attribute_or_method, other.attribute_or_method
4. \_\_mul\_\_(self, other)
5. \_\_truediv\_\_(self, other)
6. \_\_eq\_\_(self, other)
	参数：self，other
	定义：当使用"\=="时候，自动调用该函数
7. \_\_lt\_\_(self, other)
8. \_\_gt\_\_(self, other)
9. \_\_call\_\_(self)
	使对象可以向函数一样被调用
	使用方法
		def \_\_call\_\_(self):
		# 代码块
		object()   # 调用
10. \_\_len__(self)
11. \_\_getitem__(self, index)
	自定义了用方括号访问下标的行为
12. \_\_setitem__(self, index, value)
	用方括号访问下标并赋值

### 私有成员
一般是通过公有成员进行访问来实现公有成员的功能，但是外部直接访问私有成员是不行的
定义：
	\_\_开头
	私有属性
		\_\_init__()括号中是参数（属性），既然是参数那就不要\_\_, 在self.\_\_private_attribute_name = attribute_or_pramameter_name 这里再定义私有属性，那么，self.\_\_private_attribute_name成为一个私有属性，其值为用类创建对象时给attribute_or_pramameter_name位置传的参数（值）
	私有方法
		直接定义就好

### 类的单继承
定义：class ChildrenClass(ParentClass):
特点：继承所有的公开成员（公开属性&公开方法）
初始化
	\_\_init__(self, its_prarameters_according_to_the_need_regardless_of_whether_it_occurs_in_the_ParentClass)
	super().\_\_init__(the_prameters_occurred_in_the_parentclass_except_self)
	self.the_prameters_didn't_occurred_in_the_parentclass = the_prameters_didn't_occurred_in_the_parentclass
	第二行其实就是一个函数调用，其实是省略了前面好多行self.的属性初始化
覆盖
	子类重写某个方法or属性，则会覆盖父类的相应方法

### 类的多继承
定义
	class ChildrenClass(MainParentClass, ViceParentClass):
初始化
	\_\_init__(self, its_prarameters_according_to_need_regardless_of_whether_it_occurs_in_the_ParentClasses)
	super().\_\_init__(the_prameters_occurred_in_the_MainParentClass_except_self)
	ViceParentClass.\_\_init(self, prameters_occurred_in_the_ViceParentClass)
	self.the_prameters_didn't_occurred_in_the_parentclass = the_prameters_didn't_occurred_in_the_parentclass
	其实super.()代表的就是MainParentClass
选择
	如果亲爹和继父有重复方法，则用亲爹的or亲爹从亲爷爷那里遗传的
	多个继父：谁在前谁关系亲
	不想用亲爹的而想用继父的：自己定义一个方法其返回值是继父的对应方法的返回值
		def call(self, number)
			return ViceParentClass.call(number)

## 模块与库
### 安装
[【pip 安装】国内 pip 镜像源换源方法以及 pip 基本操作_pip 源泉-CSDN博客](https://blog.csdn.net/weixin_57950978/article/details/142653359)
暂时换源：
```zsh
pip install <package_name> -i https://pypi.tuna.tsinghua.edu.cn/simple
```
换成清华源安装
永久还原：
```zsh
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
换完了

海龟编译器可以直接查看各种库……
pip安装最好！
### 语法
```python
	from libraay_name import item_name as given_name_by_me
```
eg:
```python
from random import randint
```
or
```python
from random import *
# 代表导入random库中的所有东西
```
or
```python
import library_name
library_name.item_name……
```
eg:
```python
import time
time.sleep(second_number)
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```
不知道库里面的东西是什么，or知道是个函数但不知道里面传的参数：鼠标悬浮在函数那里，有注释

import math
import os
import sys

### 模块module
模块：.py文件
在同一文件夹下
	直接import: 假设我现在有一个animal.py, 里面是[[Python#^f2109a|上面这个Animal类]]
```python
import animal
animal1 = animal.Animal(name = "男爵", age=10, sound="miaomiao", love_status=True, species="猫")
animal1.make_sound()
```
or
```python
from animal import Animal
animal1 = Animal(name = "男爵", age=10, sound="miaomiao", love_status=True, species="猫")
animal1.make_sound()
```
PS:
	第一个的 *.* 操作：当引入模块需要调用那个模块中的东西，可以将这个模块当作一个类，进而有 *.* 操作, 调用那个模块（文件）中的任何一个东西
	如果那个模块中还有一个变量 a = 8
	那么可以：print(animal.a)

### 库or包package
库（文件夹），里面有模块（文件）
#### 调用语法
##### 前提

python怎样知道这是一个包而不是一个普通文件夹：
假设现在有一个库（文件夹）叫做myPackage, 里面有三个模块（文件）叫做myModule1.py、myModule2.py、myModule3.py

那么，得在该文件夹下写一个__init__.py文件，里面什么都不用写就行，也可以写东西：
```python
__all__ = ['myModule1', 'myModule2']
```
代表：外部可以访问myModule1和myModule2，其他的模块如myModule3.py无法访问；如果没有__add__[...], 默认可以访问所有的模块

还有其他配置，你自己写库的时候可以自己查
##### 调用
假设现在有一个库（文件夹）叫做myPackage, 里面有一个模块（文件）叫做myModule.py, 里面有一个函数叫做my_func()
```python
from myPackage import myModule
myModule.my_func()
```
or
```python
import myPackage.myModule
myPackage.myModule.my_func()
```
or
```python
from myPackage.myModule import my_func
my_func()
```

python很好学的

## 杂项

- 假：
	0, "", None, \[], (), {}   空字符串、空数列、空的……
	函数return  <=> return None  <=> return 0  <=> ……


## 想了解的东西
服务器，端口,pip, anaconda， 换源

函数注释规范 7.30 1:21:40

