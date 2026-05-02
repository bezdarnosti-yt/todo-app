// src/components/TodoList.tsx

import type { Todo } from "../types/todo";

type TodoListProps = {
  todos: Todo[];
  onDelete: (id: number) => void;
};

function TodoList({ todos, onDelete }: TodoListProps) {
  return (
    <ul className="space-y-2">
      {todos.map((todo) => (
        <li
          className="p-3 bg-gray-100 rounded flex justify-between items-center"
          key={todo.id}
        >
          {todo.name}
          <button
            onClick={() => {
              onDelete(todo.id);
            }}
            className="text-red-500 hover:text-red-700"
          >
            X
          </button>
        </li>
      ))}
    </ul>
  );
}

export default TodoList;
