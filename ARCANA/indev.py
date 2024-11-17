# Библиотеки: tkinter, sqlite3, Pillow.
import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
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

# Скролл
def bind_scroll_events():
    window.bind("<MouseWheel>", lambda event: catalog_canvas.yview_scroll(-1 if event.delta > 0 else 1, "units"))  # Windows
    window.bind("<Button-4>", lambda event: catalog_canvas.yview_scroll(-1, "units"))  # Прокрутка вверх (Linux)
    window.bind("<Button-5>", lambda event: catalog_canvas.yview_scroll(1, "units"))   # Прокрутка вниз (Linux)

    # Обработка прокрутки для фрейма
    catalog_frame.bind("<MouseWheel>", lambda event: catalog_canvas.yview_scroll(-1 if event.delta > 0 else 1, "units"))

# Сочетания клавиш

search_text = ""

def handle_key_press(event, search_entry):
    if event.keysym == 'Escape': 
        search_entry.delete(0, tk.END)  
        search_text = ""  # Сброс текста поиска

        # Обработка сочетания Ctrl+A
    elif event.state & 0x0004 and (event.keycode == 65):  # 0x0004 - состояние Ctrl
        search_entry.select_range(0, tk.END)  # Выделение всего текста в поле поиска

    # Обработка сочетания Ctrl+V
    elif event.state & 0x0004 and (event.keysym == 86 or event.keysym == 109):  # 0x0004 - состояние Ctrl
        try:
            clipboard_content = window.clipboard_get()  # Получение содержимого из буфера обмена
            search_entry.insert(tk.END, clipboard_content)  # Вставка содержимого в поле поиска
        except tk.TclError:
            pass  # Игнорируем ошибку, если буфер обмена пуст
    else:
        search_text = search_entry.get()

# Вызов функции настройки сочетаний клавиш в функции создания главного окна
def create_main_window():
    global window, catalog_frame
    window = tk.Tk()
    window.title("Каталог специальной литературы")
    window.geometry("980x680")
    
    # Настройка весов
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Текстбокс поиска
    search_label = tk.Label(window, text="Поиск: ", font=("Arial", 14))
    search_label.grid(row=0, column=0, padx=41, pady=10, sticky='nw')

    search_entry = tk.Entry(window, font=("Arial", 12))
    search_entry.grid(row=0, column=0, padx=110, pady=10, sticky='nw')
    search_entry.bind("<KeyRelease>", lambda event: update_catalog(search_entry.get()))

    # Создание фрейма для прокрутки
    scrollbar = tk.Scrollbar(window, orient="vertical")
    scrollbar.grid(row=1, column=1, sticky='ns')

    global catalog_canvas
    catalog_canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
    catalog_canvas.grid(row=1, column=0, sticky='nsew')
    scrollbar.config(command=catalog_canvas.yview)

    catalog_frame = tk.Frame(catalog_canvas)
    catalog_canvas.create_window((0, 0), window=catalog_frame, anchor='nw')

    catalog_frame.bind("<Configure>", update_scroll_region)

    bind_scroll_events()

    # Загрузка книг
    load_books()

    # Обновление области прокрутки
    window.update_idletasks()  # Обновляем все задачи интерфейса

# Обновление размеров canvas
def update_scroll_region(event):
    catalog_canvas.configure(scrollregion=catalog_canvas.bbox("all"))

def load_books():
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
        button.grid(row=row, column=column, padx=10, pady=50)  # Интервал обложек в меню
        
        # Размещение названия книги
        label = tk.Label(catalog_frame, text=book[1], font=("Arial", 12))
        label.grid(row=row + 1, column=column, padx=10, pady=10, sticky='n')

    update_catalog("")
    window.mainloop()
    window.update_idletasks()

# Функция для обновления каталога на основе введенного текста
def update_catalog(search_text):
    for widget in catalog_frame.winfo_children():
        widget.destroy()  # Удаляем старые элементы
        
    loading_label = tk.Label(catalog_frame, text="Загрузка...", font=("Arial", 14))
    loading_label.grid(row=0, column=0, padx=10, pady=10)

    window.update()

    books = fetch_books()
    filtered_books = [book for book in books if search_text.lower() in book[1].lower() or 
                      search_text.lower() in book[2].lower() or 
                      search_text.lower() in book[4].lower()]

    # Проверка на существование метки перед её скрытием
    if loading_label.winfo_exists():
        loading_label.grid_forget()  # Скрываем метку "Загрузка..."

    if not filtered_books:
        no_match_label = tk.Label(catalog_frame, text="Совпадения не найдены.", font=("Arial", 14))
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
current_details_frame = None  # Глобальная переменная для хранения текущего окна деталей

def show_details(book_id):
    global current_details_frame  # Объявляем, что будем использовать глобальную переменную
    if current_details_frame:  # Если текущее окно существует, скрываем его
        current_details_frame.grid_forget()
    
    # Получаем данные о книге
    connection = sqlite3.connect(first_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    
    if book:
        # Новый фрейм для подробностей книги
        current_details_frame = tk.Frame(window)  # Обновляем глобальную переменную
        current_details_frame.grid(row=0, column=0, sticky='nsew')

        # Отображение обложки книги в фрейме
        try:
            image = Image.open(book[3])
            image = image.resize((200, 300), Image.LANCZOS)
            cover = ImageTk.PhotoImage(image)
            cover_label = tk.Label(current_details_frame, image=cover)  # Используем current_details_frame
            cover_label.image = cover
            cover_label.grid(row=0, column=1, sticky='nw', padx=20, pady=0)
        except FileNotFoundError:
            print(f"Файл обложки {book[3]} не найден.")
            return

        # Отображаем информацию о книге
        details = f"Автор:           {book[2]}\nНазвание:    {book[1]}\nОписание:    {book[4]}"
        details_label = tk.Label(current_details_frame, text=details, font=("Arial", 14), justify='left')
        details_label.grid(row=0, column=2, sticky='nw', padx=20, pady=0)

        # Кнопка "Назад"
        back_button = tk.Button(current_details_frame, text="Назад", command=lambda: back_to_catalog(), font=("Arial", 14))
        back_button.grid(row=0, column=0, sticky='nw', padx=0, pady=0)

def back_to_catalog():
    global current_details_frame
    if current_details_frame:
        current_details_frame.grid_forget()  # Скрываем текущее окно деталей
        current_details_frame = None  # Обнуляем ссылку на текущее окно

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
        print(f"Книга '{author} - {title}' уже существует в базе данных '{first_db}' (пропуск).")
    
    connection.close()

# Создание новых строк БД прямо из кода, (пропускается, если уже есть)
insert_book("Программирование на PHP", "Автор 3", "covers/cover1.png", "Описание книги 1", "Содержимое книги 1")
