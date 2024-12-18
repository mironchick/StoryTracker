import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
from contextlib import contextmanager


# Функция для получения соединения с базой данных
def get_connection():
    return psycopg2.connect(
        dbname="postgres",  # Замените на имя вашей базы данных
        user="postgres",       # Замените на имя пользователя
        password="8806",    # Замените на ваш пароль
        host="localhost",            # Или адрес вашего сервера
        port=5432                    # Порт по умолчанию для PostgreSQL
    )


# Контекстный менеджер для безопасной работы с соединением
@contextmanager
def db_cursor():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        yield cursor
        conn.commit()  # Подтверждаем изменения
    except Exception as e:
        if conn:
            conn.rollback()  # Откат в случае ошибки
        raise e
    finally:
        if conn:
            conn.close()
