import datetime


class LogEntry:
    def __init__(self, title, description, status="OPEN", created_at=None):
        # created_at on unikaalne ID. Kui seda pole, loome uue.
        if created_at is None:
            self.created_at = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        else:
            self.created_at = created_at

        self.title = title
        self.description = description
        self.status = status

    @staticmethod
    def validate(title, description):
        """Andmete valideerimine vastavalt reeglitele (punkt 2.1)."""
        if len(title) < 4:
            return False, "Pealkiri peab olema vähemalt 4 tähemärki pikk."
        if len(description) < 10:
            return False, "Kirjeldus peab olema vähemalt 10 tähemärki pikk."
        return True, ""

    def to_dict(self):
        """Muudab objekti sõnastikuks JSON salvestamiseks."""
        return {
            "created_at": self.created_at,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }