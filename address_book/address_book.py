from collections import UserDict
from datetime import datetime, timedelta
from record import Record


class AddressBook(UserDict):

    def add_record(self, record):
        self.data.update({str(record.name).lower(): record})

    def find(self, name) -> Record:
        for record in self.data:
            if str(record).lower() == str(name).lower():
                return self.data[record]
        return None

    def delete(self, name) -> Record:
        name_lower = str(name).lower()
        if name_lower not in self.data:
            raise KeyError(f"Contact with name '{name}' not found.")
        return self.data.pop(name_lower)

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()
        week_later = today + timedelta(days=7)
        for user in self.data.values():
            if user.birthday is None:
                continue
            original_birthday = user.birthday.value
            birthday_this_year = datetime(
                today.year, original_birthday.month, original_birthday.day).date()
            if birthday_this_year < today:
                birthday_this_year = datetime(
                    today.year + 1, original_birthday.month, original_birthday.day).date()

            if today <= birthday_this_year <= week_later:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year += timedelta(
                        days=(7 - birthday_this_year.weekday()))
                upcoming_birthdays.append({
                    "name": user.name.value,
                    "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays if upcoming_birthdays else "There are no contacts for congratulation"
