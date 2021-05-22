class Book():
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name


class BookShelf():
    def __init__(self) -> None:
        self._books: list[Book] = []

    def append(self, book: Book):
        self._books.append(book)

    def get_book_at(self, index):
        return self._books[index]

    def is_valid(self, index):
        return 0 <= index < len(self._books)


bookShelf = BookShelf()

bookShelf.append(Book("Around the World in 80 days"))
bookShelf.append(Book("Bible"))
bookShelf.append(Book("Cinderella"))
bookShelf.append(Book("Daddy-Long-Legs"))

index = 0

while bookShelf.is_valid(index):
    book = bookShelf.get_book_at(index)
    print(book.get_name())
    index += 1
