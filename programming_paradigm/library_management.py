class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)
        print(f"Added book: '{title}' by {author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"Checked out: '{title}'")
                    return True
                else:
                    print(f"'{title}' is already checked out")
                    return False
        print(f"Book not found: '{title}'")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"Returned: '{title}'")
                    return True
                else:
                    print(f"'{title}' is already available")
                    return False
        print(f"Book not found: '{title}'")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No available books in the library")
            return
        
        print("Available Books:")
        for i, book in enumerate(available_books, 1):
            print(f"  {i}. '{book.title}' by {book.author}")