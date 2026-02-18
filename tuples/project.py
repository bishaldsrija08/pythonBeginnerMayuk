'''
Create a simple Library Management System in Python that runs in the Command Prompt (CMD) and uses tuples to store book information. Each book should be stored as a tuple containing Book ID, Book Name, Author Name, and Price. The program should display a menu that allows the user to add a new book, view all books, search for a book by Book ID, update an existing book’s details, and remove a book from the library. Since tuples are immutable, when updating a book, the old tuple should be replaced with a new tuple containing the updated information. The program should continue running until the user chooses the exit option, and it should use only basic Python concepts such as input, print, tuples, loops, and conditional statements without using classes, files, or external libraries.

'''

# Library Management System using Tuple

# empty list to store book tuples
library = ()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        price = input("Enter Price: ")

        book = (book_id, name, author, price)
        library = library + (book,)   # add tuple to tuple

        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if len(library) == 0:
            print("No books in library.")
        else:
            print("\nBooks in Library:")
            for book in library:
                print("ID:", book[0], "| Name:", book[1], "| Author:", book[2], "| Price:", book[3])

    # Search Book
    elif choice == "3":
        search_id = input("Enter Book ID to search: ")
        found = False

        for book in library:
            if book[0] == search_id:
                print("Book found:")
                print("ID:", book[0], "| Name:", book[1], "| Author:", book[2], "| Price:", book[3])
                found = True
                break

        if not found:
            print("Book not found.")

    # Update Book
    elif choice == "4":
        update_id = input("Enter Book ID to update: ")
        new_library = ()
        found = False

        for book in library:
            if book[0] == update_id:
                print("Enter new details:")
                name = input("Enter Book Name: ")
                author = input("Enter Author Name: ")
                price = input("Enter Price: ")

                new_book = (update_id, name, author, price)
                new_library = new_library + (new_book,)
                found = True
            else:
                new_library = new_library + (book,)

        library = new_library

        if found:
            print("Book updated successfully!")
        else:
            print("Book not found.")

    # Remove Book
    elif choice == "5":
        remove_id = input("Enter Book ID to remove: ")
        new_library = ()
        found = False

        for book in library:
            if book[0] == remove_id:
                found = True
            else:
                new_library = new_library + (book,)

        library = new_library

        if found:
            print("Book removed successfully!")
        else:   
            print("Book not found.")

    # Exit
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
