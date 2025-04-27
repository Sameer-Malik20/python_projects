notes = []
def add_notes():
    title = input("enter note title: ")
    content = input("enter note content: ")
    notes.append({'title': title, 'content': content})
    print("note added successfully")

def view_notes():
    if not notes:
        print("no notes found")
        return 
    for idx, note in enumerate(notes):
        print(f"{idx+1}. {note['title']}: {note['content']}")

def search_notes():
    title = input("enter search title: ")
    for note in notes:
        if note['title'] == title:
            print(f"found: {note}")
            return
    print("note not found")

def update_notes():
    title = input("enter note title for update: ")
    for note in notes:
        if note['title'] == title:
            new_title = input("enter new note title: ")
            new_content = input("enter new note content: ")
            note['title'] = new_title
            note['content'] = new_content
            print("note updated successfully")
            return

def delete_notes():
    title = input("enter note title for delete: ")
    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            print("note deleted successfully")
            return
    print("note not found")


def save_notes_to_file(filename):
    with open(filename, 'w') as file:
        for note in notes:
            file.write(f"{note['title']}: {note['content']}\n")
    print(f"Notes saved to {filename}")

while True:
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Update Note")
    print("5. Delete Note")
    print("6. Save Notes to File")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_notes()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        search_notes()
    elif choice == '4':
        update_notes()
    elif choice == '5':
        delete_notes()
    elif choice == '6':
        filename = input("enter file name to save notes: ")
        save_notes_to_file(filename)
    elif choice == '7':
        break
    else:
        print("invalid choice")
