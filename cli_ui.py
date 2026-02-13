from models import LogEntry


def print_formatted_entries(entries):
    """Abifunktsioon kirjete kuvamiseks vastavalt punktile 3.3."""
    if not entries:
        print("\n--- Kirjeid ei leitud ---")
        return

    print("\n" + "=" * 80)
    for e in entries:
        # TÄPNE FORMAT: aeg | [status] | pealkiri | kirjeldus
        print(f"{e.created_at} | [{e.status}] | {e.title} | {e.description}")
    print("=" * 80)


def run_cli(book):
    while True:
        print("\n--- IT-MLog (CLI) ---")
        print("1. Lisa uus logikirje")
        print("2. Kuva kõik logikirjed")
        print("3. Otsi märksõna järgi")
        print("4. Filtreeri staatuse järgi (OPEN/DONE)")
        print("5. Muuda kirje staatust")
        print("6. Kustuta kirje")
        print("7. Salvesta andmed ja välju")

        choice = input("\nVali tegevus (1-7): ")

        if choice == "1":
            t = input("Sisesta pealkiri (min 4 tähemärki): ")
            d = input("Sisesta kirjeldus (min 10 tähemärki): ")

            valid, msg = LogEntry.validate(t, d)
            if valid:
                book.add_entry(LogEntry(t, d))
                print(">>> Kirje edukalt lisatud!")
            else:
                print(f">>> VIGA: {msg}")

        elif choice == "2":
            print("\nKÕIK KIRJED:")
            print_formatted_entries(book.entries)

        elif choice == "3":
            s = input("Sisesta otsingusõna (pealkiri või kirjeldus): ")
            results = book.find_entries(s)
            print(f"\nOTSINGU TULEMUSED '{s}':")
            print_formatted_entries(results)

        elif choice == "4":
            stat = input("Millist staatust kuvada? (OPEN/DONE): ").upper()
            if stat in ["OPEN", "DONE"]:
                results = book.filter_by_status(stat)
                print(f"\nFILTREERITUD: {stat}")
                print_formatted_entries(results)
            else:
                print(">>> Vale staatus! Kasuta ainult OPEN või DONE.")

        elif choice == "5":
            id_val = input("Sisesta muudetava kirje aeg (ID täpselt nii nagu tabelis): ")
            if book.change_status(id_val):
                print(">>> Staatus muudetud!")
            else:
                print(">>> Kirjet ei leitud. Kontrolli kellaaega.")

        elif choice == "6":
            id_val = input("Sisesta kustutatava kirje aeg (ID): ")
            confirm = input(f"Kas oled kindel, et soovid kustutada kirje {id_val}? (j/n): ")
            if confirm.lower() == 'j':
                book.delete_entry(id_val)
                print(">>> Kirje kustutatud.")

        elif choice == "7":
            book.save_to_json()
            print(">>> Andmed salvestatud faili logbook.json. Head aega!")
            break

        else:
            print(">>> Tundmatu valik, proovi uuesti.")