from tkinter import *
from tkinter import font


class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.font_obj = font.Font(size=20)
        self.check_num = '0'
        self.answers = 0
        self.do = ''

        self.title('Калькулятор')
        self.geometry('300x500')

        self.MainUi = Frame()
        self.buttons = Frame(pady=5)

        self.out = Label(self.MainUi, text='', foreground='#A99797')
        self.inp = Label(self.MainUi, text='0', font=self.font_obj)

        self.out.pack(anchor='w')
        self.inp.pack(anchor='w')

        self.b1 = Button(self.buttons, text='1', font=self.font_obj, command=lambda: self.input_text('1'))
        self.b2 = Button(self.buttons, text='2', font=self.font_obj, command=lambda: self.input_text('2'))
        self.b3 = Button(self.buttons, text='3', font=self.font_obj, command=lambda: self.input_text('3'))
        self.b4 = Button(self.buttons, text='4', font=self.font_obj, command=lambda: self.input_text('4'))
        self.b5 = Button(self.buttons, text='5', font=self.font_obj, command=lambda: self.input_text('5'))
        self.b6 = Button(self.buttons, text='6', font=self.font_obj, command=lambda: self.input_text('6'))
        self.b7 = Button(self.buttons, text='7', font=self.font_obj, command=lambda: self.input_text('7'))
        self.b8 = Button(self.buttons, text='8', font=self.font_obj, command=lambda: self.input_text('8'))
        self.b9 = Button(self.buttons, text='9', font=self.font_obj, command=lambda: self.input_text('9'))
        self.b0 = Button(self.buttons, text='0', font=self.font_obj, command=lambda: self.input_text('0'))

        self.b1.grid(row=0, column=0, padx=1, pady=1, ipadx=3, ipady=3)
        self.b2.grid(row=0, column=1, padx=1, pady=1, ipadx=3, ipady=3)
        self.b3.grid(row=0, column=2, padx=1, pady=1, ipadx=3, ipady=3)
        self.b4.grid(row=1, column=0, padx=1, pady=1, ipadx=3, ipady=3)
        self.b5.grid(row=1, column=1, padx=1, pady=1, ipadx=3, ipady=3)
        self.b6.grid(row=1, column=2, padx=1, pady=1, ipadx=3, ipady=3)
        self.b7.grid(row=2, column=0, padx=1, pady=1, ipadx=3, ipady=3)
        self.b8.grid(row=2, column=1, padx=1, pady=1, ipadx=3, ipady=3)
        self.b9.grid(row=2, column=2, padx=1, pady=1, ipadx=3, ipady=3)
        self.b0.grid(row=3, column=1, padx=1, pady=1, ipadx=3, ipady=3)

        self.plus = Button(self.buttons, text='+', font=self.font_obj, command=lambda: self.moves('+'))
        self.minus = Button(self.buttons, text='-', font=self.font_obj, command=lambda: self.moves('-'))
        self.multiplication = Button(self.buttons, text='x', font=self.font_obj, command=lambda: self.moves('*'))
        self.division = Button(self.buttons, text='/', font=self.font_obj, command=lambda: self.moves('/'))

        self.comma = Button(self.buttons, text='.', font=self.font_obj, command=lambda: self.input_text('.'))
        self.smooth = Button(self.buttons, text='=', font=self.font_obj, command=self.outputs)

        self.plus.grid(row=0, column=3, padx=1, pady=1, ipadx=1, ipady=3)
        self.minus.grid(row=1, column=3, padx=1, pady=1, ipadx=5, ipady=3)
        self.multiplication.grid(row=2, column=3, padx=1, pady=1, ipadx=3, ipady=3)
        self.division.grid(row=3, column=3, padx=1, pady=1, ipadx=5, ipady=3)

        self.smooth.grid(row=3, column=0, padx=1, pady=1, ipadx=3, ipady=3)
        self.comma.grid(row=3, column=2, padx=1, pady=1, ipadx=5, ipady=3)

        self.back = Button(self.buttons, text='<=', font=self.font_obj, command=self.back_text)
        self.del_text = Button(self.buttons, text='C', font=self.font_obj, command=self.minus_text)

        self.back.grid(row=0, column=4, padx=1, pady=1, ipadx=1, ipady=3)
        self.del_text.grid(row=1, column=4, padx=1, pady=1, ipadx=5, ipady=3)

        self.MainUi.pack(anchor='w')
        self.buttons.pack(anchor='w')

    def moves(self, move):
        self.do = move
        match self.do:
            case '+':
                self.out['text'] = f'{self.inp['text']} +'
            case '-':
                self.out['text'] = f'{self.inp['text']} -'
            case '*':
                self.out['text'] = f'{self.inp['text']} *'
            case '/':
                self.out['text'] = f'{self.inp['text']} /'
        self.num = float(self.inp['text'])
        self.check_num = self.inp['text']

    def outputs(self):
        self.out['text'] += f" {self.inp['text']} ="
        match self.do:
            case '+':
                self.inp['text'] = self.num + float(self.inp['text'])
            case '-':
                self.inp['text'] = self.num - float(self.inp['text'])
            case '*':
                self.inp['text'] = self.num * float(self.inp['text'])
            case '/':
                self.inp['text'] = self.num / float(self.inp['text'])

        self.check_num = self.inp['text']

    def input_text(self, text):
        if self.inp['text'] == self.check_num:
            self.inp['text'] = text
            self.check_num = '0'
        else:
            self.inp['text'] += text

    def minus_text(self):
        self.inp['text'] = '0'
        self.out['text'] = ''
        self.check_num = '0'
        self.answers = 0

    def back_text(self):
        self.inp['text'] = self.inp['text'][:len(self.inp['text'])-1]

        if len(self.inp['text']) == 0:
            self.inp['text'] = '0'
            self.check_num = '0'
            self.answers = 0


main = Calculator()
main.mainloop()
