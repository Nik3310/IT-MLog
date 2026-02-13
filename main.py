import sys
import tkinter as tk
from logic import LogBook
from cli_ui import run_cli, add_entry_cli, list_entries_cli
from gui_ui import LogBookApp


def main():
    book = LogBook()

    # sys.argv - see on nimekiri sõnadest, mida kasutasid käivitamisel
    # sys.argv[0] on alati faili nimi (main.py)
    # sys.argv[1] on esimene käsk (add, list, gui jne)

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "add":
            add_entry_cli(book)
        elif command == "list":
            list_entries_cli(book)
        elif command == "gui":
            root = tk.Tk()
            app = LogBookApp(root, book)
            root.mainloop()
        else:
            print(f"Tundmatu käsk: {command}")
            print("Kasuta: add, list, gui või käivita ilma argumentideta menüü jaoks.")
    else:
        # Kui argumente pole, käivitame tavalise interaktiivse menüü
        run_cli(book)


if __name__ == "__main__":
    main()