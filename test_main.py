import pytest
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from main import MainWindow  # Импортируем MainWindow для использования функции переключения страниц


@pytest.fixture
def app():
    """Создание и возвращение объекта приложения для тестов."""
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def window(app):
    """Создание экземпляра MainWindow и передача функции переключения на главную страницу в MoviesPage."""
    main_window = MainWindow()  # Создаем экземпляр главного окна
    main_window.show()  # Показываем окно
    return main_window


def test_button_click_books(window, app):
    """Тест нажатия на кнопку 'See my books'."""

    # Находим кнопку по имени
    button = window.findChild(QPushButton, "See my books")
    assert button is not None  # Убедитесь, что кнопка существует

    # Эмулируем клик по кнопке
    QTest.mouseClick(button, Qt.LeftButton)

    # Обрабатываем события после клика
    QApplication.processEvents()

    # Проверяем, что при клике открылась страница с книгами
    assert window.stack.currentWidget() == window.books_page
