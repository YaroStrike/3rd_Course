import tkinter as tk
from tkinter import messagebox
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
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    
    if book:
        details = f"Название: {book[1]}\nАвтор: {book[2]}\nОписание: {book[4]}"
        messagebox.showinfo("Подробности книги", details)

def create_main_window():
    window = tk.Tk()
    window.title("Каталог специальной литературы")
    
    books = fetch_books()
    
    for index, book in enumerate(books):
        image = Image.open(book[3])
        image = image.resize((153, 237), Image.LANCZOS)
        cover = ImageTk.PhotoImage(image)
        
        # Используем grid для размещения обложек
        row = index // 3  # 3 обложки в строке
        column = index % 3
        button = tk.Button(window, image=cover, command=lambda id=book[0]: show_details(id))
        button.image = cover
        button.grid(row=row, column=column, padx=10, pady=10)
        
        label = tk.Label(window, text=book[1])
        label.grid(row=row + 1, column=column)  # Название под обложкой
    
    window.mainloop()

create_main_window()

def insert_book(title, author, cover_image, description, content):
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    
    # Проверяем, существует ли книга с таким же названием и автором
    cursor.execute("SELECT * FROM books WHERE title=? AND author=?", (title, author))
    existing_book = cursor.fetchone()
    
    if existing_book is None:  # Если книга не найдена, добавляем её
        cursor.execute("INSERT INTO books (title, author, cover_image, description, content) VALUES (?, ?, ?, ?, ?)",
                       (title, author, cover_image, description, content))
        connection.commit()
    else:
        print(f"Книга '{author} - {title}' уже существует в базе данных '{first_db}' (пропуск).")
    
    connection.close()

# Пример добавления книги
insert_book("Программирование на Python", "Автор 3", "cover1.png", "Описание книги 1", "Содержимое книги 1")
insert_book("Изучаем алгоритмы", "Автор 4", "cover2.png", "Описание книги 2", "Содержимое книги 2")
