// src/api/todos.ts

import type { Todo } from "../types/todo";

const API_URL = import.meta.env.VITE_API_URL;

export async function fetchTodos(): Promise<Todo[]> {
  const response = await fetch(`${API_URL}/items`);
  if (!response.ok) {
    throw new Error("Failed to fetch todos");
  }
  return response.json();
}

export async function createTodo(name: string): Promise<Todo> {
  const response = await fetch(`${API_URL}/items`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
  if (!response.ok) {
    throw new Error("Failed to create todo");
  }
  return response.json();
}

export async function updateTodo(id: number, name: string): Promise<Todo> {
  const response = await fetch(`${API_URL}/items/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
  if (!response.ok) {
    throw new Error("Failed to update todo");
  }
  return response.json();
}

export async function deleteTodo(id: number): Promise<void> {
  const response = await fetch(`${API_URL}/items/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete todo");
  }
  return;
}
