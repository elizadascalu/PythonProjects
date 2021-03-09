class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    # properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # double-underscore properties are hidden from other classes
    __booklist = None

    # static methods
    # do not receive class or instance arguments
    # usually operate on data that is not instance- or class-specific

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # class methods
    # receive a class as their argument
    # can only operate on class-level data
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # instance methods
    # receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    # "self" is just a convention, it binds the attributes with the given argument
    def __init__(self, title, booktype, price, author=None):
        super().__init__(title, price)
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

        # Use references to other objects, like author and chapters =>> COMPOSITION
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

    def setDiscount(self, percent):
        self._discount = percent

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount / 100)
        else:
            return self.price

        #  __str__ function is used to return a user-friendly stringrepresentation of the object

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

        # The __repr__ function computes the “official” string reputation of an object

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

        # __ge__ establishes >= relationship with another obj

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return self.price >= value.price

        # __lt__ establishes <= relationship with another obj

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return self.price < value.price

        # __call__ calls the object like a function

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

        # Called when an attribute is retrieved. Be aware that you can't
        # directly access the attr name otherwise a recursive loop is created


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


# access the class attribute
print("Book types: ", Book.getbooktypes())

# create some author instances
auth = Author("Marin", "Preda")

# create some book instances
b1 = Book("Book1", "HARDCOVER", 100, auth)
b2 = Book("Book2", "PAPERBACK", 24, auth)

# use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

# use type() to inspect the object type
print(type(b1))
print(type(b2))

# compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(b2))

# use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(b2, Book))
print(isinstance(b2, object))

# price of book1
print("Price before discount: ", b1.getPrice())
b1.setDiscount(25)
print("Price after discount: ", b1.getPrice())

# try setting the discount
print("Price before discount: ", b2.getPrice())
b2.setDiscount(10)
print("Price after discount: ", b2.getPrice())

b1.addchapter(Chapter("Chapter 1", 10))
b1.addchapter(Chapter("Chapter 2", 45))
b1.addchapter(Chapter("Chapter 3", 24))

print("Book name: ", b1.title)
print("Author name: ", b1.author)
print("Page count: ", b1.getbookpagecount())

# print each object
print(b1)
print(b2)

# use str() and repr()
print(str(b1))
print(repr(b2))

# check for equality
print(b1 == b2)
# check for greater and lesser value
print(b2 >= b1)

# we can also sort them
books = [b1, b2]
books.sort()
print([book.title for book in books])

b1("New Title", "John Doe", 50.0)  # the __call__ function makes it happen
print(b1)
