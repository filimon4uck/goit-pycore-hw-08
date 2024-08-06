from field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, "%d.%m.%Y").date())
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def str_birthday(self):
        return datetime.strftime(self.value, "%d.%m.%Y")
