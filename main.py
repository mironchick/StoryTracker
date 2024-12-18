import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QStackedWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from BookPage import BookPage
from MoviesPage import MoviesPage  # Импортируем страницу фильмов


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StoryTracker")
        self.setGeometry(100, 100, 1200, 800)  # Размер окна
        self.setStyleSheet("background-color: #F1E9DB;")  # Цвет фона

        # Stack for switching pages
        self.stack = QStackedWidget()

        # Main Page
        main_page = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 30, 50, 30)
        main_layout.setAlignment(Qt.AlignCenter)

        # Заголовок
        title_label = QLabel("StoryTracker")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Lato", 78, QFont.Bold))
        title_label.setStyleSheet("color: #716A5C;")

        # Приветственное сообщение
        welcome_label = QLabel("Welcome! What do you want to check out today?")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(QFont("Lato", 34))
        welcome_label.setStyleSheet("color: #A39B8B; font-weight: regular;")
        welcome_label.setWordWrap(True)
        welcome_label.setMaximumSize(830, 150)

        # Кнопка "See my books"
        see_books_button = QPushButton("See my books")
        see_books_button.setFixedSize(752, 100)
        see_books_button.setFont(QFont("Lato", 28, QFont.Bold))
        see_books_button.setStyleSheet("""
            QPushButton {
                background-color: #5DB7DE;
                color: #07020D;
                font-weight: bold;
                border-radius: 25px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5D86DE;
            }
        """)
        see_books_button.clicked.connect(self.show_books_page)

        # Кнопка "See my movies"
        see_movies_button = QPushButton("See my movies")
        see_movies_button.setFixedSize(752, 100)
        see_movies_button.setFont(QFont("Lato", 28, QFont.Bold))
        see_movies_button.setStyleSheet("""
            QPushButton {
                background-color: #5DB7DE;
                color: #07020D;
                font-weight: bold;
                border-radius: 25px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5D86DE;
            }
        """)
        see_movies_button.clicked.connect(self.show_movies_page)  # Привязка к функции

        # Добавление элементов в макет главной страницы
        main_layout.addWidget(title_label)
        main_layout.addSpacing(65)
        main_layout.addWidget(welcome_label)
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addWidget(see_books_button)
        main_layout.addSpacing(28)
        main_layout.addWidget(see_movies_button)
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        main_page.setLayout(main_layout)

        # Add pages to the stack
        self.stack.addWidget(main_page)

        # Создание страниц и добавление их в стек
        self.books_page = BookPage(self.show_main_page)
        self.movies_page = MoviesPage(self.show_main_page)  # Экземпляр MoviePage

        self.stack.addWidget(self.books_page)
        self.stack.addWidget(self.movies_page)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

    def show_books_page(self):
        """Показать страницу с книгами."""
        self.stack.setCurrentWidget(self.books_page)

    def show_movies_page(self):
        """Показать страницу с фильмами."""
        self.stack.setCurrentWidget(self.movies_page)

    def show_main_page(self):
        """Показать главную страницу."""
        self.stack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())