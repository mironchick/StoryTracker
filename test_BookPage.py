import pytest
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from main import MainWindow  # Импортируем MainWindow для использования функции переключения страниц
from BookPage import BookPage


@pytest.fixture
def app():
    """Создание и возвращение объекта приложения для тестов."""
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def window(app):
    """Создание экземпляра MainWindow и передача функции переключения на главную страницу в BookPage."""
    main_window = MainWindow()  # Создаем экземпляр главного окна
    main_window.show()  # Показываем окно
    return main_window


def test_book_page_button(window, app):
    """Тест на кнопки на странице с книгами."""

    # Передаем функцию show_main_page в BookPage
    window.books_page = BookPage(window.show_main_page)  # Передаем функцию для перехода на главную страницу
    window.books_page.show()  # Показываем страницу с книгами

    # Находим кнопку (замените на реальное имя кнопки, если оно отличается)
    button = window.books_page.findChild(QPushButton)
    assert button is not None  # Убедитесь, что кнопка существует

    # Эмулируем клик по кнопке
    QTest.mouseClick(button, Qt.LeftButton)

    # Обрабатываем события после клика
    QApplication.processEvents()
