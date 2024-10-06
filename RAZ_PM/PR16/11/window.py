import tkinter as tk
from tkinter import font

def DecodeText(input_text, K):
    lc_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uc_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    decrypted_text = ''
    
    for char in input_text:
        if char in lc_alphabet:
            original_index = lc_alphabet.index(char)
            new_index = (original_index - K) % len(lc_alphabet)
            decrypted_text += lc_alphabet[new_index]
        elif char in uc_alphabet:
            original_index = uc_alphabet.index(char)
            new_index = (original_index - K) % len(uc_alphabet)
            decrypted_text += uc_alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text

def on_decrypt():
    input_text = e1.get()
    result = DecodeText(input_text, 3)
    output_label.config(text=f"Послание: {result}")

root = tk.Tk()
root.title("Расшифратор 1.6")
root.geometry("600x100")

label1 = tk.Label(root, text="Ввод шифра: ")
label1.grid(row=0, column=0)

semibold = font.Font(family="Arial", size=11, weight="bold")
e1 = tk.Entry(root, font=semibold)
e1.grid(row=0, column=1)

calc_button = tk.Button(root, text="Декрипт", command=on_decrypt)
calc_button.grid(row=1, column=1)

output_label = tk.Label(root, text="")
output_label.grid(row=2, column=1)

root.mainloop()
