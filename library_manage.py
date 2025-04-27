books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    books.append({'title': title, 'author': author, 'year': year})
    print(f"Book '{title}' added successfully!")

def view_books():
    if not books:
        print("No books found.")
        return
    for idx, book in enumerate(books):
        print(f"{idx + 1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        break
    else:
        print("Invalid choice! Please try again.")
