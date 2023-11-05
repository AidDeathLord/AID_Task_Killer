from tkinter import *
from tkinter import ttk
from task_killer.functions.tasks_form_functions import *
from task_killer.functions.general_functions import open_users


def open_tasks_form(server):
    # tasks form
    task_form = Toplevel()
    task_form.title(f"{server}")

    task_form['bg'] = '#fafafa'  # background color
    task_form.geometry('+600+300')
    task_form.resizable(width=False, height=False)

    # icon = PhotoImage(file='image/logo.png')
    # task_form.iconphoto(False, icon)

    canvas = Canvas(task_form, height=430, width=600)
    canvas.pack()

    # top panel #
    frame_top = Frame(task_form, bg="#202020")
    frame_top.place(relwidth=1, height=40)

    # Label Users
    title_add_server = Label(frame_top, text='Users',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=120, y=8)

    # Label Tasks
    title_add_server = Label(frame_top, text='Tasks',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=430, y=8)

    # center panel #
    frame_center = Frame(task_form, bg="#606060")
    frame_center.place(relwidth=1, height=350, y=40)

    users = Variable(value=open_users(server))
    users_listbox = Listbox(frame_center, listvariable=users, bg="#202020",
                            bd=0, highlightbackground='#202020', fg='#C0C0C0',
                            font=30, selectbackground='#48BA6B')
    users_listbox.place(height=330, width=280, x=10, y=10)

    # add table
    columns = ('Program', 'PID')
    table = ttk.Treeview(frame_center, columns=columns, show='headings')
    table.place(height=330, x=300, y=10)

    # table style
    style = ttk.Style(task_form)
    style.theme_use('clam')
    style.configure('Treeview', background='#202020', bordercolor='#202020',
                    fieldbackground='#202020', foreground='#C0C0C0', font=30)
    style.configure('Treeview.Heading', background='#202020', foreground='#C0C0C0', borderwidth=0)
    style.map('Treeview', background=[('selected', '#48BA6B')])

    table.heading('Program', text='Program')
    table.column('Program', anchor=W, width=200)
    table.heading('PID', text='PID')
    table.column('PID', anchor=CENTER, width=90)

    # bottom panel
    frame_bottom = Frame(task_form, bg="#202020")
    frame_bottom.place(relwidth=1, height=50, y=390)

    open_tasks_button = Button(frame_bottom,
                               text='Open',
                               bg='#202020',
                               fg='#C0C0C0',
                               command=lambda: open_tasks(users_listbox, table, server))
    open_tasks_button.place(x=10, y=10, height=26, width=60)

    kick_user_button = Button(frame_bottom,
                              text='Kick',
                              bg='#202020',
                              fg='#C0C0C0',
                              command=lambda: kick_user(users_listbox, server))
    kick_user_button.place(x=180, y=10, height=26, width=60)

    close_tasks_button = Button(frame_bottom,
                                text='Close',
                                bg='#202020',
                                fg='#C0C0C0',
                                command=lambda: close_task(table, server))
    close_tasks_button.place(x=430, y=10, height=26, width=60)

    task_form.mainloop()
