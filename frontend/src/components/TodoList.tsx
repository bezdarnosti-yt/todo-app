// src/components/TodoList.tsx

import type { Todo } from "../types/todo";
import TodoItem from "./TodoItem";

type TodoListProps = {
  todos: Todo[];
  onDelete: (id: number) => void;
  onUpdate: (id: number, name: string) => void;
};

function TodoList({ todos, onDelete, onUpdate }: TodoListProps) {
  return (
    <ul className="space-y-2">
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onDelete={onDelete}
          onUpdate={onUpdate}
        />
      ))}
    </ul>
  );
}

export default TodoList;
