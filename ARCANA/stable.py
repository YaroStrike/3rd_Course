import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import os
from PIL import Image, ImageTk

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
first_db = 'books_catalog.db'

def create_database():
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        cover_image TEXT NOT NULL,
        description TEXT NOT NULL,
        content TEXT NOT NULL
    );
    ''')
    
    connection.commit()
    connection.close()

create_database()

def fetch_books():
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

def show_details(book_id):
    # Скрываем каталог
    catalog_frame.pack_forget()
    
    # Получаем данные о книге
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    
    if book:
        # Создаем новый фрейм для отображения деталей книги
        details_frame = tk.Frame(window)
        details_frame.pack(pady=20)

        # Отображаем обложку книги
        try:
            image = Image.open(book[3])
            image = image.resize((200, 300), Image.LANCZOS)
            cover = ImageTk.PhotoImage(image)
            cover_label = tk.Label(details_frame, image=cover)
            cover_label.image = cover
            cover_label.grid(row=0, column=0, padx=70, pady=0)  # Размещаем обложку в верхнем левом углу
        except FileNotFoundError:
            print(f"Файл обложки {book[3]} не найден.")
            return

        # Отображаем информацию о книге
        details = f"Автор:             {book[2]}\nНазвание:     {book[1]}\nОписание:     {book[4]}"
        details_label = tk.Label(details_frame, text=details, font=("Arial", 14), justify='left')
        details_label.grid(row=0, column=1, padx=10, pady=10)  # Размещаем детали справа от обложки

        # Кнопка "Назад"
        back_button = tk.Button(details_frame, text="Назад", command=lambda: back_to_catalog(details_frame), font=("Arial", 14))
        back_button.grid(row=0, column=0, sticky='nw', padx=0, pady=2)  # Размещаем кнопку "Назад" вверху слева

def back_to_catalog(details_frame):
    details_frame.pack_forget()  # Скрываем детали книги
    catalog_frame.pack()  # Показываем каталог

def create_main_window():
    global window, catalog_frame
    window = tk.Tk()
    window.title("Каталог специальной литературы")
    window.geometry("840x680")  # стартовый размер окна
    
    catalog_frame = tk.Frame(window)
    catalog_frame.pack()

    books = fetch_books()
    
    for index, book in enumerate(books):
        try:
            image = Image.open(book[3])
            image = image.resize((153, 237), Image.LANCZOS)
            cover = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            continue  # Пропустить книгу, если обложка не найдена

        # Используем grid для размещения обложек
        row = index // 4  # 4 обложки в строке
        column = index % 4
        
        button = tk.Button(catalog_frame, image=cover, command=lambda id=book[0]: show_details(id))
        button.image = cover
        button.grid(row=row, column=column, padx=10, pady=(50, 0))  # Уменьшаем нижний отступ
        
        # Изменяем размещение метки с названием книги
        label = tk.Label(catalog_frame, text=book[1], font=("Arial", 12))
        label.grid(row=row + 1, column=column, padx=10, pady=(0, 10), sticky='n')  # Используем sticky для выравнивания по верху
    
    window.mainloop()

create_main_window()

def insert_book(title, author, cover_image, description, content):
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    
    # Проверяем, существует ли книга с таким же названием и автором
    cursor.execute("SELECT id FROM books WHERE title=? AND author=?", (title, author))
    existing_book = cursor.fetchone()
    
    if existing_book is None:  # Если книга не найдена, добавляем её
        try:
            cursor.execute("INSERT INTO books (title, author, cover_image, description, content) VALUES (?, ?, ?, ?, ?)",
                           (title, author, cover_image, description, content))
            connection.commit()
            print(f"Книга '{author} - {title}' успешно добавлена в базу данных '{first_db}'.")
        except Exception as e:
            print(f"Произошла ошибка при добавлении книги: {e}")
    else:
        print(f"Книга '{author} - {title}' уже существует в базе данных '{first_db}'.")
    
    connection.close()

# Пример добавления книги
insert_book("Программирование на Python", "Автор 3", "covers/cover1.png", "Описание книги 1", "Содержимое книги 1")
insert_book("Изучаем алгоритмы", "Автор 5", "covers/cover2.png", "Описание книги 2", "Содержимое книги 2")