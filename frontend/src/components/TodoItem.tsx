// src/components/TodoItem.tsx

import { useState } from "react";
import type { Todo } from "../types/todo";

type TodoItemProps = {
  todo: Todo;
  onDelete: (id: number) => void;
  onUpdate: (id: number, name: string) => void;
};

function TodoItem({ todo, onDelete, onUpdate }: TodoItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editValue, setEditValue] = useState(todo.name);

  const handleSave = () => {
    if (editValue.trim() && editValue !== todo.name) {
      onUpdate(todo.id, editValue);
    } else {
      setEditValue(todo.name);
    }
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditValue(todo.name);
    setIsEditing(false);
  };

  return (
    <li className="p-3 bg-gray-100 rounded flex justify-between items-center">
      {isEditing ? (
        <input
          value={editValue}
          onChange={(e) => setEditValue(e.target.value)}
          onBlur={handleSave}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSave();
            if (e.key === "Escape") handleCancel();
          }}
          autoFocus
          className="flex-1 px-2 py-1 border border-blue-500 rounded outline-none"
        />
      ) : (
        <span
          onClick={() => setIsEditing(true)}
          className="flex-1 cursor-pointer hover:text-blue-600"
        >
          {todo.name}
        </span>
      )}
      <button
        className="text-red-500 hover:text-red-700"
        onClick={() => onDelete(todo.id)}
      >
        X
      </button>
    </li>
  );
}

export default TodoItem;
