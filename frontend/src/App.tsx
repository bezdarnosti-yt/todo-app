// src/App.tsx

import type { Todo } from "./types/todo";
import TodoList from "./components/TodoList";
import { useState } from "react";
import TodoForm from "./components/TodoForm";

function App() {
  const [todos, setTodos] = useState([
    { id: 1, name: "Купить хлеб" },
    { id: 2, name: "Выгулять собаку" },
    { id: 3, name: "Написать код" },
  ]);

  const handleAdd = (name: string) => {
    const newTodo: Todo = {
      id: Date.now(),
      name,
    };
    setTodos([...todos, newTodo]);
  };

  const handleDelete = (id: number) => {
    setTodos(todos.filter((t) => t.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-3xl font-bold mb-6">Plankton Todo</h1>
      <div className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow">
        <TodoForm onAdd={handleAdd}></TodoForm>
        <TodoList todos={todos} onDelete={handleDelete}></TodoList>
      </div>
    </div>
  );
}

export default App;
