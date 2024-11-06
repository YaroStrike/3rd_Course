import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def create_database():
    connection = sqlite3.connect('books_catalog.db')
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
    connection = sqlite3.connect('books_catalog.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

def show_details(book_id):
    connection = sqlite3.connect('books_catalog.db')
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
    
    for book in books:
        cover = PhotoImage(file=book[3])  # Путь к изображению обложки
        button = tk.Button(window, image=cover, command=lambda id=book[0]: show_details(id))
        button.image = cover  # Сохраняем ссылку на изображение
        button.pack(side=tk.LEFT)
    
    window.mainloop()

create_main_window()

def insert_book(title, author, cover_image, description, content):
    connection = sqlite3.connect('books_catalog.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, cover_image, description, content) VALUES (?, ?, ?, ?, ?)",
                   (title, author, cover_image, description, content))
    connection.commit()
    connection.close()

# Пример добавления книги
insert_book("Программирование на Python", "Автор 1", "cover1.jpg", "Описание книги 1", "Содержимое книги 1")
insert_book("Изучаем алгоритмы", "Автор 2", "cover2.png", "Описание книги 2", "Содержимое книги 2")

