from tkinter import *


def open_memory_form(main_listbox):

    memory_form = Toplevel()
    memory_form.title(f'Memory')

    memory_form['bg'] = '#fafafa'  # background color
    memory_form.geometry('+600+300')
    memory_form.resizable(width=False, height=False)

    # icon = PhotoImage(file='image/logo.png')
    # task_form.iconphoto(False, icon)

    canvas = Canvas(memory_form, height=415, width=570)
    canvas.pack()
