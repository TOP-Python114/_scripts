"""Компонент Представление (MVC) — графический интерфейс пользователя."""
from typing import Collection

from tkinter import Tk, ttk, Text, Button, StringVar
from tkinter.constants import GROOVE, DISABLED

import controller


def start_view() -> None:
    top_label['text'] = 'Приветствую в Демонстраторе MVC!'
    root.after(2000, ask_if_show_all)
    root.mainloop()


def ask_if_show_all() -> None:
    top_label['text'] = 'Хотите вывести всю информацию из БД [д/н]?'
    root.after(5000, controller.answer_check, answer.get())


def show_all_view(data: Collection) -> None:
    top_label['text'] = f'В БД всего {len(data)} элементов'
    text = '\n'.join(str(elem) for elem in data)
    data_field.insert('1.0', text)
    root.after(10000, controller.end)


def end_view() -> None:
    top_label['text'] = 'Пока!'
    root.after(2000, exit)


root = Tk()
root.title('Демонстратор MVC')
root.geometry('500x1050-50+50')

mainframe = ttk.Frame(root, padding=10)
mainframe.grid(row=0, column=0, sticky='nsew')

top_label = ttk.Label(mainframe, text='', font=24)
top_label.grid(row=0, column=0, columnspan=2, sticky='nwe')

answer = StringVar()

answer_field = ttk.Entry(mainframe, textvariable=answer)
answer_field.grid(row=1, column=0, sticky='nwe')

answer_button = Button(
    mainframe,
    text='Ответить',
    font=20,
    command=lambda: controller.answer_check(answer.get())
)
answer_button.grid(row=1, column=1, sticky='ne', padx=(10, 0))

data_field = Text(
    mainframe,
    relief=GROOVE,
    borderwidth=6,
    font=20,
    # state=DISABLED
)
data_field.grid(row=2, column=0, columnspan=2, sticky='nsew', pady=10)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(0, weight=1)


if __name__ == '__main__':
    root.mainloop()
