from tkinter import *
import subprocess
from task_killer.parser import get_tasks, get_users


def close_task(table, server):
    selected_item = table.selection()[0]
    task = table.item(selected_item, option="values")

    command = f'taskkill /PID {task[1]} /S {server} /F'
    subprocess.call(command)
    table.delete(selected_item)


def kick_user(listbox, server):
    selection = listbox.curselection()
    selected_user = listbox.get(selection[0])
    users_dict = get_users(server)
    user_id = users_dict.get(selected_user)

    command = f'logoff {user_id} /server:{server}'
    subprocess.call(command)
    listbox.delete(selection)


def open_tasks(listbox, table, server):
    selection = listbox.curselection()
    # remember the content of the element
    selected_user = listbox.get(selection[0])

    users_dict = get_users(server)
    user_id = users_dict.get(selected_user)

    tasks = get_tasks(server, user_id)
    for elem in tasks:
        table.insert('', END, values=elem)
