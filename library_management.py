import os

FILE_NAME = "library.txt"

# Ensure the file exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

def load_books():
    """Load all books from the text file into a list of dictionaries"""
    books = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                title, author, status = line.strip().split("|")
                books.append({"title": title, "author": author, "status": status})
    return books

def save_books(books):
    """Save all book records back to the file"""
    with open(FILE_NAME, "w") as file:
        for book in books:
            file.write(f"{book['title']}|{book['author']}|{book['status']}\n")

def add_book():
    """Add a new book to the library"""
    title = input("Enter Book Title: ").strip().title()
    author = input("Enter Author Name: ").strip().title()
    
    books = load_books()
    if any(book["title"] == title for book in books):
        print("⚠️ This book already exists in the library.")
        return

    books.append({"title": title, "author": author, "status": "Available"})
    save_books(books)
    print(f"✅ '{title}' by {author} added successfully.")

def borrow_book():
    """Mark a book as borrowed"""
    title = input("Enter the book title to borrow: ").strip().title()
    books = load_books()

    for book in books:
        if book["title"] == title:
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                save_books(books)
                print(f"📘 You borrowed '{title}'. Please return after reading.")
                return
            else:
                print("❌ This book is already borrowed.")
                return
    print("❌ Book not found in library.")

def return_book():
    """Return a borrowed book"""
    title = input("Enter the book title to return: ").strip().title()
    books = load_books()

    for book in books:
        if book["title"] == title:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                save_books(books)
                print(f"✅ '{title}' has been returned successfully.")
                return
            else:
                print("⚠️ This book was not borrowed.")
                return
    print("❌ Book not found in library.")

def display_books():
    """Display available and borrowed books separately"""
    books = load_books()
    available = [b for b in books if b["status"] == "Available"]
    borrowed = [b for b in books if b["status"] == "Borrowed"]

    print("\n📗 Available Books:")
    if available:
        for b in available:
            print(f" - {b['title']} by {b['author']}")
    else:
        print("No available books.")

    print("\n📕 Borrowed Books:")
    if borrowed:
        for b in borrowed:
            print(f" - {b['title']} by {b['author']}")
    else:
        print("No borrowed books.")
    print()

def main():
    """Main menu loop"""
    while True:
        print("\n=== 📚 LIBRARY MANAGEMENT MENU ===")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
