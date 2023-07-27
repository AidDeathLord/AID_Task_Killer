from tkinter import *
from tkinter import ttk
from task_killer.parser import get_tasks, get_users
import subprocess


def open_users(server):
    users_info = get_users(server)
    return list(users_info.keys())


def open_form(server):
    def open_tasks():
        selection = users_listbox.curselection()
        # remember the content of the element
        selected_user = users_listbox.get(selection[0])

        users_dict = get_users(server)
        user_id = users_dict.get(selected_user)

        tasks = get_tasks(server, user_id)
        for elem in tasks:
            table.insert('', END, values=elem)

    def close_task():
        selected_item = table.selection()[0]
        task = table.item(selected_item, option="values")

        command = f'''powershell.exe $process = Get-Process -ID {task[1]} -ComputerName {server}\n
                      Stop-Process -InputObject $process'''
        subprocess.call(command)
        table.delete(selected_item)

    def kick_user():
        selection = users_listbox.curselection()
        selected_user = users_listbox.get(selection[0])
        users_dict = get_users(server)
        user_id = users_dict.get(selected_user)

        command = f'logoff {user_id} /server:{server}'
        subprocess.call(command)
        users_listbox.delete(selection)

    # tasks form
    task_form = Toplevel()
    task_form.title(f"{server}")

    task_form['bg'] = '#fafafa'  # background color
    task_form.geometry('+600+300')
    task_form.resizable(width=False, height=False)

    icon = PhotoImage(file='image/logo.png')
    task_form.iconphoto(False, icon)

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

    open_tasks_button = Button(frame_bottom, text='Open', bg='#202020',
                               fg='#C0C0C0', command=open_tasks)
    open_tasks_button.place(x=10, y=10, height=26, width=60)

    kick_user_button = Button(frame_bottom, text='Kick', bg='#202020',
                              fg='#C0C0C0', command=kick_user)
    kick_user_button.place(x=180, y=10, height=26, width=60)

    close_tasks_button = Button(frame_bottom, text='Close', bg='#202020',
                                fg='#C0C0C0', command=close_task)
    close_tasks_button.place(x=430, y=10, height=26, width=60)

    task_form.mainloop()
