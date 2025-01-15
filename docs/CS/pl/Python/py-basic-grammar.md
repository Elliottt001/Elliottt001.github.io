## 语言元素

!!! info "指令和程序"

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

#### 逻辑运算符

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

### for循环

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



