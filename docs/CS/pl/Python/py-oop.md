## 面向对象编程

> &quot;把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。&quot;


OOP三步走：第一步定义类，第二步创建对象，第三步给对象发消息。

- 内置对象：只需要第三步
- 一些变量类型如 dict、str、tuple、set、list：需要二三步

### 类和对象

类是对象的蓝图和模板，而对象是类的实例。类是抽象的概念，而对象是具体的东西。

??? info "对象是可以接受消息的"

    什么是消息？是指对象之间通信的方式。通常表现为方法调用。当你调用一个对象的方法时，实际上是在向这个对象发送一条消息，请求它执行某个操作。

    例如：
    ```python
    print(my_dog.bark())  # 输出: Buddy says Woof!
    ```

    在这里，`bark()` 是一个方法调用，相当于向 `my_dog` 对象发送了一条消息：“请执行 `bark` 操作”。


    消息传递的特点

    - **封装性**：对象封装了数据和行为，外部只能通过消息（方法调用）与对象交互。
    - **多态性**：不同的对象可以对相同的消息做出不同的响应。例如，`Dog` 对象和 `Cat` 对象都可以响应 `speak` 消息，但它们的实现不同。
    - **动态性**：消息的接收和处理是动态的，可以在运行时决定。

    ---

    ??? info "多态性"
    不同的对象可以对相同的消息做出不同的响应。

        ```python
        class Dog:
            def speak(self):
                return "Woof!"

        class Cat:
            def speak(self):
                return "Meow!"

        # 发送相同的消息给不同的对象
        animals = [Dog(), Cat()]
        for animal in animals:
            print(animal.speak())
        ```

        输出：
        ```
        Woof!
        Meow!
        ```

    ??? info "消息传递与函数调用的区别"

        - **函数调用**：是面向过程编程的概念，直接调用函数来执行操作。
        - **消息传递**：是面向对象编程的概念，通过向对象发送消息来请求操作。

        例如：
        ```python
        # 面向过程
        def bark(dog_name):
            return f"{dog_name} says Woof!"

        print(bark("Buddy"))  # 输出: Buddy says Woof!

        # 面向对象
        class Dog:
            def __init__(self, name):
                self.name = name

            def bark(self):
                return f"{self.name} says Woof!"

        my_dog = Dog("Buddy")
        print(my_dog.bark())  # 输出: Buddy says Woof!
        ```

        在面向对象编程中，`my_dog.bark()` 是向 `my_dog` 对象发送消息，而在面向过程编程中，`bark("Buddy")` 是直接调用函数。


### 定义类

在Python中，可以使用`class`关键字加上类名来定义类，通过缩进我们可以确定类的代码块，就如同定义函数那样。在类的代码块中，我们需要写一些函数，我们说过类是一个抽象概念，那么这些函数就是我们对一类对象共同的动态特征的提取。写在类里面的函数我们通常称之为**方法**，方法就是对象的行为，也就是对象可以接收的消息。方法的第一个参数通常都是`self`，它代表了接收这个消息的对象本身。

```Python
class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')
```


在面向对象编程的世界里，程序中的**数据和操作数据的函数是一个逻辑上的整体**，我们称之为**对象**，**对象可以接收消息**，解决问题的方法就是**创建对象并向对象发出各种各样的消息**；通过消息传递，程序中的多个对象可以协同工作，这样就能构造出复杂的系统并解决现实中的问题。当然，面向对象编程的雏形还可以向前追溯到更早期的Simula语言，但这不是我们现在要讨论的重点。

### 创建和使用对象

在我们定义好一个类之后，可以使用构造器语法来创建对象，代码如下所示。

```Python
stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0> 
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0
```

在类的名字后跟上圆括号就是所谓的构造器语法，上面的代码创建了两个学生对象，一个赋值给变量`stu1`，一个复制给变量`stu2`。当我们用`print`函数打印`stu1`和`stu2`两个变量时，我们会看到输出了对象在内存中的地址（十六进制形式），跟我们用`id`函数查看对象标识获得的值是相同的。现在我们可以告诉大家，我们定义的变量其实保存的是一个对象在内存中的逻辑地址（位置），通过这个逻辑地址，我们就可以在内存中找到这个对象。所以`stu3 = stu2`这样的赋值语句并没有创建新的对象，只是用一个新的变量保存了已有对象的地址。

接下来，我们尝试给对象发消息，即调用对象的方法。刚才的`Student`类中我们定义了`study`和`play`两个方法，两个方法的第一个参数`self`代表了接收消息的学生对象，`study`方法的第二个参数是学习的课程名称。Python中，给对象发消息有两种方式，请看下面的代码。

```Python
# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)    # 学生正在玩游戏.
stu2.play()           # 学生正在玩游戏. 
```

### 初始化方法

大家可能已经注意到了，刚才我们创建的学生对象只有行为没有属性，如果要给学生对象定义属性，我们可以修改`Student`类，为其添加一个名为`__init__`的方法。在我们调用`Student`类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，然后通过自动执行`__init__`方法，完成对内存的初始化操作，也就是把数据放到内存空间中。所以我们可以通过给`Student`类添加`__init__`方法的方式为学生对象指定属性，同时完成对属性赋初始值的操作，正因如此，`__init__`方法通常也被称为初始化方法。

我们对上面的`Student`类稍作修改，给学生对象添加`name`（姓名）和`age`（年龄）两个属性。

```Python
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
```

修改刚才创建对象和给对象发消息的代码，重新执行一次，看看程序的执行结果有什么变化。

```Python
# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student('骆昊', 40)
stu2 = Student('王大锤', 15)
stu1.study('Python程序设计')    # 骆昊正在学习Python程序设计.
stu2.play()                    # 王大锤正在玩游戏.
```


### 属性和方法


| 类型         | 定义位置       | 访问方式       | 参数        | 用途                             |
|--------------|----------------|----------------|-------------|----------------------------------|
| **实例属性** | `__init__` 或其他实例方法 | 通过实例访问   | 无          | 描述对象的状态 / 属性                   |
| **类属性**   | 类中直接定义   | 通过类或实例访问 | 无，这就是一个普通的变量（有点类似全局变量）          | 属于类本身的属性，所有实例共享同一个类属性                 |
| **实例方法** | 类中定义       | 通过实例访问   | `self`（表示当前对象）      | 属于对象的方法，操作实例属性                     |
| **类方法**   | 类中定义，使用 `@classmethod` | 通过类或实例访问 | `cls` （表示当前类）      | 操作类属性或执行与类相关的操作   |
| **静态方法** | 类中定义，使用 `@staticmethod` | 通过类或实例访问 | 无，外界传入          | 与类和实例无关，实现与类相关的工具函数           |

---

```python
class Dog:
    species = "Canis familiaris"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

    def bark(self):  # 实例方法
        print(f"{self.name} is barking!")

    @classmethod
    def get_species(cls):  # 类方法
        return cls.species

    @staticmethod
    def is_valid_age(age):  # 静态方法
        return age > 0

# 测试
dog = Dog("Buddy", 3)
dog.bark()  # 输出: Buddy is barking!
print(Dog.get_species())  # 输出: Canis familiaris
print(Dog.is_valid_age(3))  # 输出: True
```


### 打印对象

上面我们通过`__init__`方法在创建对象时为对象绑定了属性并赋予了初始值。在Python中，以两个下划线`__`（读作“dunder”）开头和结尾的方法通常都是有特殊用途和意义的方法，我们一般称之为**魔术方法**或**魔法方法**。如果我们在打印对象的时候不希望看到对象的地址而是看到我们自定义的信息，可以通过在类中放置`__repr__`魔术方法来做到，**该方法返回的字符串就是用`print`函数打印对象的时候会显示的内容**，代码如下所示。

```Python
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
    
    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('骆昊', 40)
print(stu1)        # 骆昊: 40
students = [stu1, Student('李元芳', 36), Student('王大锤', 25)]
print(students)    # [骆昊: 40, 李元芳: 36, 王大锤: 25]
```



### 访问可见性问题

对于上面的代码，有C++、Java、C#等编程经验的程序员可能会问，我们给`Student`对象绑定的`name`和`age`属性到底具有怎样的访问权限（也称为可见性）。因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不允许外界访问，而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的消息。在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。

```Python
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()
```

但是，Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们。

```Python
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
```

习惯上，让属性名以单下划线开头来表示属性是受保护的（因为实在没有必要用双下划线命名私有成员），事实上，外界都仍然是可以访问的

### 封装

封装：&quot;隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口&quot;。我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，只需要给对象发送一个消息（调用方法）就可以执行方法中的代码，也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节（方法的内部视图）。

**示例**

定义一个类描述数字时钟。

参考答案：

```Python
from time import sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show(), end = "\r")
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```

定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。

参考答案：

```Python
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
```

### @property装饰器

!!! warning "warning"

    1. 变量 / 函数命名：@property 修饰的方法直接命名为相应变量的名字，将 `__init__` 中相应变量改为私有属性（名字前面加一个下划线），@<name>.setter 中 “name” 是与 @property 修饰的方法同名。


> 之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。

!!! success "理解"
    其实@property、getter、setter只是一种简单的习惯，不是什么高端的东西。

    目的是：

    - 通过@property（getter），使得**可以像使用属性一样使用这个方法**
    - 通过@method_name.setter，使得外界可以修改对象的属性值，从而实现“动态性”
    - 通过@method_name.deleter，使得外界可以通过 `del` 删除对象的属性值，从而实现“动态性”


`@property` 是 Python 中一个非常有用的装饰器，用于将一个方法转换为属性，使得你可以像访问属性一样访问方法，同时还可以添加额外的逻辑（如数据验证、计算属性等）。它的主要作用是提供一种更优雅的方式来管理类的属性访问。

1. 基本用法    
`@property` 通常用于定义“只读”属性，或者对属性的访问进行控制。以下是一个简单的例子：

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

# 使用
c = Circle(5)
print(c.diameter)  # 输出: 10
```

解释：
- `diameter` 是一个方法，但通过 `@property` 装饰后，可以像属性一样直接访问（`c.diameter`），而不需要调用方法（`c.diameter()`）。
- 这里 `diameter` 是一个只读属性，因为它没有定义对应的 setter。

---

2. 设置属性的值    
除了定义只读属性，`@property` 还可以与 setter 和 deleter 结合使用，实现对属性的赋值和删除操作。

示例：
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self.radius = value / 2

    @diameter.deleter
    def diameter(self):
        print("Deleting diameter")
        del self.radius

# 使用
c = Circle(5)
print(c.diameter)  # 输出: 10

c.diameter = 12  # 设置 diameter，会自动更新 radius
print(c.radius)  # 输出: 6

del c.diameter  # 删除 diameter，会触发 deleter
```

解释：
- `@diameter.setter`：定义了一个 setter 方法，允许通过 `c.diameter = value` 的方式设置 `diameter` 的值。
- `@diameter.deleter`：定义了一个 deleter 方法，允许通过 `del c.diameter` 的方式删除属性。
- 通过这些方法，你可以在属性赋值或删除时添加额外的逻辑（如数据验证）。

---

3. 数据验证    
`@property` 的一个常见用途是对属性赋值进行验证。例如，确保半径不能为负数：

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# 使用
c = Circle(5)
print(c.radius)  # 输出: 5

c.radius = -10  # 抛出 ValueError: Radius cannot be negative
```

解释：    

- 这里 `radius` 被定义为一个属性，通过 setter 方法确保赋值的合法性。
- 注意：在 `__init__` 中直接赋值 `self.radius` 会触发 setter 方法，因此可以确保初始值也是合法的。

---

4. 计算属性    
`@property` 还可以用于定义计算属性，即属性的值是根据其他属性动态计算的。

示例：
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

# 使用
r = Rectangle(4, 5)
print(r.area)  # 输出: 20
```

解释：

- `area` 是一个计算属性，它的值是根据 `width` 和 `height` 动态计算的。
- 每次访问 `r.area` 时，都会重新计算。

---

5. 优点

- **封装性**：通过 `@property`，你可以隐藏内部实现细节，只暴露必要的接口。
- **灵活性**：可以在属性访问、赋值和删除时添加额外的逻辑。
- **兼容性**：可以将已有的方法转换为属性，而不需要修改外部调用代码。

---

6. 注意事项

- **性能**：如果 `@property` 方法的计算量很大，频繁访问可能会导致性能问题。在这种情况下，可以考虑缓存结果。
- **只读属性**：如果没有定义 setter，那么属性是只读的，尝试赋值会抛出 `AttributeError`。

??? info "my try"
    ```python
    class Article():
        language = "Chinese"
        def __init__(self, reads, likes, form, theme, platform):
            self._reads = reads
            self._likes = likes
            self.form = form
            self.theme = theme
            self.platform = platform

        @property
        def proportion_of_likes(self):
            return self._likes / self._reads
        
        @property
        def judge_form(self):
            forms = ["video", "character", "film"]
            if self.form in forms:
                index = forms.index(self.form)
            else:
                forms.append(self.form)
                index = forms.index(self.form)
            return index
        
        @property
        def likes(self):
            return self._likes
        
        @likes.setter
        def likes(self, cnt):
            if cnt < 0:
                raise ValueError
            else:
                self._likes = cnt


    class xhs(Article):
        def __init__(self, reads, likes, form, theme, platform = "xhs"):
            super().__init__(reads, likes, form, theme, platform)

    class gzh(Article):
        def __init__(self, reads, likes, form, theme, platform = "wechat"):
            super().__init__(reads, likes, form, theme, platform)


    art1 = xhs(5, 3, "video", "fun", "xhs")
    art2 = gzh(10, 3, "character", "cs", "wechat")
    art3 = gzh(14, 5, "hhh", "hhh", "wechat")

    print(art3.judge_form)
    print(art2.proportion_of_likes)
    print(art1.proportion_of_likes)
    art1.likes = 2
    print(art1.proportion_of_likes)
    ```


```Python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
```

### \_\_slots\_\_魔法

我们讲到这里，不知道大家是否已经意识到，Python是一门[动态语言](https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80)。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义\_\_slots\_\_变量来进行限定。需要注意的是\_\_slots\_\_的限定只对当前类的对象生效，对子类并不起任何作用。

```Python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
```

### 静态方法和类方法

之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。

```Python
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()
```

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。

```Python
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```


使用staticmethod装饰器声明某方法是某类的静态方法，如果要声明类方法，可以使用classmethod装饰器。可以直接使用 `类名.方法名` 的方式来调用静态方法和类方法，二者的区别在于，类方法的第一个参数是类对象本身 `cls`，而静态方法则没有这个参数。

简单的总结一下，对象方法、类方法、静态方法都可以通过类名.方法名的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。

### 类之间的关系

简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。

我们可以使用一种叫做[UML](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E5%BB%BA%E6%A8%A1%E8%AF%AD%E8%A8%80)（统一建模语言）的东西来进行面向对象建模，其中一项重要的工作就是把类和类之间的关系用标准化的图形符号描述出来。关于UML我们在这里不做详细的介绍，有兴趣的读者可以自行阅读[《UML面向对象设计基础》](https://e.jd.com/30392949.html)一书。

![](./res/uml-components.png)

![](./res/uml-example.png)

利用类之间的这些关系，我们可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，这些都是实现代码复用的重要手段。复用现有的代码不仅可以减少开发的工作量，也有利于代码的管理和维护，这是我们在日常工作中都会使用到的技术手段。

### 继承和多态

继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类。如果定义一个类的时候没有指定它的父类是谁，那么默认的父类是 `object` 类。`object` 类是Python中的顶级类，这也就意味着所有的类都是它的子类，要么直接继承它，要么间接继承它。Python语言允许多重继承，也就是说一个类可以有一个或多个父类。

在子类的初始化方法中，我们可以通过 `super().__init__()` 来调用父类初始化方法，`super` 函数是Python内置函数中专门为获取当前对象的父类对象而设计的。从上面的代码可以看出，子类除了可以通过继承得到父类提供的属性和方法外，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力。

在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，也叫做“里氏替换原则”（Liskov Substitution Principle）。

!!! warning "warning"

    1. 子类的 `super().__init__()` 的参数顺序和数量一定要与父类的 `__init__()` 方法完全一致（除self）
    
    2. 带不带self：，每一个（子类 & 父类） `__init__()` 都带，子类的 `super().__init__()` 不带

```Python
class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()
```

子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

```Python
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
```

在上面的代码中，我们将`Pet`类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

子类继承父类的方法后，还可以对方法进行重写（重新实现该方法），不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。多态是面向对象编程中最精髓的部分，当然也是对初学者来说最难以理解和灵活运用的部分，我们会在下一节课中用专门的例子来讲解多态这个知识点。

### 示例

示例1：奥特曼打小怪兽。

```Python
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击

        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()
```
案例2：扑克游戏。

> **说明**：简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将52张牌发到4个玩家的手上，每个玩家手上有13张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。

使用面向对象编程方法，首先需要从问题的需求中找到对象并抽象出对应的类，此外还要找到对象的属性和行为。当然，这件事情并不是特别困难，我们可以从需求的描述中找出名词和动词，名词通常就是对象或者是对象的属性，而动词通常是对象的行为。扑克游戏中至少应该有三类对象，分别是牌、扑克和玩家，牌、扑克、玩家三个类也并不是孤立的。类和类之间的关系可以粗略的分为**is-a关系（继承）**、**has-a关系（关联）**和**use-a关系（依赖）**。很显然扑克和牌是has-a关系，因为一副扑克有（has-a）52张牌；玩家和牌之间不仅有关联关系还有依赖关系，因为玩家手上有（has-a）牌而且玩家使用了（use-a）牌。

牌的属性显而易见，有花色和点数。我们可以用0到3的四个数字来代表四种不同的花色，但是这样的代码可读性会非常糟糕，因为我们并不知道黑桃、红心、草花、方块跟0到3的数字的对应关系。如果一个变量的取值只有有限多个选项，我们可以使用枚举。与C、Java等语言不同的是，Python中没有声明枚举类型的关键字，但是可以通过继承`enum`模块的`Enum`类来创建枚举类型，代码如下所示。

```Python
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
```

通过上面的代码可以看出，定义枚举类型其实就是定义符号常量，如`SPADE`、`HEART`等。每个符号常量都有与之对应的值，这样表示黑桃就可以不用数字`0`，而是用`Suite.SPADE`；同理，表示方块可以不用数字`3`， 而是用`Suite.DIAMOND`。注意，使用符号常量肯定是优于使用字面常量的，因为能够读懂英文就能理解符号常量的含义，代码的可读性会提升很多。Python中的枚举类型是可迭代类型，简单的说就是可以将枚举类型放到`for-in`循环中，依次取出每一个符号常量及其对应的值，如下所示。

```Python
for suite in Suite:
    print(f'{suite}: {suite.value}')
```

接下来我们可以定义牌类。

```Python
class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'
```

可以通过下面的代码来测试下`Card`类。

```Python
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)    # ♠5 ♥K
```

接下来我们定义扑克类。

```Python
import random


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
```

可以通过下面的代码来测试下`Poker`类。

```Python
poker = Poker()
poker.shuffle()
print(poker.cards)
```

定义玩家类。

```Python
class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()
```

创建四个玩家并将牌发到玩家的手上。

```Python
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)
```

执行上面的代码会在`player.arrange()`那里出现异常，因为`Player`的`arrange`方法使用了列表的`sort`对玩家手上的牌进行排序，排序需要比较两个`Card`对象的大小，而`<`运算符又不能直接作用于`Card`类型，所以就出现了`TypeError`异常，异常消息为：`'<' not supported between instances of 'Card' and 'Card'`。

为了解决这个问题，我们可以对`Card`类的代码稍作修改，使得两个`Card`对象可以直接用`<`进行大小的比较。这里用到技术叫**运算符重载**，Python中要实现对`<`运算符的重载，需要在类中添加一个名为`__lt__`的魔术方法。很显然，魔术方法`__lt__`中的`lt`是英文单词“less than”的缩写，以此类推，魔术方法`__gt__`对应`>`运算符，魔术方法`__le__`对应`<=`运算符，`__ge__`对应`>=`运算符，`__eq__`对应`==`运算符，`__ne__`对应`!=`运算符。

修改后的`Card`类代码如下所示。

```Python
class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    def __lt__(self, other):
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value
```

>**说明：** 大家可以尝试在上面代码的基础上写一个简单的扑克游戏，如21点游戏（Black Jack），游戏的规则可以自己在网上找一找。



案例3：工资结算系统。

> **要求**：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定15000元；程序员按工作时间（以小时为单位）支付月薪，每小时200元；销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。

通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为，那么我们可以先设计一个名为`Employee`的父类，再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。很显然，后续的代码不会创建`Employee` 类的对象，因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类。Python中没有定义抽象类的关键字，但是可以通过`abc`模块中名为`ABCMeta` 的元类来定义抽象类。关于元类的知识，后面的课程中会有专门的讲解，这里不用太纠结这个概念，记住用法即可。

```Python
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass
```

在上面的员工类中，有一个名为`get_salary`的方法用于结算月薪，但是由于还没有确定是哪一类员工，所以结算月薪虽然是员工的公共行为但这里却没有办法实现。对于暂时无法实现的方法，我们可以使用`abstractmethod`装饰器将其声明为抽象方法，所谓**抽象方法就是只有声明没有实现的方法**，**声明这个方法是为了让子类去重写这个方法**。接下来的代码展示了如何从员工类派生出部门经理、程序员、销售员这三个子类以及子类如何重写父类的抽象方法。

```Python
class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05
```

上面的`Manager`、`Programmer`、`Salesman`三个类都继承自`Employee`，三个类都分别重写了`get_salary`方法。**重写就是子类对父类已有的方法重新做出实现**。相信大家已经注意到了，三个子类中的`get_salary`各不相同，所以这个方法在程序运行时会产生**多态行为**，多态简单的说就是**调用相同的方法**，**不同的子类对象做不同的事情**。

我们通过下面的代码来完成这个工资结算系统，由于程序员和销售员需要分别录入本月的工作时间和销售额，所以在下面的代码中我们使用了Python内置的`isinstance`函数来判断员工对象的类型。我们之前讲过的`type`函数也能识别对象的类型，但是`isinstance`函数更加强大，因为它可以判断出一个对象是不是某个继承结构下的子类型，你可以简答的理解为`type`函数是对对象类型的精准匹配，而`isinstance`函数是对对象类型的模糊匹配。

```Python
emps = [
    Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), 
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽'),
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')
```

### 简单的总结

面向对象的编程思想非常的好，也符合人类的正常思维习惯，但是要想灵活运用面向对象编程中的抽象、封装、继承、多态需要长时间的积累和沉淀，这件事情无法一蹴而就，属于“路漫漫其修远兮，吾将上下而求索”的东西。