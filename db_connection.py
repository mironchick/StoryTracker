import sqlite3
from contextlib import contextmanager

DB_FILE = "storytracker.db"

@contextmanager
def db_cursor():
    """Контекстный менеджер для подключения к базе данных SQLite."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Позволяет работать с результатами как с dict
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def initialize_db():
    """Инициализация базы данных: создание таблиц, если они не существуют."""
    with db_cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            is_read BOOLEAN DEFAULT 0
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            is_watched BOOLEAN DEFAULT 0
        );
        """)

# Инициализация базы данных при импорте модуля
initialize_db()
