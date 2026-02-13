import json
import os
from models import LogEntry


class LogBook:
    def __init__(self, filename="logbook.json"):
        self.filename = filename
        self.entries = []
        self.load_from_json()

    def add_entry(self, entry):
        self.entries.append(entry)

    def delete_entry(self, created_at):
        self.entries = [e for e in self.entries if e.created_at != created_at]

    def find_entries(self, keyword):
        k = keyword.lower()
        return [e for e in self.entries if k in e.title.lower() or k in e.description.lower()]

    def filter_by_status(self, status):
        return [e for e in self.entries if e.status == status]

    def change_status(self, created_at):
        for e in self.entries:
            if e.created_at == created_at:
                e.status = "DONE" if e.status == "OPEN" else "OPEN"
                return True
        return False

    def save_to_json(self):
        """Salvestab kõik kirjed JSON faili."""
        data = [e.to_dict() for e in self.entries]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        """Laeb andmed failist ja käitleb puuduva faili viga (punkt 3.2)."""
        if not os.path.exists(self.filename):
            print("Teade: Andmefaili ei leitud, alustatakse tühja loendiga.")
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = [LogEntry(**item) for item in data]
                print(f"Laaditi {len(self.entries)} kirjet.")
        except Exception:
            print("Viga: Fail on vigane või tühi.")

    def import_from_test_file(self, file_path):
        """Vigase näidisfaili importimine ja logimine (punkt 4)."""
        if not os.path.exists(file_path):
            return "Faili ei leitud."

        errors = []
        imported = 0
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for item in data:
                title = item.get('title', '')
                desc = item.get('description', '')
                is_valid, msg = LogEntry.validate(title, desc)

                if is_valid:
                    self.add_entry(LogEntry(title, desc, item.get('status', 'OPEN')))
                    imported += 1
                else:
                    errors.append(f"VIGA: {msg} | Kirje: {title}\n")

            if errors:
                with open("import_errors.log", "w", encoding='utf-8') as ef:
                    ef.writelines(errors)
            return f"Imporditud {imported} kirjet. Vigade logi: import_errors.log"
        except:
            return "Vigane faili formaat."