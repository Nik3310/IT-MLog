import tkinter as tk
from tkinter import ttk, messagebox


class LogBookApp:
    def __init__(self, root, book):
        self.root = root
        self.book = book
        self.root.title("IT-MLog (GUI)")
        self.root.geometry("900x500")

        # ... (код ввода остается прежним, но обновим таблицу) ...
        self.columns = ("ID", "Aeg", "Status", "Pealkiri", "Kirjeldus")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.column("ID", width=40, anchor="center")
        # ... остальные колонки как в прошлом примере ...
        self.tree.heading("Aeg", text="Aeg")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Pealkiri", text="Pealkiri")
        self.tree.heading("Kirjeldus", text="Kirjeldus")
        self.tree.pack(fill="both", expand=True, padx=10)

        # Кнопки
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Muuda staatust", command=self.change_stat).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Kustuta", command=self.del_log).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Salvesta", command=self.book.save_to_json).pack(side="left", padx=5)

        self.update_table()

    def update_table(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for e in self.book.entries:
            # Передаем e.entry_id первым
            self.tree.insert("", "end", values=(e.entry_id, e.created_at, e.status, e.title, e.description))

    def change_stat(self):
        sel = self.tree.selection()
        if sel:
            # Теперь ID берем из первой колонки (индекс 0)
            item_id = self.tree.item(sel[0])['values'][0]
            self.book.change_status(item_id)
            self.update_table()

    def del_log(self):
        sel = self.tree.selection()
        if sel:
            item_id = self.tree.item(sel[0])['values'][0]
            self.book.delete_entry(item_id)
            self.update_table()

