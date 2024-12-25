from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QListWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from db_connection import db_cursor  # Импортируем наш модуль для работы с БД


class MoviesPage(QWidget):
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

        # Текст "Want to watch:"
        want_to_watch_label = QLabel("Want to watch:")
        want_to_watch_label.setAlignment(Qt.AlignCenter)
        want_to_watch_label.setFont(QFont("Lato", 20))
        want_to_watch_label.setStyleSheet("color: #716A5C;")

        # Поле ввода для добавления фильмов
        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(70)
        self.input_field.setStyleSheet(
            "background-color: #A39B8B; color: #07020D; border-radius: 25px; padding-left: 15px; font-size: 18px;"
        )

        # Кнопка добавления фильма
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
        add_button.clicked.connect(self.add_movie)

        # Подсказка
        hint_label = QLabel(
            "Click the movie to mark as watched/unwatched or press Delete to remove it from the list")
        hint_label.setWordWrap(True)
        hint_label.setAlignment(Qt.AlignCenter)
        hint_label.setFont(QFont("Lato", 24))
        hint_label.setStyleSheet("color: #A39B8B;")
        hint_label.setFixedWidth(568)

        # Добавление в макет
        left_layout.addWidget(self.title_label)
        left_layout.addSpacing(52)
        left_layout.addWidget(want_to_watch_label)
        left_layout.addSpacing(42)
        left_layout.addWidget(self.input_field)
        left_layout.addSpacing(48)
        left_layout.addWidget(add_button, alignment=Qt.AlignCenter)
        left_layout.addSpacing(160)
        left_layout.addWidget(hint_label)
        left_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Линия
        separator = QLabel()
        separator.setFixedWidth(2)
        separator.setStyleSheet("background-color: #E9E4DB;")

        # Правая часть: Список фильмов
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(15, 30, 30, 30)

        # Заголовок для списка фильмов
        list_label = QLabel("List:")
        list_label.setFont(QFont("Lato", 24))
        list_label.setStyleSheet("color: #716A5C;")

        # Список фильмов
        self.movie_list = QListWidget()
        self.movie_list.setStyleSheet(
            "background-color: #F1E9DB; color: #07020D; border: none; padding: 10px; font-size: 18px;"
        )

        # Добавление в макет
        right_layout.addWidget(list_label)
        right_layout.addWidget(self.movie_list)
        right_layout.setAlignment(Qt.AlignVCenter)

        # Основной макет
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(separator)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        self.movie_list.itemClicked.connect(self.toggle_movie_status)

        # Загружаем фильмы из базы данных при запуске
        self.load_movies_from_db()

    def add_movie(self):
        movie_name = self.input_field.text().strip()
        if movie_name:
            try:
                with db_cursor() as cursor:
                    cursor.execute("INSERT INTO Movies (title, is_watched) VALUES (?, ?);", (movie_name, False))
                self.input_field.clear()
                self.load_movies_from_db()  # Обновляем список после добавления
            except Exception as e:
                print(f"Error while adding movie: {e}")

    def load_movies_from_db(self):
        try:
            self.movie_list.clear()  # Очищаем список
            with db_cursor() as cursor:
                cursor.execute("SELECT id, title, is_watched FROM Movies;")
                movies = cursor.fetchall()
                for movie in movies:
                    item = QListWidgetItem(movie['title'])
                    item.setData(Qt.UserRole, movie['id'])  # Привязываем ID фильма к элементу
                    item.setData(Qt.UserRole + 1, movie['is_watched'])  # Привязываем статус фильма
                    item.setFont(QFont("Lato", 18))
                    item.setForeground(QColor("#A39B8B" if movie['is_watched'] else "#716A5C"))
                    self.movie_list.addItem(item)
        except Exception as e:
            print(f"Error while loading movies: {e}")

    def on_title_click(self, event):
        """Переход на главную страницу."""
        self.switch_to_main_page()

    def toggle_movie_status(self, item: QListWidgetItem):
        """Переключить статус фильма (просмотрено/не просмотрено)."""
        movie_id = item.data(Qt.UserRole)
        is_watched = item.data(Qt.UserRole + 1)
        try:
            new_status = not is_watched
            with db_cursor() as cursor:
                cursor.execute("UPDATE Movies SET is_watched = ? WHERE id = ?;", (new_status, movie_id))
            item.setData(Qt.UserRole + 1, new_status)
            item.setForeground(QColor("#A39B8B" if new_status else "#716A5C"))
        except Exception as e:
            print(f"Error while toggling movie status: {e}")

    def keyPressEvent(self, event):
        """Удаляет выбранный элемент при нажатии клавиши Delete."""
        if event.key() == Qt.Key_Delete:
            current_item = self.movie_list.currentItem()
            if current_item:
                movie_id = current_item.data(Qt.UserRole)
                try:
                    with db_cursor() as cursor:
                        cursor.execute("DELETE FROM Movies WHERE id = ?;", (movie_id,))
                    self.movie_list.takeItem(self.movie_list.row(current_item))
                except Exception as e:
                    print(f"Error while deleting movie: {e}")