import os

def show_menu():
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Quit")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added!")

def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
            else:
                print("No notes found.")
    else:
        print("No notes found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
