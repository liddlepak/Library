import json

from pprint import pprint
from typing import Union

EMPTY: int = 0
COUNT: int = 1
INDENT: int = 2
LAST_INDEX: int = -1
MESSAGE: str = "Книга с таким id-номером не существует!"

ACTION_DIGIT: dict = {
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
}


class Library:
    """Класс библиотеки."""

    def update_list(self, library: list) -> None:
        """Обновление библиотеки."""
        with open("library.json", "w") as file:
            json.dump(library, file, indent=INDENT, ensure_ascii=False)

    def list_books(self) -> list:
        """Список всех книг."""
        with open("library.json", "r") as file:
            library = json.load(file)
            return library

    def single_book(self, book_id: int):
        """Поиск книги по id."""
        library = self.list_books()
        for id, book in enumerate(library):
            if book["id"] == book_id:
                return (library, id, book)
        return None

    def search_book(self, choice: str) -> Union[dict, str]:
        """Поиск книги по автору, названию или году выпуска."""
        library = self.list_books()
        for book in library:
            if (choice.capitalize() in book.values()) or (
                choice.title() in book.values()
            ):
                return book
        return "Книга не найдена. Попробуйте еще раз."

    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавление книги в библиотеку."""
        library = self.list_books()
        if len(library) == EMPTY:
            id = COUNT
        else:
            id = library[LAST_INDEX]["id"] + COUNT
        data = {
            "id": id,
            "title": title.capitalize(),
            "author": author.title(),
            "year": year,
            "status": "В наличии",
        }
        library.append(data)
        self.update_list(library)
        print(f"Книга {title.capitalize()} добавлена в библиотеку!")

    def delete_book(self, book_id: int) -> None:
        """Удаление книги."""
        try:
            library, id, book = self.single_book(book_id)
            library.pop(id)
            print(f"Книга {book['title']} удалена из библиотеки")
            self.update_list(library)
        except TypeError:
            print(MESSAGE)

    def change_status_book(self, book_id: int) -> None:
        """Изменение статуса книги."""
        try:
            library, id, book = self.single_book(book_id)
            choice = input(
                "Введите новый статус книги (в наличии/выдана): "
            ).capitalize()
            if choice not in ("Выдана", "В наличии"):
                print("Введите корректный статус!")
            elif choice == book["status"]:
                print("Этот статус уже присвоен этой книге!")
            else:
                book["status"] = choice
                self.update_list(library)
                print(f"Статус книги {book['title']} изменен: {choice}")
        except TypeError:
            print(MESSAGE)


def main():
    """Главная функция."""
    lib = Library()

    while True:
        try:
            print(
                "\n"
                "Выберите действие:\n1. Поиск книги.\n"
                "2. Добавление книги.\n3. Удаление книги.\n"
                "4. Изменение статуса книги.\n5. Список всех книг.\n"
                "6. Выйти из библиотеки."
            )
            action = int(input("\nВведите действие: "))

            if action == ACTION_DIGIT["ONE"]:
                print("Напишите название, автора или год выпуска.")
                print(lib.search_book(input()))

            elif action == ACTION_DIGIT["TWO"]:
                title = input("Введите название книги: ")
                author = input("Введите имя автора: ")
                try:
                    year = int(input("Введите год выпуска: "))
                except ValueError:
                    print("Введите число!")
                    continue
                lib.add_book(title, author, str(year))

            elif action == ACTION_DIGIT["THREE"]:
                book_id = int(input("Введите id книги для удаления: "))
                lib.delete_book(book_id)

            elif action == ACTION_DIGIT["FOUR"]:
                book_id = int(input(
                    "Введите id книги для изменения статуса: "))
                lib.change_status_book(book_id)

            elif action == ACTION_DIGIT["FIVE"]:
                library = lib.list_books()
                if len(library) == EMPTY:
                    print("Библиотека пуста!")
                    continue
                pprint(library, sort_dicts=False)

            elif action == ACTION_DIGIT["SIX"]:
                print("До свидания!")
                break
        except ValueError:
            print("Введите число!")


if __name__ == "__main__":
    main()
