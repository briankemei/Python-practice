'''Simple library management system'''
class library:

    def __init__(self):
        self.books = {}

    '''Function to add books to the library dictionary'''
    def add_books(self,title,author):
        self.books[title]={"Author":author,"available":True}
        print(f"{title}by {author} has been added to the system")
    
    '''Method to check the book availability'''
    def borrow_book(self,title):
        if title in self.books:
            #Check the availability of the book
            if self.books[title]["available"]:
                #if the book is avialable set it to false
                self.books[title]["available"]=False
                print(f"You have successfully borrowed {title} the book")
            else:
                print("The book is not available")
        else:
            print(f"The book is not available {title}")
    # Function to reintergrate the book into the system
    def return_book(self,title):
        if title in self.books:
            if not self.books[title]["available"]:
                self.books[title]["available"]=True
                print(f"You have successfully returned {title}. Thank you!")
            else:
                print(f"{title} This is not the correct book")
        else:
            print("Please return the book")
    def list_books(self):
        for title, author in self.books.items():
            available = "True" if author["available"] else false
            print(f"{title} of the books, author is: {author} and the book availability is Available")         



            
if __name__ == "__main__":
    my_library = library()
        
        #'''Asking for the book name and author '''
    
    
    while True:
        print("Choose the menu\n 0: Add a book: \n 1: Return a booK \n 2: Check books list\n Enter your choice:   ")
        choice= int(input())
        Name = input("Enter the name of the books: ")
        writer = input ("Enter the writer of the book: ")
        
        if choice == 0: 
            my_library.add_books(Name, writer)
            print(my_library.books)
        elif choice==1:
            my_library.borrow_book(Name)
        elif choice==2:
            my_library.return_book(Name)
        elif choice ==3:
            my_library.list_books()
        else:
            print("Wrong choice.")
