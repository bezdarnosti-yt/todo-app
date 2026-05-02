// src/App.tsx

import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";
import { useQuery } from "@tanstack/react-query";
import { fetchTodos } from "./api/todos";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createTodo } from "./api/todos";
import { deleteTodo } from "./api/todos";
import { updateTodo } from "./api/todos";

function App() {
  const {
    data: todos,
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["todos"],
    queryFn: fetchTodos,
  });

  const queryClient = useQueryClient();

  const createMutation = useMutation({
    mutationFn: (name: string) => createTodo(name),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] });
    },
  });

  const deleteMutation = useMutation({
    mutationFn: (id: number) => deleteTodo(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] });
    },
  });

  const updateMutation = useMutation({
    mutationFn: ({ id, name }: { id: number; name: string }) =>
      updateTodo(id, name),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] });
    },
  });

  if (isLoading) return <div>Загрузка...</div>;
  if (isError) return <div>Ошибка: {error.message}</div>;

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-3xl font-bold mb-6">Plankton Todo</h1>
      <div className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow">
        <TodoForm onAdd={(name) => createMutation.mutate(name)}></TodoForm>
        <TodoList
          todos={todos ?? []}
          onDelete={(id) => deleteMutation.mutate(id)}
          onUpdate={(id, name) => updateMutation.mutate({ id, name })}
        />
      </div>
    </div>
  );
}

export default App;
