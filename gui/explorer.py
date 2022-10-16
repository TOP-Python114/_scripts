from pathlib import Path
from sys import path

from tkinter import ttk
import tkinter as tk

SCRIPT_DIR = Path(path[0])

root = tk.Tk()
root.title('Файлы')
root.wm_state('zoomed')

mframe = ttk.Frame(root, padding=7)
mframe.grid(row=0, column=0, sticky='nsew')

lbl1_text = tk.StringVar(value='Введите путь:')
ttk.Label(
    mframe,
    textvariable=lbl1_text,
    font=('Verdana', 16)
).grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(0, 10))

def check_input(variable: tk.StringVar):
    path_string = variable.get()
    return Path(path_string).is_dir()

ent1_text = tk.StringVar(value=str(SCRIPT_DIR))
ttk.Entry(
    mframe,
    textvariable=ent1_text,
    font=('Verdana', 15),
    validate='focusout',
    validatecommand=lambda: check_input(ent1_text),
    invalidcommand=lambda: ent1_text.set('')
).grid(row=1, column=0, sticky='nsew')

def dir_folder(path_to_folder: str):
    if path_to_folder:
        result = ''
        path_to_folder = Path(path_to_folder)
        for item in path_to_folder.iterdir():
            result += f'{item}\n'
        lbl2_text.set(result)

icon_open = tk.PhotoImage(file=SCRIPT_DIR / 'open.png')
ttk.Button(
    mframe,
    image=icon_open,
    command=lambda: dir_folder(ent1_text.get())
).grid(row=1, column=1, sticky='nse', padx=(10, 0))

lbl2_text = tk.StringVar()
ttk.Label(
    mframe,
    textvariable=lbl2_text,
    font=('Nk 57 Sc Rg', 15)
).grid(row=2, column=0, columnspan=2, sticky='nsew', pady=(10, 0))

root.bind('<Return>', lambda event: dir_folder(ent1_text.get()))

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mframe.rowconfigure(1, weight=0)
mframe.columnconfigure(0, weight=1)

root.mainloop()
