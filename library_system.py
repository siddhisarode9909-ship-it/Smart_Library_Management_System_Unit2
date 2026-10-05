"""
Smart Library Management System
Unit 2 - Python Programming (IBM)

This program demonstrates Strings, Lists, Tuples, Sets and Dictionaries.
"""

library = []


def add_book(book_id, title, author, category, isbn, price):
    """Add a new book if the Book ID is not already present."""
    for book in library:
        if book["book_id"] == book_id:
            print("Book already exists.")
            return

    isbn_tuple = tuple(isbn.split("-"))
    book = {
        "book_id": book_id.strip(),
        "title": title.strip().title(),
        "author": author.strip(),
        "category": category.strip().title(),
        "isbn": isbn_tuple,
        "price": price,
        "available": True
    }
    library.append(book)
    print("Book added successfully.")


def search_book(title):
    """Search for a book by title."""
    for book in library:
        if book["title"].lower() == title.strip().lower():
            display_book(book)
            return
    print("Book Not Found.")


def update_book(book_id):
    """Update the title, author, category, price or availability of a book."""
    for book in library:
        if book["book_id"] == book_id.strip():
            print("1. Title")
            print("2. Author")
            print("3. Category")
            print("4. Price")
            print("5. Availability")
            choice = input("Enter field number to update: ").strip()

            if choice == "1":
                book["title"] = input("Enter new title: ").strip().title()
            elif choice == "2":
                book["author"] = input("Enter new author: ").strip()
            elif choice == "3":
                book["category"] = input("Enter new category: ").strip().title()
            elif choice == "4":
                try:
                    book["price"] = float(input("Enter new price: "))
                except ValueError:
                    print("Invalid price.")
                    return
            elif choice == "5":
                value = input("Available? (yes/no): ").strip().lower()
                if value not in ("yes", "no"):
                    print("Invalid availability.")
                    return
                book["available"] = value == "yes"
            else:
                print("Invalid choice.")
                return

            print("Book updated successfully.")
            return

    print("Book Not Found.")


def delete_book(book_id):
    """Delete a book by Book ID."""
    for book in library:
        if book["book_id"] == book_id.strip():
            library.remove(book)
            print("Book deleted successfully.")
            return
    print("Book Not Found.")


def display_book(book):
    """Display one book record."""
    print("\n--- Book Details ---")
    print("Book ID:", book["book_id"])
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Category:", book["category"])
    print("ISBN:", "-".join(book["isbn"]))
    print("Price:", book["price"])
    print("Available:", "Yes" if book["available"] else "No")


def display_all_books():
    """Display all books in the catalogue."""
    if not library:
        print("Library is empty.")
        return

    print("\n===== ALL BOOKS =====")
    for book in library:
        print(
            f'{book["book_id"]} | {book["title"]} | '
            f'{book["author"]} | {book["category"]} | '
            f'Available: {"Yes" if book["available"] else "No"}'
        )


def unique_categories():
    """Return unique categories using a set."""
    return set(book["category"] for book in library)


def count_available_books():
    """Count books whose availability is True."""
    count = 0
    for book in library:
        if book["available"]:
            count += 1
    return count


def find_by_author(author_name):
    """Display all books written by the given author."""
    matches = []
    for book in library:
        if book["author"].lower() == author_name.strip().lower():
            matches.append(book)

    if not matches:
        print("No books found for this author.")
        return

    for book in matches:
        display_book(book)


def sort_books():
    """Display book titles in alphabetical order."""
    titles = [book["title"] for book in library]
    titles.sort()

    if titles:
        print("\n===== SORTED TITLES =====")
        for title in titles:
            print(title)
    else:
        print("Library is empty.")


def load_sample_data():
    """Add sample books for demonstration."""
    add_book(
        "B1001", "the great gatsby", "F. Scott Fitzgerald",
        "Fiction", "978-0743273565", 10.99
    )
    add_book(
        "B1002", "Dune", "Frank Herbert",
        "Sci-Fi", "978-0441172719", 14.50
    )
    add_book(
        "B1003", "Python Crash Course", "Eric Matthes",
        "Programming", "978-1593279288", 18.00
    )


def main():
    """Run the menu-driven Smart Library Management System."""
    load_sample_data()

    while True:
        print("\n========== SMART LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Display All Books")
        print("6. Find Books by Author")
        print("7. Show Unique Categories")
        print("8. Count Available Books")
        print("9. Sort Books Alphabetically")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            isbn = input("ISBN (example 978-1234567890): ")
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Invalid price.")
                continue
            add_book(book_id, title, author, category, isbn, price)

        elif choice == "2":
            search_book(input("Enter title to search: "))

        elif choice == "3":
            update_book(input("Enter Book ID to update: "))

        elif choice == "4":
            delete_book(input("Enter Book ID to delete: "))

        elif choice == "5":
            display_all_books()

        elif choice == "6":
            find_by_author(input("Enter author name: "))

        elif choice == "7":
            print("Unique Categories:", unique_categories())

        elif choice == "8":
            print("Available Books:", count_available_books())

        elif choice == "9":
            sort_books()

        elif choice == "10":
            print("Thank you for using the Smart Library Management System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 10.")


if __name__ == "__main__":
    main()
