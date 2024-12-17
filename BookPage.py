from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QListWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class BookPage(QWidget):
    def __init__(self, switch_to_main_page):
        super().__init__()

        self.switch_to_main_page = switch_to_main_page  # Передача функции переключения

        self.setStyleSheet("background-color: #F1E9DB;")  # Цвет фона

        # Левая часть: Ввод и кнопка
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(30, 30, 15, 30)

        # Заголовок страницы
        self.title_label = QLabel("StoryTracker")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Lato", 48, QFont.Bold))
        self.title_label.setStyleSheet("""
            color: #716A5C;
            cursor: pointer;  /* Указывает, что элемент интерактивный */
        """)
        self.title_label.mousePressEvent = self.on_title_click  # Привязка клика

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

        # Подсказка
        hint_label = QLabel(
            "Click the check mark to mark what you have read or the cross to remove the book from the list")
        hint_label.setWordWrap(True)
        hint_label.setAlignment(Qt.AlignCenter)
        hint_label.setFont(QFont("Lato", 24))
        hint_label.setStyleSheet("color: #A39B8B;")
        hint_label.setFixedWidth(568)

        # Добавление в макет
        left_layout.addWidget(self.title_label)
        left_layout.addSpacing(52)
        left_layout.addWidget(want_to_read_label)
        left_layout.addSpacing(42)
        left_layout.addWidget(self.input_field)
        left_layout.addSpacing(48)
        left_layout.addWidget(add_button, alignment=Qt.AlignCenter)
        left_layout.addSpacing(160)
        left_layout.addWidget(hint_label)
        left_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Линия
        separator = QLabel()
        separator.setFixedWidth(1)
        separator.setStyleSheet("background-color: #E9E4DB;")

        # Правая часть: Список книг
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(15, 30, 30, 30)

        # Заголовок для списка книг
        list_label = QLabel("List:")
        list_label.setFont(QFont("Lato", 24))
        list_label.setStyleSheet("color: #716A5C;")

        # Список книг
        self.book_list = QListWidget()
        self.book_list.setStyleSheet(
            "background-color: #F1E9DB; color: #07020D; border: none; padding: 10px; font-size: 18px;"
        )

        # Добавление в макет
        right_layout.addWidget(list_label)
        right_layout.addWidget(self.book_list)
        right_layout.setAlignment(Qt.AlignVCenter)

        # Основной макет
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(separator)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        self.book_list.itemClicked.connect(self.toggle_book_status)

    def add_book(self):
        book_name = self.input_field.text().strip()
        if book_name:
            try:
                # Создание элемента списка
                item = QListWidgetItem(book_name)
                item.setFont(QFont("Lato", 18))  # Устанавливаем шрифт размером 18
                item.setForeground(QColor("#716A5C"))  # Устанавливаем цвет текста

                # Добавление элемента в список
                self.book_list.addItem(item)

                # Очищаем поле ввода после добавления
                self.input_field.clear()

            except Exception as e:
                print(f"Error while adding book: {e}")

    def on_title_click(self, event):
        """Переход на главную страницу."""
        self.switch_to_main_page()

    def toggle_book_status(self, item: QListWidgetItem):
        """Переключить статус книги (прочитано/не прочитано)."""
        if item.data(Qt.UserRole) is None:  # Если книга не прочитана
            item.setForeground(QColor("#A39B8B"))  # Меняем цвет текста
            item.setData(Qt.UserRole, True)  # Устанавливаем статус прочитано
            item.setText(f"{item.text()}")
        elif item.data(Qt.UserRole):
            item.setForeground(QColor("#716A5C"))  # Меняем цвет текста
            item.setData(Qt.UserRole, None)
            item.setText(f"{item.text()}")