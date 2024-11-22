import unittest
import random

from library import Library

INDENT: int = 2
TEST_ID_BOOK: int = - 1
VALUES: tuple = ("title", "author", "0000", "any")


class Tests(unittest.TestCase):
    """Тестирование библиотеки."""

    @classmethod
    def setUpClass(cls):
        """Подготовка фикстур."""
        cls.lib = Library()
        cls.lib.add_book("title", "author", "0000")
        cls.list_book = cls.lib.list_books()
        cls.test_book = cls.list_book[TEST_ID_BOOK]
        cls.book_id = cls.test_book["id"]

    @classmethod
    def tearDownClass(cls):
        """Проверка удаления книги."""
        cls.lib.delete_book(cls.book_id)
        update_book_list = cls.lib.list_books()
        cls.assertTrue(
           (cls.test_book not in update_book_list), "Книга не была удалена")

    def test_add_book(self):
        """Тест добавления книги в библиотеку."""
        self.assertIn(
            self.test_book, self.list_book, "Книга не добавлена")
        self.assertTrue(
            self.test_book["year"].isdigit(), "Переменная не является числом")

    def test_search_book(self):
        """Тестирование поиска книги по параметрам."""
        value = random.choice(VALUES)
        book = self.lib.search_book(value)
        if value == "any":
            self.assertIsInstance(book, str, "Вернулась не строка")
        else:
            self.assertIsInstance(book, dict, "Объект не является словарем")

    def test_change_status_book(self):
        """Проверка изменения статуса книги."""
        old_status = self.test_book["status"]
        self.lib.change_status_book(self.book_id)
        self.assertNotEqual("Выдана", old_status, "Статус не поменялся")

    def test_list_book(self):
        """Проверка выдачи списка книг."""
        book_list = self.list_book
        self.assertIsInstance(book_list, list, "Объект не является списком")


unittest.main()
