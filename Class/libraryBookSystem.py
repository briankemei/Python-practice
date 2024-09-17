class Library:

    def __init__(self):
        # Fixed initialization of the dictionary with correct key-value pair
        self.books = {"Kidagaa": {"Author": "Wala bin Walaa", "available": True}}

    '''Function to add books to the library dictionary'''
    def add_books(self, title, author):
        # Add a new book to the library dictionary
        self.books[title] = {"Author": author, "available": True}
        print(f"{title} by {author} has been added to the system")
    
    '''Method to check the book availability'''
    def borrow_book(self, title):
        if title in self.books:
            # Check if the book is available
            if self.books[title]["available"]:
                # If the book is available, mark it as borrowed
                self.books[title]["available"] = False
                print(f"You have successfully borrowed '{title}'.")
            else:
                print(f"The book '{title}' is not available.")
        else:
            print(f"The book '{title}' is not available in the library.")

    '''Function to reintegrate the book into the system'''
    def return_book(self, title):
        if title in self.books:
            if not self.books[title]["available"]:
                # Mark the book as returned
                self.books[title]["available"] = True
                print(f"You have successfully returned '{title}'. Thank you!")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' is not in the library.")

    '''Method to list all the books'''
    def list_books(self):
        for title, details in self.books.items():
            # Correct boolean check with capital 'True'
            available = "Available" if details["available"] else "Not available"
            print(f"Title: {title}, Author: {details['Author']}, Availability: {available}")


# Main section to handle user inputs
if __name__ == "__main__":
    my_library = Library()  # Create an instance of Library

    # Main loop to interact with the user
    while True:
        print("\nChoose from the menu:")
        print("0: Add a book")
        print("1: Borrow a book")
        print("2: Return a book")
        print("3: List all books")
        print("Enter your choice (or any other key to exit):")

        # User choice
        try:
            choice = int(input())  # Ask for user's menu choice
        except ValueError:
            print("Invalid input, exiting.")
            break

        if choice == 0:
            # Input for adding a book
            Name = input("Enter the name of the book: ")
            writer = input("Enter the writer of the book: ")
            my_library.add_books(Name, writer)
            print(my_library.books)
        elif choice == 1:
            # Input for borrowing a book
            Name = input("Enter the name of the book to borrow: ")
            my_library.borrow_book(Name)
        elif choice == 2:
            # Input for returning a book
            Name = input("Enter the name of the book to return: ")
            my_library.return_book(Name)
        elif choice == 3:
            # List all books
            my_library.list_books()
        else:
            print("Exiting the program.")
            break
