import tkinter as tk
from tkinter import ttk, messagebox
from models import LogEntry


class LogBookApp:
    def __init__(self, root, book):
        self.root = root
        self.book = book
        self.root.title("IT-MLog (GUI)")
        self.root.geometry("900x500")  # Немного увеличил окно для описания

        # --- UI elemendid (Sisestus) ---
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10, fill="x")

        tk.Label(frame, text="Pealkiri:").grid(row=0, column=0)
        self.ent_title = tk.Entry(frame)
        self.ent_title.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Kirjeldus:").grid(row=0, column=2)
        self.ent_desc = tk.Entry(frame, width=40)  # Сделал поле ввода шире
        self.ent_desc.grid(row=0, column=3, padx=5)

        tk.Button(frame, text="Lisa kirje", command=self.add_log, bg="#e1e1e1").grid(row=0, column=4, padx=5)

        # --- Tabel (Treeview) ---
        # ДОБАВЛЕНО: "Kirjeldus" в кортеж колонок
        self.columns = ("Aeg", "Status", "Pealkiri", "Kirjeldus")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")

        # Настройка заголовков
        self.tree.heading("Aeg", text="Loomise aeg")
        self.tree.heading("Status", text="Staatus")
        self.tree.heading("Pealkiri", text="Pealkiri")
        self.tree.heading("Kirjeldus", text="Töö kirjeldus")

        # Настройка ширины колонок (чтобы описание было широким)
        self.tree.column("Aeg", width=150, anchor="center")
        self.tree.column("Status", width=80, anchor="center")
        self.tree.column("Pealkiri", width=200)
        self.tree.column("Kirjeldus", width=400)  # Самая широкая колонка

        self.tree.pack(fill="both", expand=True, padx=10)

        # --- Nupud (Alumine paneel) ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10, fill="x", padx=10)

        tk.Button(btn_frame, text="Muuda staatust (OPEN/DONE)", command=self.change_stat).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Kustuta valitud", command=self.del_log, fg="red").pack(side="left", padx=5)

        # Поле поиска прямо в GUI
        tk.Label(btn_frame, text="  Otsi:").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_table())
        self.ent_search = tk.Entry(btn_frame, textvariable=self.search_var)
        self.ent_search.pack(side="left", padx=5)

        tk.Button(btn_frame, text="Salvesta faili", command=self.save_data, bg="#d1ffd1").pack(side="right", padx=5)

        self.update_table()

    def update_table(self):
        """Värskendab tabeli sisu vastavalt andmetele ja otsingule."""
        # Puhastame tabeli
        for i in self.tree.get_children():
            self.tree.delete(i)

        search_term = self.search_var.get().lower()

        # Filtreerime ja lisame andmed
        for e in self.book.entries:
            if search_term in e.title.lower() or search_term in e.description.lower():
                self.tree.insert("", "end", values=(e.created_at, e.status, e.title, e.description))

    def add_log(self):
        t = self.ent_title.get()
        d = self.ent_desc.get()
        valid, msg = LogEntry.validate(t, d)
        if valid:
            self.book.add_entry(LogEntry(t, d))
            self.update_table()
            self.ent_title.delete(0, tk.END)
            self.ent_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Vigased andmed", msg)

    def del_log(self):
        sel = self.tree.selection()
        if not sel:
            return

        item_data = self.tree.item(sel[0])['values']
        # item_data[0] on aeg (ID)
        self.book.delete_entry(str(item_data[0]))
        self.update_table()

    def change_stat(self):
        sel = self.tree.selection()
        if not sel:
            return

        item_data = self.tree.item(sel[0])['values']
        self.book.change_status(str(item_data[0]))
        self.update_table()

    def save_data(self):
        self.book.save_to_json()
        messagebox.showinfo("Salvestatud", "Andmed on edukalt salvestatud JSON faili.")