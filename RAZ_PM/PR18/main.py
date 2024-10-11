import tkinter as tk

def animation():
    for shape in shapes:
        canvas.move(shape, 5, 0)
    canvas.after(100, animation)

root = tk.Tk()
root.title("variant11")
root.geometry("1366x768")
canvas = tk.Canvas(root, width=1366, height=768)
canvas.pack()

shapes = []
#(левая, верхняя, правая, нижняя граница)
#Ноги сзади
shapes.append(canvas.create_rectangle(100, 350, 150, 425, fill='gray'))
shapes.append(canvas.create_rectangle(150, 350, 200, 425, fill='gray'))
# Тело
shapes.append(canvas.create_oval(75, 200, 350, 400, fill='gray'))
# Ноги спереди
shapes.append(canvas.create_rectangle(225, 350, 275, 425, fill='gray'))
shapes.append(canvas.create_rectangle(275, 350, 325, 425, fill='gray'))
# Голова
shapes.append(canvas.create_oval(200, 100, 400, 300, fill='gray'))
# Уши
shapes.append(canvas.create_oval(150, 100, 225, 225, fill='lightgray'))
shapes.append(canvas.create_oval(375, 100, 450, 225, fill='lightgray'))
# Глаза
shapes.append(canvas.create_oval(250, 150, 270, 170, fill='white'))
shapes.append(canvas.create_oval(330, 150, 350, 170, fill='white'))
shapes.append(canvas.create_oval(260, 160, 265, 165, fill='black'))
shapes.append(canvas.create_oval(340, 160, 345, 165, fill='black'))
# Хобот
shapes.append(canvas.create_rectangle(300, 225, 500, 205, fill='darkgray'))

animation()
root.mainloop()