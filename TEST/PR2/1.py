import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    clear_plot()

    try:
        x_values = np.linspace(float(x_min_entry.get()), float(x_max_entry.get()), 1000)

        function_type = function_var.get()

        if function_type == "Линейная":
            y_values = float(a_entry.get()) * x_values + float(b_entry.get())
        elif function_type == "Квадратная":
            y_values = float(a_entry.get()) * x_values ** 2 + float(b_entry.get())
        elif function_type == "Кубическая":
            y_values = float(a_entry.get()) * x_values ** 3 + float(b_entry.get())
        elif function_type == "Степенная":
            y_values = float(a_entry.get()) * x_values ** float(power_entry.get()) + float(b_entry.get())
        elif function_type == "Логарифмическая":
            y_values = np.log(x_values)
        elif function_type == "Показательная":
            y_values = np.exp(x_values)
        elif function_type == "Тригонометрическая функция(sin)":
            y_values = np.sin(x_values)
        elif function_type == "Тригонометрическая функция(cos)":
            y_values = np.cos(x_values)

        fig = plt.figure()
        plt.plot(x_values, y_values)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError as e:
        error_label.config(text=str(e))


def clear_plot():
    for widget in root.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()


root = tk.Tk()
root.title("Калькулятор")

function_var = tk.StringVar()
function_var.set("Линейная")

label_function = tk.Label(root, text="Выберите функцию:")
label_function.pack()

function_options = ["Линейная", "Квадратная", "Кубическая", "Степенная", "Логарифмическая", "Показательная", "Тригонометрическая функция(sin)", "Тригонометрическая функция(cos)"]
function_menu = tk.OptionMenu(root, function_var, *function_options)
function_menu.pack()

label_a = tk.Label(root, text="Введите значение 'a':")
label_a.pack()

a_entry = tk.Entry(root)
a_entry.pack()

label_b = tk.Label(root, text="Введите значение 'b':")
label_b.pack()

b_entry = tk.Entry(root)
b_entry.pack()

label_power = tk.Label(root, text="Введите степень(только для степенной функции):")
label_power.pack()

power_entry = tk.Entry(root)
power_entry.pack()

label_x_range = tk.Label(root, text="Введите гранницы значения Х(min, max):")
label_x_range.pack()

x_min_entry = tk.Entry(root)
x_min_entry.pack()

x_max_entry = tk.Entry(root)
x_max_entry.pack()

plot_button = tk.Button(root, text="Сооставить график", command=plot_graph)
plot_button.pack()

clear_button = tk.Button(root, text="Очистить график", command=clear_plot)
clear_button.pack()

error_label = tk.Label(root, fg="red")
error_label.pack()

root.mainloop()