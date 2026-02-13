import tkinter as tk
from logic import LogBook
from cli_ui import run_cli
from gui_ui import LogBookApp


def main():
    book = LogBook()  # Loome loogika eksemplari

    print("Vali režiim:")
    print("1. Konsool (CLI)")
    print("2. Graafiline (GUI)")

    choice = input("Sisesta valik (1/2): ")

    if choice == "1":
        run_cli(book)
    elif choice == "2":
        root = tk.Tk()
        app = LogBookApp(root, book)
        root.mainloop()
    else:
        print("Vale valik. Käivitan CLI...")
        run_cli(book)


if __name__ == "__main__":
    main()