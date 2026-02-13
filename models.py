import datetime


class LogEntry:
    def __init__(self, entry_id, title, description, status="OPEN", created_at=None):
        self.entry_id = entry_id  # Lühike numbriline ID
        if created_at is None:
            self.created_at = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        else:
            self.created_at = created_at

        self.title = title
        self.description = description
        self.status = status

    @staticmethod
    def validate(title, description):
        if len(title) < 4:
            return False, "Pealkiri peab olema vähemalt 4 tähemärki pikk."
        if len(description) < 10:
            return False, "Kirjeldus peab olema vähemalt 10 tähemärki pikk."
        return True, ""

    def to_dict(self):
        return {
            "id": self.entry_id,  # Salvestame ka ID
            "created_at": self.created_at,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }