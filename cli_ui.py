from models import LogEntry


def print_table(entries):
    """Kuvab kirjed tabelina koos lühikese ID ja kirjeldusega (punkt 3.3)."""
    if not entries:
        print("\n--- Kirjeid ei leitud ---")
        return

    # Määrame tabeli päise
    print("\n" + "=" * 110)
    print(f"{'ID':<4} | {'Aeg':<19} | {'Status':<7} | {'Pealkiri':<25} | {'Kirjeldus'}")
    print("-" * 110)

    for e in entries:
        # Kuvame kõik väljad, sh kirjeldus (e.description)
        # :<25 tähendab, et pealkirja jaoks jäetakse 25 kohta, et tabel püsiks sirge
        print(f"{e.entry_id:<4} | {e.created_at} | {e.status:<7} | {e.title:<25} | {e.description}")

    print("=" * 110)


def run_cli(book):
    while True:
        print("\n=== IT-MLog (CLI) ===")
        print("1. Lisa uus logikirje")
        print("2. Kuva kõik kirjed")
        print("3. Otsi märksõna järgi")
        print("4. Muuda staatust (kasuta ID-d)")
        print("5. Kustuta kirje (kasuta ID-d)")
        print("6. Salvesta ja välju")

        choice = input("\nVali tegevus (1-6): ")

        if choice == "1":
            print("\n--- UUE KIRJE LISAMINE ---")
            t = input("Pealkiri (min 4 tähemärki): ")
            d = input("Kirjeldus (min 10 tähemärki): ")

            valid, msg = LogEntry.validate(t, d)
            if valid:
                book.add_entry(t, d)
                print(">>> EDU: Kirje on lisatud!")
            else:
                print(f">>> VIGA: {msg}")
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "2":
            print("\nKÕIK LOGIRAAMATU KIRJED:")
            print_table(book.entries)
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "3":
            s = input("Sisesta otsingusõna: ")
            results = book.find_entries(s)
            print(f"\nOTSINGU TULEMUSED '{s}':")
            print_table(results)
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "4":
            idx = input("Sisesta kirje ID, mille staatust muuta: ")
            if idx.isdigit():
                if book.change_status(int(idx)):
                    print(f">>> EDU: Kirje {idx} staatus on muudetud!")
                else:
                    print(">>> VIGA: Sellise ID-ga kirjet ei leitud.")
            else:
                print(">>> VIGA: ID peab olema number.")
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "5":
            idx = input("Sisesta kirje ID, mida soovid kustutada: ")
            if idx.isdigit():
                book.delete_entry(int(idx))
                print(f">>> EDU: Kirje {idx} on eemaldatud.")
            else:
                print(">>> VIGA: ID peab olema number.")
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "6":
            book.save_to_json()
            print(">>> Andmed salvestatud faili logbook.json. Head aega!")
            break

        else:
            print(">>> Tundmatu valik. Proovi uuesti.")