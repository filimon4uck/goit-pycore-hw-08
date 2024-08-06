from decorators import input_error
from record import Record
from datetime import datetime
from address_book import AddressBook
from custom_errors import NotFound


@input_error
def contacts_add(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        message = "Contact added."
    else:
        record.add_phone(phone)
    return message


@input_error
def contacts_change(args, book: AddressBook):
    name, old_phone, new_phone = args
    name_lower = name.lower()
    if not name.lower() in book:
        raise NotFound(f"Contact with name {name} not found")
    else:
        record = book.find(name_lower)
        record.edit_phone(old_phone, new_phone)
        return "Contact updated"


@input_error
def phone(args, book):
    name = args[0]
    if not name in book:
        raise NotFound(f"Contact with name {name} not found")
    else:
        return book[name].phones


@input_error
def all(book: AddressBook):
    if not len(book):
        raise NotFound(f"There not any contacts")
    return [{record.name.value: record.phones} for record in book.values()]


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        raise NotFound(f"Contact with name {name} not found")
    elif not record.birthday:
        record.add_birthday(birthday)
        return "Birthday added"
    return "Birthday was already added"


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if not record:
        raise NotFound(f"Contact with name {name} not found")
    elif record.birthday:
        return record.birthday.str_birthday()


@input_error
def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()
