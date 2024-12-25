# StoryTracker

## Скриншот приложения: 
![image](https://github.com/user-attachments/assets/7860199d-25bd-4f2c-885a-c21cea1d68cb)
![image](https://github.com/user-attachments/assets/8dd61a1c-b447-4e0a-bdfd-1d047942734a)
![image](https://github.com/user-attachments/assets/c7b79c6d-3cf9-44bf-8426-8af839e4b768)

## Использование приложения:

Пользователь выбирает нужную ему "категорию" между книгами и фильмами, а дальше вводит в строку нужное название. После появления названия в списке, пользователь может нажатием изменить статус "прочитанно/ не прочитанно". 

## Установка:

Установить программу Storytracker.exe (если ругается антивирус, то разрешите приложение или отключите его), запустите и пользуйтесь. Приятного пользования!

Если вы хотите использовать версию с PostgreSQL:
Скачать папку проекта (она находится в релизе для мини-проекта). Настроить базу данных в PostgreSQL, создать таблицы Books и Movies:
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_read BOOLEAN DEFAULT FALSE
);

CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_watched BOOLEAN DEFAULT FALSE
);

После поменяйте подключение к вашей БД в db_connection.py. Далее через PyInstaller создайте exe файл. Приятного пользования!
