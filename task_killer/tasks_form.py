from tkinter import *
from tkinter import ttk


def open_tasks(server):
    task_form = Toplevel()
    task_form.title(f"{server}")

    task_form['bg'] = '#fafafa'  # background color
    task_form.geometry('+800+300')
    task_form.resizable(width=False, height=False)

    icon = PhotoImage(file='image/logo.png')
    task_form.iconphoto(False, icon)

    canvas = Canvas(task_form, height=500, width=500)
    canvas.pack()

    frame = Frame(task_form, bg="#202020")
    frame.place(relwidth=1, relheight=1)

    # add table
    columns = ('Program', 'PID', 'State', 'Session', 'UserName', 'Memory')
    table = ttk.Treeview(frame, columns=columns, show='headings')
    table.place(x=10, y=10)

    table.heading('Program', text='Program')
    table.heading('PID', text='PID')
    table.heading('State', text='State')
    table.heading('Session', text='Session')
    table.heading('UserName', text='UserName')
    table.heading('Memory', text='Memory')

    tasks = [('qwe', 11, 'ewq'), (11, 22, 33, 44, 55, 66), (111, 222, 333, 444, 555, 666)]

    for i in tasks:
        table.insert('', END, values=tasks)

    task_form.mainloop()
