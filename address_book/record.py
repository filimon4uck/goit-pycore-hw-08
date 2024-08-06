from name import Name
from phone import Phone
from birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for phone_item in self.phones:
            if phone_item.value == phone:
                return self.phones.remove(phone_item)
            else:
                raise ValueError(f"Phone number {phone} not found")

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index].value = Phone(new_phone)
                return "Phone number changed"
        raise ValueError(f"{old_phone} not found")

    def find_phone(self, phone):
        for phone_item in self.phones:
            if phone_item.value == phone:
                return phone_item
        raise ValueError(f"Phone number {phone} not found")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
