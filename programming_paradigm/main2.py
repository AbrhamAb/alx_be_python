from library_management import Book, Library

def main():
    # Create a library
    library = Library()
    
    # Add some books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")
    
    # List available books
    library.list_available_books()
    
    # Check out a book
    library.check_out_book("The Great Gatsby")
    
    # List available books again
    library.list_available_books()
    
    # Return the book
    library.return_book("The Great Gatsby")
    
    # List available books one more time
    library.list_available_books()

if __name__ == "__main__":
    main()