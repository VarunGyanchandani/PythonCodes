import datetime
from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, runtime):
        super().__init__(title, item_id)
        self.director = director
        self.runtime = runtime

    def __str__(self):
        return f"DVD: {self.title} directed by {self.director}"

class Library:
    def __init__(self):
        self.items = {}

    @log_action
    def add_item(self, item):
        self.items[item.item_id] = item

    @log_action
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    @log_action
    def check_out_item(self, item_id):
        if item_id in self.items:
            return self.items[item_id].check_out()
        return False

    @log_action
    def return_item(self, item_id):
        if item_id in self.items:
            return self.items[item_id].return_item()
        return False

    def list_items(self):
        for item in self.items.values():
            print(f"{item} - {'Checked Out' if item.checked_out else 'Available'}")

def main():
    library = Library()

    # Adding items to the library
    book1 = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "B002", "Harper Lee", "9780446310789")
    dvd1 = DVD("Inception", "D001", "Christopher Nolan", 148)

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)

    # Listing all items
    print("Library Inventory:")
    library.list_items()

    # Checking out and returning items
    print("\nChecking out 'The Great Gatsby'...")
    library.check_out_item("B001")

    print("\nUpdated Library Inventory:")
    library.list_items()

    print("\nReturning 'The Great Gatsby'...")
    library.return_item("B001")

    print("\nTrying to check out a non-existent item...")
    if not library.check_out_item("B003"):
        print("Item not found in the library.")

    print("\nRemoving 'Inception' from the library...")
    library.remove_item("D001")

    print("\nFinal Library Inventory:")
    library.list_items()

if __name__ == "__main__":
    main()