# ---- Library Management System ----

class Library:

    # STEP 1 - Parameterized Constructor: runs when the library is created
    def __init__(self, name, section):
        self.name = name
        self.section = section
        self.books = []
        print(f"Library '{self.name}' ({self.section}) is ready!")

    # STEP 2 - Add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book}' added to {self.name}.")

    # STEP 3 - Remove a book from the library
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' removed.")
        else:
            print(f"'{book}' not found in library.")

    # STEP 4 - Display all books
    def display(self):
        print(f"\n--- {self.name} ({self.section}) ---")
        if self.books:
            for i, book in enumerate(self.books, 1):
                print(f"  {i}. {book}")
        else:
            print("  No books yet. Add some!")

    # STEP 5 - Destructor: runs when the library object is deleted
    def __del__(self):
        print(f"Library '{self.name}' has been deleted. Goodbye!")


# Object Creation (constructor fires here)
my_library = Library("City Library", "Fiction")

# STEP 6 - Menu-driven program using the Library class
while True:
    print("\n1. Add Book  2. Remove Book  3. View Library  4. Delete & Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        my_library.add_book(book)

    elif choice == "2":
        book = input("Enter book to remove: ")
        my_library.remove_book(book)

    elif choice == "3":
        my_library.display()

    elif choice == "4":
        del my_library
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")
