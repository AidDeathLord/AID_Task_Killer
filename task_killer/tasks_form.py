from tkinter import *
from tkinter import ttk
from task_killer.parser import get_tasks, get_users


def open_users():
    users_info = get_users()
    result = []
    for elem in users_info:
        result.append(elem.get('User'))
    return result

def open_tasks(server):
    task_form = Toplevel()
    task_form.title(f"{server}")

    task_form['bg'] = '#fafafa'  # background color
    task_form.geometry('+500+200')
    task_form.resizable(width=False, height=False)

    icon = PhotoImage(file='image/logo.png')
    task_form.iconphoto(False, icon)

    canvas = Canvas(task_form, height=500, width=800)
    canvas.pack()

    # top panel
    frame_top = Frame(task_form, bg="#202020")
    frame_top.place(relwidth=1, height=40)

    title_add_server = Label(frame_top, text='Users',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=120, y=8)

    frame_center = Frame(task_form, bg="#606060")
    frame_center.place(relwidth=1, height=300, y=40)

    title_add_server = Label(frame_top, text='Tasks',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=260, y=8)

    # center panel
    servers = Variable(value=open_users())
    server_listbox = Listbox(frame_center, listvariable=servers, bg="#202020",
                             bd=0, highlightbackground='#202020', fg='#C0C0C0',
                             font=30, selectbackground='#48BA6B')
    server_listbox.place(height=230, width=280, x=10, y=10)

    # add table
    columns = ('Program', 'PID', 'State', 'Session', 'UserName', 'Memory')
    table = ttk.Treeview(frame_center, columns=columns, show='headings')
    table.place(x=290, y=10)

    table.heading('Program', text='Program')
    table.column('Program', anchor=W, width=200)
    table.heading('PID', text='PID')
    table.column('PID', anchor=CENTER, width=50)
    table.heading('State', text='State')
    table.column('State', anchor=W, width=100)
    table.heading('Session', text='Session')
    table.column('Session', anchor=W, width=50)
    table.heading('UserName', text='UserName')
    table.column('UserName', anchor=W, width=100)
    table.heading('Memory', text='Memory')
    table.column('Memory', anchor=W, width=100)

    tasks = get_tasks()
    for i in tasks:
        info = (i.get('User'), i.get('PID'), i.get('Program'))
        table.insert('', END, values=info)

    task_form.mainloop()
