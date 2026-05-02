import { useState } from "react";

type TodoFormProps = {
  onAdd: (name: string) => void;
};

function TodoForm({ onAdd }: TodoFormProps) {
  const [name, setName] = useState("");

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onAdd(name);
        setName("");
      }}
      className="flex gap-2 mb-4"
    >
      <input
        className="flex-1 px-3 py-2 border rounded"
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        type="submit"
      >
        Добавить
      </button>
    </form>
  );
}

export default TodoForm;
