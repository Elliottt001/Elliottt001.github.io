
## csv文件与csv库

### **1. 读取 CSV 文件**
#### **(1) `csv.reader`**
- **功能**：逐行读取 CSV 文件，返回一个 `csv.reader` 对象，该对象是一个迭代器，每次迭代返回一行数据（以列表形式）。
- **语法**：
    ```python
    csv.reader(csvfile, dialect='excel', **fmtparams)
    ```
- **参数**：
    - `csvfile`：文件对象或任何支持迭代的对象。
    - `dialect`：指定 CSV 文件的格式（如 `excel`、`excel-tab` 等）。
    - `fmtparams`：其他格式化参数，如 `delimiter`（分隔符）、`quotechar`（引用符）等。

!!! info "方言"

    在 Python 的 `csv` 库中，**方言（Dialect）** 是指一组用于定义 CSV 文件格式的参数。

    **方言** 将这些格式参数封装在一起，使得在处理不同格式的 CSV 文件时，可以更方便地统一管理这些参数。

    **2. 方言的参数**
    方言由一组参数定义，常用的参数包括：
    - **`delimiter`**：字段分隔符，默认为逗号 `,`。
    - **`quotechar`**：引用符，用于括起包含特殊字符的字段，默认为双引号 `"`。
    - **`quoting`**：引用模式，决定何时使用引用符。可选值：
    - `csv.QUOTE_MINIMAL`：仅在必要时使用引用符（默认）。
    - `csv.QUOTE_ALL`：所有字段都用引用符括起。
    - `csv.QUOTE_NONNUMERIC`：所有非数字字段都用引用符括起。
    - `csv.QUOTE_NONE`：不使用引用符。
    - **`lineterminator`**：行结束符，默认为 `\r\n`。
    - **`escapechar`**：转义符，用于转义特殊字符，默认为 `None`。
    - **`doublequote`**：是否双写引用符，默认为 `True`。


- **示例**：
    ```python
    import csv

    with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    ```

#### **(2) `csv.DictReader`**
- **功能**：将 CSV 文件的每一行转换为字典形式，字典的键是表头（第一行的列名），值是对应的字段值。
- **语法**：
    ```python
    csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', **fmtparams)
    ```
- **参数**：
    - `csvfile`：文件对象或任何支持迭代的对象。
    - `fieldnames`：指定表头（列名）。如果未指定，默认使用第一行作为表头。
    - `restkey`：如果某行的字段多于表头，多余的字段会以 `restkey` 为键存储。
    - `restval`：如果某行的字段少于表头，缺少的字段会以 `restval` 为值填充。
- **示例**：
    ```python
    import csv

    with open('scores.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for data_list in reader:
            print(reader.line_num, end='\t')
            for elem in data_list:
                print(elem, end='\t')
            print()
        ```

---

### **2. 写入 CSV 文件**
#### **(1) `csv.writer`**
- **功能**：将数据逐行写入 CSV 文件。
- **语法**：
    ```python
    csv.writer(csvfile, dialect='excel', **fmtparams)
    ```
- **返回值**：返回一个 `csv.writer` 对象。
- **参数**：
    - `csvfile`：文件对象。
    - `dialect`：指定 CSV 文件的格式。
    - `fmtparams`：其他格式化参数，如 `delimiter`、`quotechar` 等。
- **示例**：
    ```python
    import csv

    data = [
        ['name', 'age', 'city'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles']
    ]

    with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    ```
    ```python
    import csv
    import random

    with open('scores.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名', '语文', '数学', '英语'])
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        for name in names:
            scores = [random.randrange(50, 101) for _ in range(3)]
            scores.insert(0, name)
            writer.writerow(scores)
        ```

#### **(2) `csv.DictWriter`**
- **功能**：将字典形式的数据写入 CSV 文件，需要指定表头。
- **语法**：
    ```python
    csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', **fmtparams)
    ```
- **参数**：
    - `csvfile`：文件对象。
    - `fieldnames`：表头（列名）。
    - `restval`：如果某行的字段少于表头，缺少的字段会以 `restval` 为值填充。
    - `extrasaction`：如果某行的字段多于表头，`extrasaction` 决定如何处理（`raise` 抛出异常，`ignore` 忽略多余字段）。
- **示例**：
    ```python
    import csv

    data = [
        {'name': 'Alice', 'age': '30', 'city': 'New York'},
        {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'}
    ]

    headers = ['name', 'age', 'city']

    with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # 写入表头
        for row in data:
            writer.writerow(row)
    ```

---

### **3. 其他功能**
#### **(1) `csv.register_dialect`**
- **功能**：注册一个自定义的 CSV 格式（方言）。
- **语法**：
    ```python
    csv.register_dialect(name, **fmtparams)
    ```
- **参数**：
    - `name`：方言的名称。
    - `fmtparams`：格式化参数，如 `delimiter`、`quotechar` 等。
- **示例**：
    ```python
    import csv

    csv.register_dialect('my_dialect', delimiter='|', quotechar='"')

    with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, dialect='my_dialect')
        for row in reader:
            print(row)
    ```

#### **(2) `csv.unregister_dialect`**
- **功能**：删除已注册的方言。
- **语法**：
    ```python
    csv.unregister_dialect(name)
    ```
- **示例**：
    ```python
    import csv

    csv.unregister_dialect('my_dialect')
    ```

#### **(3) `csv.list_dialects`**
- **功能**：返回所有已注册的方言名称。
- **语法**：
    ```python
    csv.list_dialects()
    ```
- **示例**：
    ```python
    import csv

    dialects = csv.list_dialects()
    print(dialects)  # 输出：['excel', 'excel-tab', 'unix']
    ```

#### **(4) `csv.get_dialect`**
- **功能**：获取指定名称的方言对象。
- **语法**：
    ```python
    csv.get_dialect(name)
    ```
- **示例**：
    ```python
    import csv

    dialect = csv.get_dialect('excel')
    print(dialect.delimiter)  # 输出：','
    ```

!!! info

    使用Python做数据分析，很有可能会用到名为pandas的三方库，它是Python数据分析的神器之一。pandas中封装了名为read_csv和to_csv的函数用来读写CSV文件，其中read_CSV会将读取到的数据变成一个DataFrame对象，而DataFrame就是pandas库中最重要的类型，它封装了一系列用于数据处理的方法（清洗、转换、聚合等）；而to_csv会将DataFrame对象中的数据写入CSV文件，完成数据的持久化。read_csv函数和to_csv函数远远比原生的csvreader和csvwriter强大。


## Excel文件

### Excel简介

Excel是Microsoft（微软）为使用Windows和macOS操作系统开发的一款电子表格软件。Excel凭借其直观的界面、出色的计算功能和图表工具，再加上成功的市场营销，一直以来都是最为流行的个人计算机数据处理软件。当然，Excel也有很多竞品，例如Google Sheets、LibreOffice Calc、Numbers等，这些竞品基本上也能够兼容Excel，至少能够读写较新版本的Excel文件，当然这些不是我们讨论的重点。掌握用Python程序操作Excel文件，可以让日常办公自动化的工作更加轻松愉快，而且在很多商业项目中，导入导出Excel文件都是特别常见的功能。

Python操作Excel需要三方库的支持，如果要兼容Excel 2007以前的版本，也就是`xls`格式的Excel文件，可以使用三方库`xlrd`和`xlwt`，前者用于读Excel文件，后者用于写Excel文件。如果使用较新版本的Excel，即操作`xlsx`格式的Excel文件，可以使用`openpyxl`库，当然这个库不仅仅可以操作Excel，还可以操作其他基于Office Open XML的电子表格文件。

本章我们先讲解基于`xlwt`和`xlrd`操作Excel文件，大家可以先使用下面的命令安装这两个三方库以及配合使用的工具模块`xlutils`。

```Bash
pip install xlwt xlrd xlutils
```

### 读Excel文件

例如在当前文件夹下有一个名为“阿里巴巴2020年股票数据.xls”的Excel文件，如果想读取并显示该文件的内容，可以通过如下所示的代码来完成。

```Python
import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetnames = wb.sheet_names()
print(sheetnames)
# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetnames[0])
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            # 第1列的xldate类型先转成元组再格式化为“年月日”的格式
            if col == 0:
                # xldate_as_tuple函数的第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
        print(value, end='\t')
    print()
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)
# 获取第一行的值（列表）
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))
```

> **提示**：上面代码中使用的Excel文件“阿里巴巴2020年股票数据.xls”可以通过后面的百度云盘地址进行获取。链接:https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g 提取码:e7b4。

相信通过上面的代码，大家已经了解到了如何读取一个Excel文件，如果想知道更多关于`xlrd`模块的知识，可以阅读它的[官方文档](https://xlrd.readthedocs.io/en/latest/)。

### 写Excel文件

写入Excel文件可以通过`xlwt` 模块的`Workbook`类创建工作簿对象，通过工作簿对象的`add_sheet`方法可以添加工作表，通过工作表对象的`write`方法可以向指定单元格中写入数据，最后通过工作簿对象的`save`方法将工作簿写入到指定的文件或内存中。下面的代码实现了将`5`个学生`3`门课程的考试成绩写入Excel文件的操作。

```Python
import random

import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')
# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
wb.save('考试成绩表.xls')
```

#### 调整单元格样式

在写Excel文件时，我们还可以为单元格设置样式，主要包括字体（Font）、对齐方式（Alignment）、边框（Border）和背景（Background）的设置，`xlwt`对这几项设置都封装了对应的类来支持。要设置单元格样式需要首先创建一个`XFStyle`对象，再通过该对象的属性对字体、对齐方式、边框等进行设定，例如在上面的例子中，如果希望将表头单元格的背景色修改为黄色，可以按照如下的方式进行操作。

```Python
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
pattern.pattern_fore_colour = 5
header_style.pattern = pattern
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title, header_style)
```

如果希望为表头设置指定的字体，可以使用`Font`类并添加如下所示的代码。

```Python
font = xlwt.Font()
# 字体名称
font.name = '华文楷体'
# 字体大小（20是基准单位，18表示18px）
font.height = 20 * 18
# 是否使用粗体
font.bold = True
# 是否使用斜体
font.italic = False
# 字体颜色
font.colour_index = 1
header_style.font = font
```

> **注意**：上面代码中指定的字体名（`font.name`）应当是本地系统有的字体，例如在我的电脑上有名为“华文楷体”的字体。

如果希望表头垂直居中对齐，可以使用下面的代码进行设置。

```Python
align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align
```

如果希望给表头加上黄色的虚线边框，可以使用下面的代码来设置。

```Python
borders = xlwt.Borders()
props = (
    ('top', 'top_colour'), ('right', 'right_colour'),
    ('bottom', 'bottom_colour'), ('left', 'left_colour')
)
# 通过循环对四个方向的边框样式及颜色进行设定
for position, color in props:
    # 使用setattr内置函数动态给对象指定的属性赋值
    setattr(borders, position, xlwt.Borders.DASHED)
    setattr(borders, color, 5)
header_style.borders = borders
```

如果要调整单元格的宽度（列宽）和表头的高度（行高），可以按照下面的代码进行操作。

```Python
# 设置行高为40px
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    # 设置单元格的数据和样式
    sheet.write(0, index, title, header_style)
```

#### 公式计算

对于前面打开的“阿里巴巴2020年股票数据.xls”文件，如果要统计全年收盘价（Close字段）的平均值以及全年交易量（Volume字段）的总和，可以使用Excel的公式计算即可。我们可以先使用`xlrd`读取Excel文件夹，然后通过`xlutils`三方库提供的`copy`函数将读取到的Excel文件转成`Workbook`对象进行写操作，在调用`write`方法时，可以将一个`Formula`对象写入单元格。

实现公式计算的代码如下所示。

```Python
import xlrd
import xlwt
from xlutils.copy import copy

wb_for_read = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
sheet1 = wb_for_read.sheet_by_index(0)
nrows, ncols = sheet1.nrows, sheet1.ncols
wb_for_write = copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows, 4, xlwt.Formula(f'average(E2:E{nrows})'))
sheet2.write(nrows, 6, xlwt.Formula(f'sum(G2:G{nrows})'))
wb_for_write.save('阿里巴巴2020年股票数据汇总.xls')
```

> **说明**：上面的代码有一些小瑕疵，有兴趣的读者可以自行探索并思考如何解决。

###  简单的总结

掌握了Python程序操作Excel的方法，可以解决日常办公中很多繁琐的处理Excel电子表格工作，最常见就是将多个数据格式相同的Excel文件合并到一个文件以及从多个Excel文件或表单中提取指定的数据。当然，如果要对表格数据进行处理，使用Python数据分析神器之一的`pandas`库可能更为方便。



## 第25课：用Python读写Excel文件-2

### Excel简介

Excel是Microsoft（微软）为使用Windows和macOS操作系统开发的一款电子表格软件。Excel凭借其直观的界面、出色的计算功能和图表工具，再加上成功的市场营销，一直以来都是最为流行的个人计算机数据处理软件。当然，Excel也有很多竞品，例如Google Sheets、LibreOffice Calc、Numbers等，这些竞品基本上也能够兼容Excel，至少能够读写较新版本的Excel文件，当然这些不是我们讨论的重点。掌握用Python程序操作Excel文件，可以让日常办公自动化的工作更加轻松愉快，而且在很多商业项目中，导入导出Excel文件都是特别常见的功能。

本章我们继续讲解基于另一个三方库`openpyxl`如何进行Excel文件操作，首先需要先安装它。

```Bash
pip install openpyxl
```

`openpyxl`的优点在于，当我们打开一个Excel文件后，既可以对它进行读操作，又可以对它进行写操作，而且在操作的便捷性上是优于`xlwt`和`xlrd`的。此外，如果要进行样式编辑和公式计算，使用`openpyxl`也远比上一个章节我们讲解的方式更为简单，而且`openpyxl`还支持数据透视和插入图表等操作，功能非常强大。有一点需要再次强调，`openpyxl`并不支持操作Office 2007以前版本的Excel文件。

### 读取Excel文件

例如在当前文件夹下有一个名为“阿里巴巴2020年股票数据.xlsx”的Excel文件，如果想读取并显示该文件的内容，可以通过如下所示的代码来完成。

```Python
import datetime

import openpyxl

# 加载一个工作簿 ---> Workbook
wb = openpyxl.load_workbook('阿里巴巴2020年股票数据.xlsx')
# 获取工作表的名字
print(wb.sheetnames)
# 获取工作表 ---> Worksheet
sheet = wb.worksheets[0]
# 获得单元格的范围
print(sheet.dimensions)
# 获得行数和列数
print(sheet.max_row, sheet.max_column)

# 获取指定单元格的值
print(sheet.cell(3, 3).value)
print(sheet['C3'].value)
print(sheet['G255'].value)

# 获取多个单元格（嵌套元组）
print(sheet['A2:C5'])

# 读取所有单元格的数据
for row_ch in range(2, sheet.max_row + 1):
    for col_ch in 'ABCDEFG':
        value = sheet[f'{col_ch}{row_ch}'].value
        if type(value) == datetime.datetime:
            print(value.strftime('%Y年%m月%d日'), end='\t')
        elif type(value) == int:
            print(f'{value:<10d}', end='\t')
        elif type(value) == float:
            print(f'{value:.4f}', end='\t')
        else:
            print(value, end='\t')
    print()
```

> **提示**：上面代码中使用的Excel文件“阿里巴巴2020年股票数据.xlsx”可以通过后面的百度云盘地址进行获取。链接:https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g 提取码:e7b4。

需要提醒大家一点，`openpyxl`获取指定的单元格有两种方式，一种是通过`cell`方法，需要注意，该方法的行索引和列索引都是从`1`开始的，这是为了照顾用惯了Excel的人的习惯；另一种是通过索引运算，通过指定单元格的坐标，例如`C3`、`G255`，也可以取得对应的单元格，再通过单元格对象的`value`属性，就可以获取到单元格的值。通过上面的代码，相信大家还注意到了，可以通过类似`sheet['A2:C5']`或`sheet['A2':'C5']`这样的切片操作获取多个单元格，该操作将返回嵌套的元组，相当于获取到了多行多列。

### 写Excel文件

下面我们使用`openpyxl`来进行写Excel操作。

```Python
import random

import openpyxl

# 第一步：创建工作簿（Workbook）
wb = openpyxl.Workbook()

# 第二步：添加工作表（Worksheet）
sheet = wb.active
sheet.title = '期末成绩'

titles = ('姓名', '语文', '数学', '英语')
for col_index, title in enumerate(titles):
    sheet.cell(1, col_index + 1, title)

names = ('关羽', '张飞', '赵云', '马超', '黄忠')
for row_index, name in enumerate(names):
    sheet.cell(row_index + 2, 1, name)
    for col_index in range(2, 5):
        sheet.cell(row_index + 2, col_index, random.randrange(50, 101))

# 第四步：保存工作簿
wb.save('考试成绩表.xlsx')
```

#### 调整样式和公式计算

在使用`openpyxl`操作Excel时，如果要调整单元格的样式，可以直接通过单元格对象（`Cell`对象）的属性进行操作。单元格对象的属性包括字体（`font`）、对齐（`alignment`）、边框（`border`）等，具体的可以参考`openpyxl`的[官方文档](https://openpyxl.readthedocs.io/en/stable/index.html)。在使用`openpyxl`时，如果需要做公式计算，可以完全按照Excel中的操作方式来进行，具体的代码如下所示。

```Python
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

# 对齐方式
alignment = Alignment(horizontal='center', vertical='center')
# 边框线条
side = Side(color='ff7f50', style='mediumDashed')

wb = openpyxl.load_workbook('考试成绩表.xlsx')
sheet = wb.worksheets[0]

# 调整行高和列宽
sheet.row_dimensions[1].height = 30
sheet.column_dimensions['E'].width = 120

sheet['E1'] = '平均分'
# 设置字体
sheet.cell(1, 5).font = Font(size=18, bold=True, color='ff1493', name='华文楷体')
# 设置对齐方式
sheet.cell(1, 5).alignment = alignment
# 设置单元格边框
sheet.cell(1, 5).border = Border(left=side, top=side, right=side, bottom=side)
for i in range(2, 7):
    # 公式计算每个学生的平均分
    sheet[f'E{i}'] = f'=average(B{i}:D{i})'
    sheet.cell(i, 5).font = Font(size=12, color='4169e1', italic=True)
    sheet.cell(i, 5).alignment = alignment

wb.save('考试成绩表.xlsx')
```

### 生成统计图表

通过`openpyxl`库，可以直接向Excel中插入统计图表，具体的做法跟在Excel中插入图表大体一致。我们可以创建指定类型的图表对象，然后通过该对象的属性对图表进行设置。当然，最为重要的是为图表绑定数据，即横轴代表什么，纵轴代表什么，具体的数值是多少。最后，可以将图表对象添加到表单中，具体的代码如下所示。

```Python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook(write_only=True)
sheet = wb.create_sheet()

rows = [
    ('类别', '销售A组', '销售B组'),
    ('手机', 40, 30),
    ('平板', 50, 60),
    ('笔记本', 80, 70),
    ('外围设备', 20, 10),
]

# 向表单中添加行
for row in rows:
    sheet.append(row)

# 创建图表对象
chart = BarChart()
chart.type = 'col'
chart.style = 10
# 设置图表的标题
chart.title = '销售统计图'
# 设置图表纵轴的标题
chart.y_axis.title = '销量'
# 设置图表横轴的标题
chart.x_axis.title = '商品类别'
# 设置数据的范围
data = Reference(sheet, min_col=2, min_row=1, max_row=5, max_col=3)
# 设置分类的范围
cats = Reference(sheet, min_col=1, min_row=2, max_row=5)
# 给图表添加数据
chart.add_data(data, titles_from_data=True)
# 给图表设置分类
chart.set_categories(cats)
chart.shape = 4
# 将图表添加到表单指定的单元格中
sheet.add_chart(chart, 'A10')

wb.save('demo.xlsx')
```

运行上面的代码，打开生成的Excel文件，效果如下图所示。

<img src="https://github.com/jackfrued/mypic/raw/master/20210819235009.png" alt="image-20210819235009026" width="75%">


## 第27课：用Python操作PDF文件

PDF是Portable Document Format的缩写，这类文件通常使用`.pdf`作为其扩展名。在日常开发工作中，最容易遇到的就是从PDF中读取文本内容以及用已有的内容生成PDF文档这两个任务。

### 从PDF中提取文本

在Python中，可以使用名为`PyPDF2`的三方库来读取PDF文件，可以使用下面的命令来安装它。

```Bash
pip install PyPDF2
```

`PyPDF2`没有办法从PDF文档中提取图像、图表或其他媒体，但它可以提取文本，并将其返回为Python字符串。

```Python
import PyPDF2

reader = PyPDF2.PdfReader('test.pdf')
for page in reader.pages:
    print(page.extract_text())
```

> **提示**：上面代码中使用的PDF文件“test.pdf”以及下面的代码中需要用到的PDF文件，也可以通过下面的百度云盘地址进行获取。链接:https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g 提取码:e7b4。

当然，`PyPDF2`并不是什么样的PDF文档都能提取出文字来，这个问题就我所知并没有什么特别好的解决方法，尤其是在提取中文的时候。网上也有很多讲解从PDF中提取文字的文章，推荐大家自行阅读[《三大神器助力Python提取pdf文档信息》](https://cloud.tencent.com/developer/article/1395339)一文进行了解。

要从PDF文件中提取文本也可以直接使用三方的命令行工具，具体的做法如下所示。

```Bash
pip install pdfminer.six
pdf2text.py test.pdf
```

### 旋转和叠加页面

上面的代码中通过创建`PdfFileReader`对象的方式来读取PDF文档，该对象的`getPage`方法可以获得PDF文档的指定页并得到一个`PageObject`对象，通过`PageObject`对象的`rotateClockwise`和`rotateCounterClockwise`方法可以实现页面的顺时针和逆时针方向旋转，通过`PageObject`对象的`addBlankPage`方法可以添加一个新的空白页，代码如下所示。

```Python
reader = PyPDF2.PdfReader('XGBoost.pdf')
writer = PyPDF2.PdfWriter()

for no, page in enumerate(reader.pages):
    if no % 2 == 0:
        new_page = page.rotate(-90)
    else:
        new_page = page.rotate(90)
    writer.add_page(new_page)

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

### 加密PDF文件

使用`PyPDF2`中的`PdfFileWrite`对象可以为PDF文档加密，如果需要给一系列的PDF文档设置统一的访问口令，使用Python程序来处理就会非常的方便。

```Python
import PyPDF2

reader = PyPDF2.PdfReader('XGBoost.pdf')
writer = PyPDF2.PdfWriter()

for page in reader.pages:
    writer.add_page(page)
    
writer.encrypt('foobared')

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

### 批量添加水印

上面提到的`PageObject`对象还有一个名为`mergePage`的方法，可以两个PDF页面进行叠加，通过这个操作，我们很容易实现给PDF文件添加水印的功能。例如要给上面的“XGBoost.pdf”文件添加一个水印，我们可以先准备好一个提供水印页面的PDF文件，然后将包含水印的`PageObject`读取出来，然后再循环遍历“XGBoost.pdf”文件的每个页，获取到`PageObject`对象，然后通过`mergePage`方法实现水印页和原始页的合并，代码如下所示。

```Python
reader1 = PyPDF2.PdfReader('XGBoost.pdf')
reader2 = PyPDF2.PdfReader('watermark.pdf')
writer = PyPDF2.PdfWriter()
watermark_page = reader2.pages[0]

for page in reader1.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

如果愿意，还可以让奇数页和偶数页使用不同的水印，大家可以自己思考下应该怎么做。

### 创建PDF文件

创建PDF文档需要三方库`reportlab`的支持，安装的方法如下所示。

```Bash
pip install reportlab
```

下面通过一个例子为大家展示`reportlab`的用法。

```Python
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdf_canvas = canvas.Canvas('resources/demo.pdf', pagesize=A4)
width, height = A4

# 绘图
image = canvas.ImageReader('resources/guido.jpg')
pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

# 显示当前页
pdf_canvas.showPage()

# 注册字体文件
pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/青呱石头体.ttf'))

# 写字
pdf_canvas.setFont('Font2', 40)
pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
pdf_canvas.setFont('Font1', 40)
pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
pdf_canvas.rotate(18)
pdf_canvas.drawString(250, 250, 'hello, world!')

# 保存
pdf_canvas.save()
```

上面的代码如果不太理解也没有关系，等真正需要用Python创建PDF文档的时候，再好好研读一下`reportlab`的[官方文档](https://www.reportlab.com/docs/reportlab-userguide.pdf)就可以了。

> **提示**：上面代码中用到的图片和字体，也可以通过下面的百度云盘链接获取。链接:https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g 提取码:e7b4。

###  简单的总结

在学习完上面的内容之后，相信大家已经知道像合并多个PDF文件这样的工作应该如何用Python代码来处理了，赶紧自己动手试一试吧。



## 第28课：用Python处理图像

### 入门知识

1. 颜色。如果你有使用颜料画画的经历，那么一定知道混合红、黄、蓝三种颜料可以得到其他的颜色，事实上这三种颜色就是美术中的三原色，它们是不能再分解的基本颜色。在计算机中，我们可以将红、绿、蓝三种色光以不同的比例叠加来组合成其他的颜色，因此这三种颜色就是色光三原色。在计算机系统中，我们通常会将一个颜色表示为一个RGB值或RGBA值（其中的A表示Alpha通道，它决定了透过这个图像的像素，也就是透明度）。

   |    名称     |      RGB值      |     名称     |     RGB值     |
   | :---------: | :-------------: | :----------: | :-----------: |
   | White（白） | (255, 255, 255) |  Red（红）   |  (255, 0, 0)  |
   | Green（绿） |   (0, 255, 0)   |  Blue（蓝）  |  (0, 0, 255)  |
   | Gray（灰）  | (128, 128, 128) | Yellow（黄） | (255, 255, 0) |
   | Black（黑） |    (0, 0, 0)    | Purple（紫） | (128, 0, 128) |

2. 像素。对于一个由数字序列表示的图像来说，最小的单位就是图像上单一颜色的小方格，这些小方块都有一个明确的位置和被分配的色彩数值，而这些一小方格的颜色和位置决定了该图像最终呈现出来的样子，它们是不可分割的单位，我们通常称之为像素（pixel）。每一个图像都包含了一定量的像素，这些像素决定图像在屏幕上所呈现的大小，大家如果爱好拍照或者自拍，对像素这个词就不会陌生。

### 用Pillow处理图像

Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作。可以使用下面的命令来安装Pillow。

```Shell
pip install pillow
```

Pillow中最为重要的是`Image`类，可以通过`Image`模块的`open`函数来读取图像并获得`Image`类型的对象。

1. 读取和显示图像

   ```Python
   from PIL import Image
   
   # 读取图像获得Image对象
   image = Image.open('guido.jpg')
   # 通过Image对象的format属性获得图像的格式
   print(image.format) # JPEG
   # 通过Image对象的size属性获得图像的尺寸
   print(image.size)   # (500, 750)
   # 通过Image对象的mode属性获取图像的模式
   print(image.mode)   # RGB
   # 通过Image对象的show方法显示图像
   image.show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202628.png" width="80%">

2. 剪裁图像

   ```Python
   # 通过Image对象的crop方法指定剪裁区域剪裁图像
   image.crop((80, 20, 310, 360)).show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202701.png" width="80%">

3. 生成缩略图

   ```Python
   # 通过Image对象的thumbnail方法生成指定尺寸的缩略图
   image.thumbnail((128, 128))
   image.show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202722.png" width="100%">

4. 缩放和黏贴图像

   ```Python
   # 读取骆昊的照片获得Image对象
   luohao_image = Image.open('luohao.png')
   # 读取吉多的照片获得Image对象
   guido_image = Image.open('guido.jpg')
   # 从吉多的照片上剪裁出吉多的头
   guido_head = guido_image.crop((80, 20, 310, 360))
   width, height = guido_head.size
   # 使用Image对象的resize方法修改图像的尺寸
   # 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
   luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
   luohao_image.show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202749.png" width="80%">

5. 旋转和翻转

   ```Python
   image = Image.open('guido.jpg')
   # 使用Image对象的rotate方法实现图像的旋转
   image.rotate(45).show()
   # 使用Image对象的transpose方法实现图像翻转
   # Image.FLIP_LEFT_RIGHT - 水平翻转
   # Image.FLIP_TOP_BOTTOM - 垂直翻转
   image.transpose(Image.FLIP_TOP_BOTTOM).show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202829.png" width="80%">

6. 操作像素

   ```Python
   for x in range(80, 310):
       for y in range(20, 360):
           # 通过Image对象的putpixel方法修改图像指定像素点
           image.putpixel((x, y), (128, 128, 128))
   image.show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202932.png" width="80%">

7. 滤镜效果

   ```Python
   from PIL import ImageFilter
   
   # 使用Image对象的filter方法对图像进行滤镜处理
   # ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
   image.filter(ImageFilter.CONTOUR).show()
   ```

   <img src="https://github.com/jackfrued/mypic/raw/master/20210803202953.png" width="80%">

### 使用Pillow绘图

Pillow中有一个名为`ImageDraw`的模块，该模块的`Draw`函数会返回一个`ImageDraw`对象，通过`ImageDraw`对象的`arc`、`line`、`rectangle`、`ellipse`、`polygon`等方法，可以在图像上绘制出圆弧、线条、矩形、椭圆、多边形等形状，也可以通过该对象的`text`方法在图像上添加文字。

<img src="https://github.com/jackfrued/mypic/raw/master/20210803203016.png" width="80%">

要绘制如上图所示的图像，完整的代码如下所示。

```Python
import random

from PIL import Image, ImageDraw, ImageFont


def random_color():
    """生成随机颜色"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


width, height = 800, 600
# 创建一个800*600的图像，背景色为白色
image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
# 创建一个ImageDraw对象
drawer = ImageDraw.Draw(image)
# 通过指定字体和大小获得ImageFont对象
font = ImageFont.truetype('Kongxin.ttf', 32)
# 通过ImageDraw对象的text方法绘制文字
drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0), font=font)
# 通过ImageDraw对象的line方法绘制两条对角直线
drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
# 通过ImageDraw对象的rectangle方法绘制矩形
drawer.rectangle(xy, outline=(255, 0, 0), width=2)
# 通过ImageDraw对象的ellipse方法绘制椭圆
for i in range(4):
    left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
    drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
# 显示图像
image.show()
# 保存图像
image.save('result.png')
```

> **注意**：上面代码中使用的字体文件需要根据自己准备，可以选择自己喜欢的字体文件并放置在代码目录下。

###  简单的总结

使用Python语言做开发，除了可以用Pillow来处理图像外，还可以使用更为强大的OpenCV库来完成图形图像的处理，OpenCV（**Open** Source **C**omputer **V**ision Library）是一个跨平台的计算机视觉库，可以用来开发实时图像处理、计算机视觉和模式识别程序。在我们的日常工作中，有很多繁琐乏味的任务其实都可以通过Python程序来处理，编程的目的就是让计算机帮助我们解决问题，减少重复乏味的劳动。通过本章节的学习，相信大家已经感受到了使用Python程序绘图P图的乐趣，其实Python能做的事情还远不止这些，继续你的学习吧。


## 第29课：用Python发送邮件和短信

在前面的课程中，我们已经教会大家如何用Python程序自动的生成Excel、Word、PDF文档，接下来我们还可以更进一步，就是通过邮件将生成好的文档发送给指定的收件人，然后用短信告知对方我们发出了邮件。这些事情利用Python程序也可以轻松愉快的解决。

### 发送电子邮件

在即时通信软件如此发达的今天，电子邮件仍然是互联网上使用最为广泛的应用之一，公司向应聘者发出录用通知、网站向用户发送一个激活账号的链接、银行向客户推广它们的理财产品等几乎都是通过电子邮件来完成的，而这些任务应该都是由程序自动完成的。

我们可以用HTTP（超文本传输协议）来访问网站资源，HTTP是一个应用级协议，它建立在TCP（传输控制协议）之上，TCP为很多应用级协议提供了可靠的数据传输服务。如果要发送电子邮件，需要使用SMTP（简单邮件传输协议），它也是建立在TCP之上的应用级协议，规定了邮件的发送者如何跟邮件服务器进行通信的细节。Python通过名为`smtplib`的模块将这些操作简化成了`SMTP_SSL`对象，通过该对象的`login`和`send_mail`方法，就能够完成发送邮件的操作。

我们先尝试一下发送一封极为简单的邮件，该邮件不包含附件、图片以及其他超文本内容。发送邮件首先需要接入邮件服务器，我们可以自己架设邮件服务器，这件事情对新手并不友好，但是我们可以选择使用第三方提供的邮件服务。例如，我在<www.126.com>已经注册了账号，登录成功之后，就可以在设置中开启SMTP服务，这样就相当于获得了邮件服务器，具体的操作如下所示。

<img src="https://github.com/jackfrued/mypic/raw/master/20210820190307.png" alt="image-20210820190306861" width="95%">

![image-20210820190816557](https://github.com/jackfrued/mypic/raw/master/20210820190816.png)

用手机扫码上面的二维码可以通过发送短信的方式来获取授权码，短信发送成功后，点击“我已发送”就可以获得授权码。授权码需要妥善保管，因为一旦泄露就会被其他人冒用你的身份来发送邮件。接下来，我们就可以编写发送邮件的代码了，如下所示。

```Python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email['From'] = 'xxxxxxxxx@126.com'
email['To'] = 'yyyyyy@qq.com;zzzzzz@1000phone.com'
email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
# 添加邮件正文内容
content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
email.attach(MIMEText(content, 'plain', 'utf-8'))

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
# 通过用户名和授权码进行登录
smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    'xxxxxxxxx@126.com',
    ['yyyyyy@qq.com', 'zzzzzz@1000phone.com'],
    email.as_string()
)
```

如果要发送带有附件的邮件，只需要将附件的内容处理成BASE64编码，那么它就和普通的文本内容几乎没有什么区别。BASE64是一种基于64个可打印字符来表示二进制数据的表示方法，常用于某些需要表示、传输、存储二进制数据的场合，电子邮件就是其中之一。对这种编码方式不理解的同学，推荐阅读[《Base64笔记》](http://www.ruanyifeng.com/blog/2008/06/base64.html)一文。在之前的内容中，我们也提到过，Python标准库的`base64`模块提供了对BASE64编解码的支持。

下面的代码演示了如何发送带附件的邮件。

```Python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email['From'] = 'xxxxxxxxx@126.com'
email['To'] = 'zzzzzzzz@1000phone.com'
email['Subject'] = Header('请查收离职证明文件', 'utf-8')
# 添加邮件正文内容（带HTML标签排版的内容）
content = """<p>亲爱的前同事：</p>
<p>你需要的离职证明在附件中，请查收！</p>
<br>
<p>祝，好！</p>
<hr>
<p>孙美丽 即日</p>"""
email.attach(MIMEText(content, 'html', 'utf-8'))
# 读取作为附件的文件
with open(f'resources/王大锤离职证明.docx', 'rb') as file:
    attachment = MIMEText(file.read(), 'base64', 'utf-8')
    # 指定内容类型
    attachment['content-type'] = 'application/octet-stream'
    # 将中文文件名处理成百分号编码
    filename = quote('王大锤离职证明.docx')
    # 指定如何处置内容
    attachment['content-disposition'] = f'attachment; filename="{filename}"'

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
# 通过用户名和授权码进行登录
smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    'xxxxxxxxx@126.com',
    'zzzzzzzz@1000phone.com',
    email.as_string()
)
```

为了方便大家用Python实现邮件发送，我将上面的代码封装成了函数，使用的时候大家只需要调整邮件服务器域名、端口、用户名和授权码就可以了。

```Python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 邮件服务器域名（自行修改）
EMAIL_HOST = 'smtp.126.com'
# 邮件服务端口（通常是465）
EMAIL_PORT = 465
# 登录邮件服务器的账号（自行修改）
EMAIL_USER = 'xxxxxxxxx@126.com'
# 开通SMTP服务的授权码（自行修改）
EMAIL_AUTH = '邮件服务器的授权码'


def send_email(*, from_user, to_users, subject='', content='', filenames=[]):
    """发送邮件
    
    :param from_user: 发件人
    :param to_users: 收件人，多个收件人用英文分号进行分隔
    :param subject: 邮件的主题
    :param content: 邮件正文内容
    :param filenames: 附件要发送的文件路径
    """
    email = MIMEMultipart()
    email['From'] = from_user
    email['To'] = to_users
    email['Subject'] = subject

    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open(filename, 'rb') as file:
            pos = filename.rfind('/')
            display_filename = filename[pos + 1:] if pos >= 0 else filename
            display_filename = quote(display_filename)
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            attachment['content-type'] = 'application/octet-stream'
            attachment['content-disposition'] = f'attachment; filename="{display_filename}"'
            email.attach(attachment)

    smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    smtp.login(EMAIL_USER, EMAIL_AUTH)
    smtp.sendmail(from_user, to_users.split(';'), email.as_string())
```

### 发送短信

发送短信也是项目中常见的功能，网站的注册码、验证码、营销信息基本上都是通过短信来发送给用户的。发送短信需要三方平台的支持，下面我们以[螺丝帽平台](https://luosimao.com/)为例，为大家介绍如何用Python程序发送短信。注册账号和购买短信服务的细节我们不在这里进行赘述，大家可以咨询平台的客服。

![image-20210820194420911](https://github.com/jackfrued/mypic/raw/master/20210820194421.png)

接下来，我们可以通过`requests`库向平台提供的短信网关发起一个HTTP请求，通过将接收短信的手机号和短信内容作为参数，就可以发送短信，代码如下所示。

```Python
import random

import requests


def send_message_by_luosimao(tel, message):
    """发送短信（调用螺丝帽短信网关）"""
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-注册成功后平台分配的KEY'),
        data={
            'mobile': tel,
            'message': message
        },
        timeout=10,
        verify=False
    )
    return resp.json()


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    return ''.join(random.choices('0123456789', k=length))


def main():
    code = gen_mobile_code()
    message = f'您的短信验证码是{code}，打死也不能告诉别人哟！【Python小课】'
    print(send_message_by_luosimao('13500112233', message))


if __name__ == '__main__':
    main()
```

上面请求螺丝帽的短信网关`http://sms-api.luosimao.com/v1/send.json`会返回JSON格式的数据，如果返回`{'error': 0, 'msg': 'OK'}`就说明短信已经发送成功了，如果`error`的值不是`0`，可以通过查看官方的[开发文档](https://luosimao.com/docs/api/)了解到底哪个环节出了问题。螺丝帽平台常见的错误类型如下图所示。

<img src="https://github.com/jackfrued/mypic/raw/master/20210820195505.png" alt="image-20210820195505761" style="zoom:50%;">

目前，大多数短信平台都会要求短信内容必须附上签名，下图是我在螺丝帽平台配置的短信签名“【Python小课】”。有些涉及到敏感内容的短信，还需要提前配置短信模板，有兴趣的读者可以自行研究。一般情况下，平台为了防范短信被盗用，还会要求设置“IP白名单”，不清楚如何配置的可以咨询平台客服。

![image-20210820194653785](https://github.com/jackfrued/mypic/raw/master/20210820194653.png)

当然国内的短信平台很多，读者可以根据自己的需要进行选择（通常会考虑费用预算、短信达到率、使用的难易程度等指标），如果需要在商业项目中使用短信服务建议购买短信平台提供的套餐服务。

### 简单的总结

其实，发送邮件和发送短信一样，也可以通过调用三方服务来完成，在实际的商业项目中，建议自己架设邮件服务器或购买三方服务来发送邮件，这个才是比较靠谱的选择。


