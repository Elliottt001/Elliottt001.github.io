YL
	函数注释规范 7.30 1:21:40
	PEP8规范：编程规范 第二期第一or二节
	
# 杂项

- in 关键词：用于可迭代对象
  eg：
```python
for i in range(1, 100)
if "hi" in word
```
- 假：
	0, "", None, \[], (), {}   空字符串、空数列、空的……
	函数return  <=> return None  <=> return 0  <=> ……

# 函数
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

修改：建议：用调用函数，返回值赋给要修改的那个变量
eg：
```python
y = 10
def func(y):
	#对y一番操作
	return y
y = func(y)
```

## 函数的多返回值
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
## 传参
关键词传参
	形式：形参名 = 实参值
位置传参
	按位置
混合使用
	可以，不建议，会被辞退
	如果位置的出现在关键词的后面，会报错
默认参数
	给默认参数的全放在不给默认参数的后面，否则会报错
函数作为参数传递
	形参那里写一个形参代表函数
	实参写函数名字！不能带括号，因为带了括号的意思是调用那个函数，则会报错（少参数）
	作用：
		回调
		可以通过改变传入的作为参数的函数（即：回调函数），灵活的改变我在这个函数中调用哪个函数（比函数的嵌套灵活）
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

# 数据容器
## 序列sequence
序列的切片
	定义：取出一个子序列
	语法：sequence_name\[start: stop: step]
		start : 省略默认0
		stop : 省略默认值为len(sequence_name)，前取后不取
		step : 省略默认1；负数：正负决定取值顺序（输出和读取从前到后or从后到前）；跳过stop-1个去取
		超限：不报错，到最后
	逻辑：读到start，看step（正负&大小），按他在序列里面找到stop
	应用
		倒序输出：print(序列名\[ : : -1]) : 如果前面两个都没填，则默认第一个是-1，最后一个是0
序列总结
	![[e3aa546b6378288f581c530b96df6b4.jpg]]
### 列表list
定义
	方式1：list_name = \["任意类型的数据", 123, 4 + 5j, \["甚至可以放列表", 5.3], None, True]
	方式2：list_name = list( "里面什么都能装")
访问
	list_name\[index] : index从0开始
	超过限制：报错
	index是负数：反向index：最后一个-1，倒数第二个-2，依此类推
	二维列表（列表·里面有列表）：list_name\[index1]\[index2]
修改
	list_name\[index] = new_item_which_can_be_any_type
点操作
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

循环遍历
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
PS: range()
	range(start, stop, step)
	start : 省略默认0
	stop : 前取后不取
	step : 省略默认1

### 元组tuple
跟list：
	定义：把\[]变成()即可
	不同：不能修改！所以.方法没有添加删除那几个
	相同：
		.index()
		.count()
		len()
元组的解包
```python
tuple_name = (item1, item2, item3) #多个item，可以是任意数据类型
a, b, c = tuple_name
# 现在，a是item1， 依此类推
```
作用
	保护数据，不可修改
函数的多返回值是个元组

tips
```python
my_tuple = (124, 'hello', ["a", "b", 89])
my_tuple[2][0] = 'A'
print(my_tuple)
# 被修改了
```
### 字符串string
跟list相同点
	.index()
	.count()
	len()
跟list不同
	不可直接修改！
	如果要修改，换新的字符串：见下，用.方法: new_str = ori_str.func(pra)
.方法（修改必须新字符串+调用函数）
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

## 另外两个
### 集合set
特点：
	不重复、无序、无索引index！
	可以修改！
定义：
	方法一：set_name = {item1, item2, item3, ......}
	方法二：set_name = set(item1, item2, item3, ......)
.方法
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

集合的运算(也是.方法)
	并集
		方法一：new_set = set1 | set2
		方法二：new_set = set1.union(set2)
	交集
		方法一：new_set = set1 & set2
		方法二：new_set = set1.intersection(set2)
	差集
		方法一：new_set = set1 - set2
		方法二：new_set = set1.difference(set2)

遍历
	只能用for：for item in set_name:
	while不行: 因为没有index

应用
给列表去重
	引用：爬去豆瓣排名前100的导演，去分析他们的合作关系之类的东西
```python
my_list = [……]
my_list = list(set(my_list))
```

### 字典dict
定义
	方法1：dict_name = {key1: value1, key2: value2, key3: value3 ……} ：元素为键值对
	方法2：dict_name = dict()
规范
	数据类型：除键不能是字典外，对key和value其他随便啥数据类型都行
	key要唯一：如果不唯一则后面覆盖前面（即按最后一个算）
访问
	查找：dict_name\[key_name]
	新增：dict_name\[new_key_name] = new_value
	修改：dict_name\[key_name] = new_value
		<!--可以通过这种方式修改高考分数：各省考试院对数据库重视程度不一样，有些存在漏洞，故可以修改-->
		<!--在ZJU，可以黑进教务网修改考试成绩，但是你的技术没达到那种超级tmd顶尖的水平，留痕是不可避免的，可溯源，抓到直接……-->
		<!--“我干过别的……嘿嘿嘿……”看看人家大学四年的技术水平，本科毕业直接工作，报价3000的爬虫小项目-->
		<!--by YL-->
	没有下标索引
.方法
	dict_name.pop(key_name)
		删除指定元素
	dict_name.clear()
		清空字典
	len(dict_name)
		元素个数