# Библиотеки: tkinter, sqlite3, Pillow.
import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import os
from PIL import Image, ImageTk

# Рабочая папка (относительно самой программы)
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
first_db = 'books_catalog.db'

# Инициализация базы данных
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

# Загрузка данных из БД
def fetch_books():
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

# Окно
def create_main_window():
    global window, catalog_frame, canvas, scrollbar
    window = tk.Tk()
    window.title("Каталог специальной литературы")
    window.geometry("980x680")

    # Создание Canvas и Scrollbar
    canvas = tk.Canvas(window)
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    catalog_frame = tk.Frame(canvas)

    catalog_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=catalog_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Настройка grid для правильного распределения пространства
    window.grid_rowconfigure(1, weight=1)  # Позволяет строке 1 занимать доступное пространство
    window.grid_columnconfigure(0, weight=1)  # Позволяет колонне 0 занимать доступное пространство

    # Размещение Canvas и Scrollbar
    canvas.grid(row=1, column=0, sticky='nsew')
    scrollbar.grid(row=1, column=1, sticky='ns')

    # Загрузка книг
    books = fetch_books()
    
    for index, book in enumerate(books):
        try:
            image = Image.open(book[3])
            image = image.resize((153, 237), Image.LANCZOS)
            cover = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            continue  # Пропустить книгу, если обложка не найдена

        # grid для обложек в меню (4 на 4)
        row = index // 4 
        column = index % 4
        
        button = tk.Button(catalog_frame, image=cover, command=lambda id=book[0]: show_details(id))
        button.image = cover
        button.grid(row=row, column=column, padx=10) # Интервал обложек в меню
        
        # Размещение названия книги
        label = tk.Label(catalog_frame, text=book[1], font=("Arial", 12))
        label.grid(row=row + 1, column=column, padx=10, sticky='n')

    update_catalog("")
    window.mainloop()

# Функция для обновления каталога на основе введенного текста
def update_catalog(search_text):
    for widget in catalog_frame.winfo_children():
        widget.destroy()  # Удаляем старые элементы

    books = fetch_books()
    filtered_books = [book for book in books if search_text.lower() in book[1].lower() or 
                      search_text.lower() in book[2].lower() or 
                      search_text.lower() in book[4].lower()]

    if not filtered_books:
        no_match_label = tk.Label(catalog_frame, text="Совпадения не найдены.", font=("Arial", 12))
        no_match_label.grid(row=0, column=0, padx=10, pady=10)
    else:
        for index, book in enumerate(filtered_books):
            try:
                image = Image.open(book[3])
                image = image.resize((153, 237), Image.LANCZOS)
                cover = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                continue

            row = index // 4
            column = index % 4
            
            button = tk.Button(catalog_frame, image=cover, command=lambda id=book[0]: show_details(id))
            button.image = cover
            button.grid(row=row, column=column, padx=10, pady=(50, 0))
            
            label = tk.Label(catalog_frame, text=book[1], font=("Arial", 12))
            label.grid(row=row + 1, column=column, padx=10, pady=(0, 10), sticky='n')

# Окно подробностей книги
def show_details(book_id):
    # Скрываем каталог
    catalog_frame.grid_forget()
    
    # Получаем данные о книге
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    
    if book:
        # Новый фрейм для подробностей книги
        details_frame = tk.Frame(window)
        details_frame.grid(row=0, column=0, padx=20, pady=20)

        # Отображение обложки книги в фрейме
        try:
            image = Image.open(book[3])
            image = image.resize((200, 300), Image.LANCZOS)
            cover = ImageTk.PhotoImage(image)
            cover_label = tk.Label(details_frame, image=cover)
            cover_label.image = cover
            cover_label.grid(row=0, column=1, sticky='nw' ,padx=20, pady=0)  # Размещаем обложку в верхнем левом углу
        except FileNotFoundError:
            print(f"Файл обложки {book[3]} не найден.")
            return

        # Отображаем информацию о книге
        details = f"Автор:           {book[2]}\nНазвание:    {book[1]}\nОписание:    {book[4]}"
        details_label = tk.Label(details_frame, text=details, font=("Arial", 14), justify='left')
        details_label.grid(row=0, column=2, sticky='nw', padx=20, pady=0)  # Размещаем детали справа от обложки

        # Кнопка "Назад"
        back_button = tk.Button(details_frame, text="Назад", command=lambda: back_to_catalog(details_frame), font=("Arial", 14))
        back_button.grid(row=0, column=0, sticky='nw', padx=0, pady=0)  # Размещаем кнопку "Назад" вверху слева

# Возвращение в каталог
def back_to_catalog(details_frame):
    details_frame.grid_forget() 
    catalog_frame.grid(row=1, column=0)

create_main_window()

# Условия пополнения БД из кода
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

# Создание новых строк БД прямо из кода
insert_book("Мастер и Маргарита (не фейк)", "Автор 3", "covers/cover1.png", "Описание книги 1", "Содержимое книги 1")
insert_book("ШИФР", "Автор 5", "covers/cover2.png", "Описание книги 2", "Содержимое книги 2") 