from book import Book

library = [
    Book("Гарри Поттер -","Джоан Роулинг"),
    Book("Детство.Отрочество.Юность -", "Лев Николаевич Толстой"),
    Book("Недоросль -", "Фонвизин")
]

for book in library:
    print(book.name, book.autor)