from tkinter import ttk
import tkinter as tk


root = tk.Tk()
root.title('Пример реализации оконного графического интерфейса')
root.geometry('900x300+200-50')

mainframe = ttk.Frame(root, padding=10)
mainframe.grid(row=0, column=0, sticky='nsew')

text_toplabel = tk.StringVar()
toplabel = ttk.Label(
    mainframe,
    textvariable=text_toplabel,
    background='light green',
    font=('Comic Sans MS', 24),
    padding=(2, 0, 4, 5)
)
toplabel.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(0, 10))

text_msgentry = tk.StringVar()
msgentry = ttk.Entry(
    mainframe,
    textvariable=text_msgentry,
    font=('Arial', 20)
)
msgentry.grid(row=1, column=0, sticky='nsew')

entrybutton = tk.Button(
    mainframe,
    text='n',
    font=('Digits', 16),
    # command=
)
entrybutton.grid(row=1, column=1, sticky='nse', padx=(10, 0))

botlabel = ttk.Label(
    mainframe,
    textvariable=text_msgentry,
    background='light yellow',
    font=('Arounder', 22),
    justify='center',
    wraplength=880,
    padding=(10, 5)
)
botlabel.grid(row=2, column=0, columnspan=2, sticky='nsew', pady=(10, 0))

text_toplabel.set('Пример надписи')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=0)
mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(0, weight=1)

root.mainloop()
