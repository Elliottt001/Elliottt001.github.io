## 网页的构建

当用户导航到新网页时（通过单击链接或在浏览器地址栏中输入 Web 地址），将发送多个 HTTP 请求，并在 HTTP 响应中发回多个文件。在这些响应中收到的文件由浏览器处理，并放在一个用户可以与之交互的网页中。这种将各个部分组装到网页中的过程称为 渲染。

首先，浏览器接收包含网页内容并定义其结构的 HTML 文件，并对其进行解析。浏览器将其转换为称为 DOM 树（文档对象模型）的树状结构。DOM 表示计算机内存中的 HTML 文档结构。以这个基本的 HTML 代码片段为例：

![alt text](image.png)

/// caption
这就是一个树 `tree`，只不过变了一下形状（所以跟fds里画的不太一样）
///

> Each element, attribute, and piece of text in the HTML becomes a DOM node in the tree structure. The nodes are defined by their relationship to other DOM nodes. Some elements are parents of child nodes, and child nodes have siblings. The browser will parse this HTML and create the following DOM tree from it:

![alt text](image-1.png)

![HTML 与 CSS 的渲染过程](rendering.svg)

![alt text](image-2.png)

## React 里的更新

前面是浏览器把 HTML/CSS 变成页面。React 则是在状态变了之后，重新算出页面应该是什么样，再更新 DOM。

下面这个 TodoApp：`todos` 存列表，`newTodo` 存输入框。新增、删除、完成状态都通过 `setTodos` 更新。

```jsx
// TodoApp.js
import React, { useState } from "react";

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");

  const handleAddTodo = () => {
    if (newTodo.trim() === "") {
      alert("Please enter a todo item.");
      return;
    }

    setTodos([...todos, { text: newTodo, completed: false }]);
    setNewTodo("");
  };

  const handleDeleteTodo = (index) => {
    const updatedTodos = todos.filter((_, i) => i !== index);
    setTodos(updatedTodos);
  };

  const handleToggleComplete = (index) => {
    const updatedTodos = todos.map((todo, i) =>
      i === index ? { ...todo, completed: !todo.completed } : todo
    );
    setTodos(updatedTodos);
  };

  return (
    <div className="todo-app">
      <h1>Todo List</h1>
      <input
        type="text"
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="Add a new todo"
      />
      <button onClick={handleAddTodo}>Add</button>
      <ul>
        {todos.map((todo, index) => (
          <li key={index} className={todo.completed ? "completed" : ""}>
            {todo.text}
            <button onClick={() => handleDeleteTodo(index)}>Delete</button>
            <button onClick={() => handleToggleComplete(index)}>
              {todo.completed ? "Undo" : "Complete"}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
```

注意这里不是直接 `todos.push(...)`：展开成新数组，再交给 `setTodos`。修改某一项也是 `map` 生成新数组。

这个小例子删除、切换状态都用数组下标；真做项目时最好给每项一个稳定的 ID，列表的 `key` 也用 ID，避免删一项之后身份跟着挪。
