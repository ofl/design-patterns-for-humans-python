class Book():
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name


bookShelf = []

bookShelf.append(Book("Around the World in 80 days"))
bookShelf.append(Book("Bible"))
bookShelf.append(Book("Cinderella"))
bookShelf.append(Book("Daddy-Long-Legs"))

for book in bookShelf:
    print(book.get_name())
