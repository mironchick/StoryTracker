import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StoryTracker")
        self.setGeometry(100, 100, 1200, 800)  # Изменён размер окна
        self.setStyleSheet("background-color: #F1E9DB;")  # Цвет фона

        # Заголовок
        title_label = QLabel("StoryTracker")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Lato", 78, QFont.Bold))  # Изменён размер шрифта
        title_label.setStyleSheet("color: #716A5C;")  # Цвет заголовка

        # Приветственное сообщение
        welcome_label = QLabel("Welcome! What do you want to check out today?")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(QFont("Lato", 34))  # Установлен новый размер шрифта
        welcome_label.setStyleSheet("color: #A39B8B; font-weight: regular;")  # Установлен новый цвет текста
        welcome_label.setWordWrap(True)  # Включить перенос текста
        welcome_label.setMaximumSize(830, 150)  # Ограничиваем размер

        # Кнопки
        see_books_button = QPushButton("See my books")
        see_books_button.setFixedSize(752, 100)  # Изменён размер кнопок
        see_books_button.setFont(QFont("Lato", 28, QFont.Bold))  # Уменьшен размер шрифта кнопок
        see_books_button.setStyleSheet(
            "background-color: #5DB7DE; color: #07020D; font-weight: bold; border-radius: 25px;"
        )

        see_movies_button = QPushButton("See my movies")
        see_movies_button.setFixedSize(752, 100)
        see_movies_button.setFont(QFont("Lato", 28, QFont.Bold))
        see_movies_button.setStyleSheet(
            "background-color: #5DB7DE; color: #07020D; font-weight: bold; border-radius: 25px;"
        )

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

        # Макет
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 30, 50, 30)  # Уменьшены отступы
        layout.setAlignment(Qt.AlignCenter)  # Выравнивание всего макета по центру

        # Добавление элементов в макет
        layout.addWidget(title_label)
        layout.addSpacing(65)  # Расстояние между заголовком и приветствием
        layout.addWidget(welcome_label)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(see_books_button)
        layout.addSpacing(28)  # Расстояние между кнопками
        layout.addWidget(see_movies_button)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
