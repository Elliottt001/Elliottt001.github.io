实验课不用去

quiz 可以请假补测   


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