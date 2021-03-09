from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
# "frozen" parameter makes the class immutable
class Book:
    title: str
    author: str
    pages: int
    price: float = field(default_factory=price_func)

    # __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("Book1 Title", "Author1 Name",  1225)
b2 = Book("Book2 Title", "Author2 Name",  234, 24.0)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses provide a default
# implementation of the __repr__ function
print(b1)
print(b2)

# comparing two dataclasses
b3 = Book("Book3 Title", "Author3 Name", 234, 43.2)
print(b1 == b3)

# change some fields, call a regular class method
b1.title = "New Book Title"
b1.pages = 600
print(b1.bookinfo())

print(b1.description)
print(b2.description)