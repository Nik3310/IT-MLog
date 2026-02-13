from models import LogEntry


def print_table(entries):
    """Kuvab kirjed tabelina, piirates kirjelduse pikkust."""
    if not entries:
        print("\n--- Kirjeid ei leitud ---")
        return

    # Päis fikseeritud laiustega
    print("\n" + "=" * 105)
    print(f"{'ID':<4} | {'Aeg':<19} | {'Olek':<7} | {'Pealkiri':<20} | {'Kirjeldus'}")
    print("-" * 105)

    for e in entries:
        # Piirame kirjelduse ja pealkirja pikkust, et tabel ei laguneks
        desc = (e.description[:42] + "...") if len(e.description) > 45 else e.description
        title = (e.title[:17] + "...") if len(e.title) > 20 else e.title

        print(f"{e.entry_id:<4} | {e.created_at} | {e.status:<7} | {title:<20} | {desc}")

    print("=" * 105)


def add_entry_cli(book):
    """Funktsioon uue kirje lisamiseks."""
    print("\n--- UUE KIRJE LISAMINE ---")
    t = input("Pealkiri (min 4 tähemärki): ")
    d = input("Kirjeldus (min 10 tähemärki): ")

    valid, msg = LogEntry.validate(t, d)
    if valid:
        book.add_entry(t, d)
        print(">>> EDU: Kirje on lisatud!")
    else:
        print(f">>> VIGA: {msg}")


def list_entries_cli(book):
    """Funktsioon kõikide kirjete kuvamiseks."""
    print("\nKÕIK LOGIRAAMATU KIRJED:")
    print_table(book.entries)


def run_cli(book):
    """Interaktiivne menüü koos Enteri vajutamise nõudega."""
    while True:
        # Sinu soovitud menüü tekst
        print("\n=== IT-MLog (CLI) ===")
        print("1. Lisa uus logikirje")
        print("2. Kuva kõik kirjed")
        print("3. Otsi märksõna järgi")
        print("4. Muuda staatust (kasuta ID-d)")
        print("5. Kustuta kirje (kasuta ID-d)")
        print("6. Salvesta ja välju")

        choice = input("\nVali tegevus (1-6): ")

        if choice == "1":
            add_entry_cli(book)
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "2":
            list_entries_cli(book)
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "3":
            s = input("Sisesta otsingusõna: ")
            results = book.find_entries(s)
            print_table(results)
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "4":
            idx = input("Sisesta kirje ID staatuse muutmiseks: ")
            if idx.isdigit():
                if book.change_status(int(idx)):
                    print(f">>> EDU: Kirje {idx} staatus muudetud!")
                else:
                    print(">>> VIGA: ID-d ei leitud.")
            else:
                print(">>> VIGA: ID peab olema number.")
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "5":
            idx = input("Sisesta kirje ID kustutamiseks: ")
            if idx.isdigit():
                book.delete_entry(int(idx))
                print(f">>> EDU: Kirje {idx} on kustutatud.")
            else:
                print(">>> VIGA: ID peab olema number.")
            input("\nVajuta Enter, et naasta menüüsse...")

        elif choice == "6":
            book.save_to_json()
            print(">>> Andmed salvestatud. Head aega!")
            break

        else:
            print(">>> Tundmatu valik, proovi uuesti.")