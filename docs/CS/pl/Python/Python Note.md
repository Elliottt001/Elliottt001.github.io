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

关键字：`if` `else` `elif`

Tips：

- 注意缩进：连续的代码如果又保持了相同的缩进那么它们属于同一个代码块。

- 建议使用4个空格，不要使用Tab 

- 能使用扁平化的结构时就不要使用嵌套。


## 循环结构

### for-in循环

**场景：** 明确知道循环执行的次数或者要对一个容器进行迭代

range函数：`range(start, stop, step)`：
- start 不写默认1
- stop 必写
- step 不写默认0，step 是负数则要求 start > stop

### while循环

不知道具体循环次数，原理：通过一个能够产生或转换出`bool`值的表达式来控制循环

`break` `continue`

## 函数

### 定义函数

`def`关键字

### 函数的参数

函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持[函数的重载](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0%E9%87%8D%E8%BD%BD)，因为我们在定义一个函数的时候可以让它有多种不同的使用方式。

例如：

```Python
from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
```

在不确定参数个数的时候，我们可以使用可变参数，代码如下。

```Python
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
```

**`*args` 和 `**kwargs`**

| 特性            | `*args`                          | `**kwargs`                      |
|-----------------|----------------------------------|---------------------------------|
| 参数类型        | 位置参数（无键值对）             | 关键字参数（键值对）            |
| 打包形式        | 打包成元组（tuple）              | 打包成字典（dict）              |
| 使用场景        | 处理可变数量的位置参数           | 处理可变数量的关键字参数         |
| 示例            | `func(1, 2, 3)`                  | `func(a=1, b=2, c=3)`           |



??? info "关于 `*args` 和 `**kwargs`"

	1. 什么是 `*args`？
	- `*args` 允许函数接受**任意数量的位置参数**。
	- 这些参数会被打包成一个**元组（tuple）**，传递给函数。
	- 可以通过遍历 `args` 来处理这些参数。

	3. 上述代码示例调用
	```python
	print(add(10, 20, 30, 40))   # 输出: 100
	print(add(5))                # 输出: 5
	print(add())                 # 输出: 0
	```

	5. 与其他参数结合使用
	`*args` 可以与其他参数一起使用，必须放在它们之后。例如：
	```python
	def greet(name, *args):
		print(f"Hello, {name}!")
		print("Additional arguments:", args)

	greet("Alice", 1, 2, 3)
	```
	在 `*args` 之后定义的参数必须通过关键字传递。

	示例
	```python
	def func(a, b, *args, c, d):
		print(a, b, args, c, d)

	func(1, 2, 3, 4, c=5, d=6)  # c 和 d 必须通过关键字传递
	```


	什么是 `**kwargs`？

	- `**kwargs` 允许函数接受任意数量的**关键字参数（关键词传参）**（即键值对）。
	- 这些参数会被打包成一个**字典（dict）**，传递给函数。
	- `kwargs` 是约定俗成的名称，你可以使用其他名称，但 `**` 是必须的。

	示例代码
	```python
	def print_info(**kwargs):
		for key, value in kwargs.items():
			print(f"{key}: {value}")

	print_info(name="Alice", age=30, city="New York")
	```
	输出：
	```
	name: Alice
	age: 30
	city: New York
	```

	特点

	- `**kwargs` 将传入的关键字参数打包成一个字典。
	- 如果没有传递关键字参数，`kwargs` 是一个空字典。

	---


	3. `*args` 和 `**kwargs` 的结合使用：必须遵循以下顺序：
		1. 标准参数（固定参数）。
		2. `*args`（可变位置参数）。
		3. `**kwargs`（可变关键字参数）。


**解包参数`*` 和 `**`**


| **符号** | **用途**                          | **示例**                                      |
|----------|----------------------------------|-----------------------------------------------|
| `*`      | **函数定义**：接收可变位置参数    | `def func(*args):` → `args` 是元组            |
|          | **函数调用**：解包可迭代对象      | `func(*[1, 2, 3])` → 相当于 `func(1, 2, 3)`   |
|          | **赋值**：扩展解包                | `a, *b = [1, 2, 3]` → `a=1`, `b=[2, 3]`       |
| `**`     | **函数定义**：接收可变关键字参数  | `def func(**kwargs):` → `kwargs` 是字典       |
|          | **函数调用**：解包字典            | `func(**{"a": 1, "b": 2})` → 相当于 `func(a=1, b=2)` |
|          | **字典合并**：合并多个字典        | `{**dict1, **dict2}` → 合并两个字典           |
| `*` 和 `**` 结合 | **函数定义**：同时接收可变位置和关键字参数 | `def func(a, *args, **kwargs):` |
|          | **函数调用**：同时解包可迭代对象和字典 | `func(*[1, 2], **{"c": 3})` → 相当于 `func(1, 2, c=3)` |

> 与指针有异曲同工之妙：定义时代表变量身份，调用时代表对变量操作

??? info "`*` 和 `**`"

	- `*` 可以用于解包**可迭代对象**（如列表、元组）为位置参数。
	- `**` 可以用于解包**字典**为关键字参数。

	示例
	```python
	def func(a, b, c):
		print(a, b, c)

	# 解包列表
	args = [1, 2, 3]
	func(*args)  # 相当于 func(1, 2, 3)

	# 解包字典
	kwargs = {"a": 1, "b": 2, "c": 3}
	func(**kwargs)  # 相当于 func(a=1, b=2, c=3)
	```


**仅位置参数**

`/` 就是放在参数表中的一个符号，代表**它之前的**参数必须通过位置传递，他不是形参。

示例
```python
def func(a, b, /, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)  # a 和 b 必须通过位置传递
```


- 关键词传参：形参名 = 实参值

- 位置传参：按位置

- 混合使用
	- 可以，不建议，会被辞退
	- 如果位置的出现在关键词的后面，会报错

- 默认参数：给默认参数的全放在不给默认参数的后面，否则会报错


### 用模块管理函数

在同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义。

解决方案：Python中每个文件就代表了一个模块（module），在不同的模块中可以有同名的函数，在使用函数的时候我们通过`import`关键字导入指定的模块就可以区分。代码如下所示。


```Python
# module1.py
def foo():
    print('hello, world!')
```

```Python
# module2.py
def foo():
    print('goodbye, world!')
```

```Python
# test.py
from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()
```

```Python
# test.py
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
```

但是，这样会导致覆盖


```Python
# test.py
from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()
```

使用 `if __name__ == '__main__'`

> 如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是 &quot;\_\_main\_\_&quot;。


```Python
# module3.py
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```



```Python
# test.py
import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
```


例题：实现判断一个数是不是回文数的函数。

```Python
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
```


### 变量的作用域

```Python
def foo():
    b = 'hello'
    # 可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()
    # print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
```

对于`foo`函数内部的`bar`函数来说，变量`b`属于嵌套作用域，在`bar`函数中我们是可以访问到它的。

查找一个变量时会按照 LEGB规则，即 **“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”** 的顺序进行搜索，

- 内置作用域：关键字，不要覆盖
- 嵌套作用域：函数内部定义的函数（即嵌套函数）可以访问其外层函数（非全局作用域）的作用域中的变量。

再看看下面这段代码，我们希望通过函数调用修改全局变量`a`的值，但实际上下面的代码是做不到的。

```Python
def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
```

在调用`foo`函数后，我们发现`a`的值仍然是100，这是因为当我们在函数`foo`中写`a = 200`的时候，是重新定义了一个名字为`a`的局部变量，它跟全局作用域的`a`并不是同一个变量，因为局部作用域中有了自己的变量`a`，因此`foo`函数不再搜索全局作用域中的`a`。如果我们希望在`foo`函数中修改全局作用域中的`a`，代码如下所示。

```Python
def foo():
    global a  # 用global关键字声明他是全局变量并在后面修改
    a = 200
    print(a)  # 200

if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
```
如果全局作用域中没有 `a`，那么下面一行的代码就会定义变量 `a` 并将其置于全局作用域。
```python
def outer():
    x = 10  # 外层函数的局部变量

    def inner():
        nonlocal x  # 声明 x 是外层作用域的变量
        x = 20      # 修改外层作用域的变量
        print("Inner:", x)

    inner()
    print("Outer:", x)
outer()

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


### 匿名函数

**匿名函数（Anonymous Function）** 是一种没有名字的函数，通常用于简化代码，尤其是在需要传递简单函数作为参数的场景。在 Python 中，匿名函数通过 `lambda` 关键字定义，因此也被称为 **lambda 函数**。


语法

```python
lambda 参数1, 参数2, ... : 表达式
```
- **参数**：匿名函数可以接受任意数量的参数。
- **表达式**：匿名函数的返回值是表达式的结果，不需要 `return` 语句。

---

匿名函数的示例

示例 1：基本用法
```python
# 普通函数
def add(x, y):
    return x + y

# 匿名函数
add_lambda = lambda x, y: x + y

print(add(2, 3))        # 输出: 5
print(add_lambda(2, 3)) # 输出: 5
```

---

示例 2：结合内置函数使用

匿名函数常用于 `map()`、`filter()`、`sorted()` 等需要函数作为参数的场景。

1. **`map()`**：对可迭代对象的每个元素应用函数。
   ```python
   numbers = [1, 2, 3, 4]
   squared = map(lambda x: x ** 2, numbers)
   print(list(squared))  # 输出: [1, 4, 9, 16]
   ```

2. **`filter()`**：过滤可迭代对象中满足条件的元素。
   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   evens = filter(lambda x: x % 2 == 0, numbers)
   print(list(evens))  # 输出: [2, 4, 6]
   ```

3. **`sorted()`**：根据指定规则排序。
   ```python
   points = [(1, 2), (3, 1), (5, 0)]
   sorted_points = sorted(points, key=lambda p: p[1])  # 按第二个元素排序
   print(sorted_points)  # 输出: [(5, 0), (3, 1), (1, 2)]
   ```

---

示例 3：作为函数返回值，用于创建动态行为。
```python
def create_multiplier(n):
    return lambda x: x * n

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15
```

---

示例 4：简化条件逻辑
匿名函数可以用于简化简单的条件逻辑。
```python
# 普通函数
def check_even(x):
    return "Even" if x % 2 == 0 else "Odd"

# 匿名函数
check_even_lambda = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(4))        # 输出: Even
print(check_even_lambda(4)) # 输出: Even
```

---

优点

1. **代码简洁**：适合定义简单的逻辑，避免定义完整的函数。
2. **临时使用**：适合一次性使用的场景，减少代码量。
3. **灵活性**：可以作为参数传递给高阶函数（如 `map()`、`filter()` 等）。

---

局限性

1. **功能受限**：匿名函数只能包含一个表达式，不能包含复杂的逻辑或多行代码。
2. **可读性差**：过度使用匿名函数可能降低代码的可读性。
3. **调试困难**：匿名函数没有函数名，调试时可能不如普通函数方便。


全局变量可以在函数体内访问，但是内部不能修改！

如果尝试修改，会报错

如果想要修改：
	用global关键字，但不建议
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

















## 字符串和常用数据结构

### 使用字符串

第二次世界大战促使了现代电子计算机的诞生，最初计算机被应用于导弹弹道的计算，而在计算机诞生后的很多年时间里，计算机处理的信息基本上都是数值型的信息。世界上的第一台电子计算机叫ENIAC（电子数值积分计算机），诞生于美国的宾夕法尼亚大学，每秒钟能够完成约5000次浮点运算。随着时间的推移，虽然数值运算仍然是计算机日常工作中最为重要的事情之一，但是今天的计算机处理得更多的数据可能都是以文本的方式存在的，如果我们希望通过Python程序操作这些文本信息，就必须要先了解字符串类型以及与它相关的知识。

所谓**字符串**，就是由零个或多个字符组成的有限序列，一般记为![$${\displaystyle s=a_{1}a_{2}\dots a_{n}(0\leq n \leq \infty)}$$](./res/formula_5.png)。在Python程序中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。

```Python
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
```

可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，例如：`\n`不是代表反斜杠和字符n，而是表示换行；而`\t`也不是代表反斜杠和字符t，而是表示制表符。所以如果想在字符串中表示`'`要写成`\'`，同理想表示`\`要写成`\\`。可以运行下面的代码看看会输出什么。

```Python
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')
```

在`\`后面还可以跟一个八进制或者十六进制数来表示字符，例如`\141`和`\x61`都代表小写字母`a`，前者是八进制的表示法，后者是十六进制的表示法。也可以在`\`后面跟Unicode字符编码来表示字符，例如`\u9a86\u660a`代表的是中文“骆昊”。运行下面的代码，看看输出了什么。

```Python
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
```

如果不希望字符串中的`\`表示转义，我们可以通过在字符串的最前面加上字母`r`来加以说明，再看看下面的代码又会输出什么。

```Python
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
```

Python为字符串类型提供了非常丰富的运算符，我们可以使用`+`运算符来实现字符串的拼接，可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是否包含另外一个字符串（成员运算），我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符（切片运算），代码如下所示。

```Python
s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
```

在Python中，我们还可以通过一系列的方法来完成对字符串的处理，代码如下所示。

```Python
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
```

我们之前讲过，可以用下面的方式来格式化输出字符串。

```Python
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
```

当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。

```Python
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
```

Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母`f`，我们可以使用下面的语法糖来简化上面的代码。

```Python
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
```

除了字符串，Python还内置了多种类型的数据结构，如果要在程序中保存和操作数据，绝大多数时候可以利用现有的数据结构来实现，最常用的包括列表、元组、集合和字典。

### 使用列表

不知道大家是否注意到，刚才我们讲到的字符串类型（`str`）和之前我们讲到的数值类型（`int`和`float`）有一些区别。数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法。接下来我们要介绍的列表（`list`），也是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在`[]`中，多个元素用`,`进行分隔，可以使用`for`循环对列表元素进行遍历，也可以使用`[]`或`[:]`运算符取出列表中的一个或多个元素。

下面的代码演示了如何定义列表、如何遍历列表以及列表的下标运算。

```Python
list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
```

下面的代码演示了如何向列表中添加元素以及如何从列表中移除元素。

```Python
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []
```

和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，代码如下所示。

```Python
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
```

下面的代码实现了对列表的排序操作。

```Python
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
```

### 生成式和生成器

我们还可以使用列表的生成式语法来创建列表，代码如下所示。

```Python
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
```

除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过`yield`关键字将一个普通函数改造成生成器函数。下面的代码演示了如何实现一个生成[斐波拉切数列](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)的生成器。所谓斐波拉切数列可以通过下面[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)的方法来进行定义：

![$${\displaystyle F_{0}=0}$$](./res/formula_6.png)

![$${\displaystyle F_{1}=1}$$](./res/formula_7.png)

![$${\displaystyle F_{n}=F_{n-1}+F_{n-2}}({n}\geq{2})$$](./res/formula_8.png)

![](./res/fibonacci-blocks.png)

```Python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
```

### 使用元组

Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。下面的代码演示了如何定义和使用元组。

```Python
# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
```

这里有一个非常值得探讨的问题，我们已经有了列表这种数据结构，为什么还需要元组这样的类型呢？

1. 元组中的元素是无法修改的，事实上我们在项目中尤其是[多线程](https://zh.wikipedia.org/zh-hans/%E5%A4%9A%E7%BA%BF%E7%A8%8B)环境（后面会讲到）中可能更喜欢使用的是那些不变对象（一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。
2. 元组在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，这个很容易做到。我们也可以在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间，下图是我的macOS系统上测试的结果。

![](./res/ipython-timeit.png)

### 使用集合

Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

![](./res/python-set.png)

可以按照下面代码所示的方式来创建和使用集合。

```Python
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
```

向集合添加元素和从集合删除元素。

```Python
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)
```

集合的成员、交集、并集、差集等运算。

```Python
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
```

> **说明：** Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，例如`&`运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。

### 使用字典

字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。下面的代码演示了如何定义和使用字典。

```Python
# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)
```

### 练习

#### 练习1：在屏幕上显示跑马灯文字。

参考答案：

```Python
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
```

#### 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

参考答案：

```Python
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
```

#### 练习3：设计一个函数返回给定文件名的后缀名。

参考答案：

```Python
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
```

#### 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

参考答案：

```Python
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
```

#### 练习5：计算指定的年月日是这一年的第几天。

参考答案：

```Python
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()
```

#### 练习6：打印[杨辉三角](https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2)。

参考答案：

```Python
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
```

### 综合案例

#### 案例1：双色球选号。

```Python
from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
```

> **说明：** 上面使用random模块的sample函数来实现从列表中选择不重复的n个元素。

#### 综合案例2：[约瑟夫环问题](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98)。

```Python
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()

```

#### 综合案例3：[井字棋](https://zh.wikipedia.org/wiki/%E4%BA%95%E5%AD%97%E6%A3%8B)游戏。

```Python
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
```

>**说明：** 最后这个案例来自[《Python编程快速上手:让繁琐工作自动化》](https://item.jd.com/11943853.html)一书（这本书对有编程基础想迅速使用Python将日常工作自动化的人来说还是不错的选择），对代码做了一点点的调整。




















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

