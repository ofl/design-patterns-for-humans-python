# Iterator Pattern

class Book():
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name


class BookShelf():
    def __init__(self) -> None:
        self._books: list[Book] = []
        self._index: int = 0

    def append(self, book: Book):
        self._books.append(book)

    def __iter__(self):
        return self

    def __next__(self):
        if self._valid():
            value = self._books[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration()

    def _valid(self):
        return 0 <= self._index < len(self._books)


bookShelf = BookShelf()

bookShelf.append(Book("Around the World in 80 days"))
bookShelf.append(Book("Bible"))
bookShelf.append(Book("Cinderella"))
bookShelf.append(Book("Daddy-Long-Legs"))

for book in bookShelf:
    print(book.get_name())
