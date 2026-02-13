import json
import os
from models import LogEntry

class LogBook:
    def __init__(self, filename="logbook.json"):
        self.filename = filename
        self.entries = []
        self.load_from_json()

    def get_next_id(self):
        """Leiab järgmise vaba ID."""
        if not self.entries:
            return 1
        return max(e.entry_id for e in self.entries) + 1

    def add_entry(self, title, description):
        """Loob uue kirje automaatse ID-ga."""
        new_id = self.get_next_id()
        new_entry = LogEntry(new_id, title, description)
        self.entries.append(new_entry)
        return new_entry

    def delete_entry(self, entry_id):
        """Kustutab kirje lühikese ID järgi."""
        self.entries = [e for e in self.entries if e.entry_id != int(entry_id)]

    def change_status(self, entry_id):
        """Muudab staatust lühikese ID järgi."""
        for e in self.entries:
            if e.entry_id == int(entry_id):
                e.status = "DONE" if e.status == "OPEN" else "OPEN"
                return True
        return False

    def find_entries(self, keyword):
        k = keyword.lower()
        return [e for e in self.entries if k in e.title.lower() or k in e.description.lower()]

    def filter_by_status(self, status):
        return [e for e in self.entries if e.status == status]

    def save_to_json(self):
        data = [e.to_dict() for e in self.entries]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = []
                for item in data:
                    # Loome objekti, kasutades failist loetud ID-d
                    e = LogEntry(item['id'], item['title'], item['description'], item['status'], item['created_at'])
                    self.entries.append(e)
        except:
            self.entries = []