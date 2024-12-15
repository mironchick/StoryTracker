from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class BookPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #F1E9DB;")  # Цвет фона

        # Левая часть: Ввод и кнопка
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(30, 30, 15, 30)  # Отступы слева

        # Заголовок страницы
        title_label = QLabel("StoryTracker")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Lato", 48, QFont.Bold))
        title_label.setStyleSheet("color: #716A5C;")  # Цвет заголовка

        # Текст "Want to read:"
        want_to_read_label = QLabel("Want to read:")
        want_to_read_label.setAlignment(Qt.AlignCenter)
        want_to_read_label.setFont(QFont("Lato", 20))
        want_to_read_label.setStyleSheet("color: #716A5C;")

        # Поле ввода для добавления книг
        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(70)
        self.input_field.setStyleSheet(
            "background-color: #A39B8B; color: #07020D; border-radius: 25px; padding-left: 15px; font-size: 18px;"
        )

        # Кнопка добавления книги
        add_button = QPushButton("Add")
        add_button.setFixedSize(476, 81)
        add_button.setFont(QFont("Lato", 28, QFont.Bold))
        add_button.setStyleSheet("""
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
        add_button.clicked.connect(self.add_book)

        # Подсказка под кнопкой
        hint_label = QLabel("Click the check mark to mark what you have read or the cross to remove the book from the list")
        hint_label.setWordWrap(True)
        hint_label.setAlignment(Qt.AlignCenter)
        hint_label.setFont(QFont("Lato", 24))
        hint_label.setStyleSheet("color: #A39B8B;")
        hint_label.setFixedWidth(568)

        # Добавление элементов в левый макет
        left_layout.addWidget(title_label)
        left_layout.addSpacing(52)
        left_layout.addWidget(want_to_read_label)
        left_layout.addSpacing(42)
        left_layout.addWidget(self.input_field)
        left_layout.addSpacing(48)
        left_layout.addWidget(add_button, alignment=Qt.AlignCenter)
        left_layout.addSpacing(160)
        left_layout.addWidget(hint_label)
        left_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Разделительная линия
        separator = QLabel()
        separator.setFixedWidth(1)
        separator.setStyleSheet("background-color: #E9E4DB;")

        # Правая часть: Список книг
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(15, 30, 30, 30)  # Отступы справа

        self.book_list = QListWidget()
        self.book_list.setStyleSheet(
            "background-color: #FFFFFF; color: #07020D; border: none; padding: 10px; font-size: 18px;"
        )

        right_layout.addWidget(self.book_list)
        right_layout.setAlignment(Qt.AlignVCenter)

        # Основной горизонтальный макет
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(separator)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

    def add_book(self):
        book_name = self.input_field.text().strip()
        if book_name:
            self.book_list.addItem(book_name)
            self.input_field.clear()
