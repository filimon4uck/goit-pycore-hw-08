
from command_parser import parse_input
import contacts
from serialize import load_data, save_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == 'add':
            print(contacts.contacts_add(args, book))
        elif command == 'change':
            print(contacts.contacts_change(args, book))
        elif command == "phone":
            print(contacts.phone(args, book))
        elif command == 'all':
            print(contacts.all(book))
        elif command == 'add-birthday':
            print(contacts.add_birthday(args, book))
        elif command == 'show-birthday':
            print(contacts.show_birthday(args, book))

        elif command == 'birthdays':
            print(contacts.birthdays(book))
        else:
            print("Invalid command.")


if (__name__ == "__main__"):
    main()
