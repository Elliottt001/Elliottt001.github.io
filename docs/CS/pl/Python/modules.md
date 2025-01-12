## matplotlib

[Matplotlib 官方文档](https://matplotlib.org/stable/contents.html)。

### pylot

创建各种类型的图表，如折线图、散点图、柱状图、饼图等。

`matplotlib.pyplot` 通常以 `plt` 作为别名导入：

```python
import matplotlib.pyplot as plt
```

#### (1) **创建图表**
- **`plt.plot(x, y)`**：绘制折线图。
  - `x`：X 轴数据。
  - `y`：Y 轴数据。
- **`plt.scatter(x, y)`**：绘制散点图。
- **`plt.bar(x, height)`**：绘制柱状图。
- **`plt.pie(data)`**：绘制饼图。

#### (2) **设置图表属性**
- **`plt.title("Title")`**：设置图表标题。
- **`plt.xlabel("X Label")`**：设置 X 轴标签。
- **`plt.ylabel("Y Label")`**：设置 Y 轴标签。
- **`plt.legend()`**：显示图例。
- **`plt.grid(True)`**：显示网格。

#### (3) **显示和保存图表**
- **`plt.show()`**：显示图表。
- **`plt.savefig("filename.png")`**：保存图表为文件。

#### (4) **其他常用函数**
- **`plt.figure()`**：创建一个新的图表。
- **`plt.subplot()`**：创建子图。
- **`plt.xlim(min, max)`**：设置 X 轴范围。
- **`plt.ylim(min, max)`**：设置 Y 轴范围。

---

### 4. **示例代码**

#### (1) **折线图**
```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 创建折线图
plt.plot(x, y, label="Line 1", marker="o")

# 设置标题和标签
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 显示图例和网格
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
```

#### (2) **散点图**
```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 创建散点图
plt.scatter(x, y, label="Points", color="red")

# 设置标题和标签
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 显示图例和网格
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
```

#### (3) **柱状图**
```python
import matplotlib.pyplot as plt

# 数据
x = ["A", "B", "C", "D"]
y = [10, 20, 15, 25]

# 创建柱状图
plt.bar(x, y, label="Bars", color="blue")

# 设置标题和标签
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

# 显示图例和网格
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
```

#### (4) **饼图**
```python
import matplotlib.pyplot as plt

# 数据
labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]

# 创建饼图
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)

# 设置标题
plt.title("Pie Chart Example")

# 显示图表
plt.show()
```

#### (5) **子图**
```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [40, 30, 25, 20, 10]

# 创建子图
plt.figure(figsize=(10, 5))  # 设置图表大小

# 第一个子图
plt.subplot(1, 2, 1)  # 1 行 2 列，第 1 个子图
plt.plot(x, y1, label="Line 1", color="blue")
plt.title("Line Chart 1")
plt.legend()

# 第二个子图
plt.subplot(1, 2, 2)  # 1 行 2 列，第 2 个子图
plt.plot(x, y2, label="Line 2", color="red")
plt.title("Line Chart 2")
plt.legend()

# 显示图表
plt.show()
```

---

### 5. **高级功能**
- **自定义样式**：可以通过 `plt.style.use()` 使用预定义的样式，例如：
  ```python
  plt.style.use("ggplot")
  ```
- **添加注释**：使用 `plt.text()` 或 `plt.annotate()` 在图表中添加文本或箭头注释。
- **颜色和标记**：可以通过 `color`、`marker`、`linestyle` 等参数自定义线条颜色、标记和样式。


