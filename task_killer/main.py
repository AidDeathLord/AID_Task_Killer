import subprocess
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from task_killer.parser import open_server_file
from task_killer.tasks_form import open_tasks_form
from task_killer.cache_form import open_cache_form


PATH_TO_SRV_FILE = Path('server_list', 'servers.txt')
PATH_TO_IMAGE = Path('image', 'logo.png')


def add_server():
    new_server = server_entry.get()
    server_list = open_server_file(PATH_TO_SRV_FILE)
    if new_server in server_list:
        error_add_server()
    else:
        if add_srv_in_txt(new_server):
            server_listbox.insert(0, new_server)
        else:
            error_add_server()


def add_srv_in_txt(new_server: str) -> bool:
    if new_server == '':
        return False
    if subprocess.check_output(f"powershell.exe tnc {new_server} -I Quiet",
                               universal_newlines=True) == 'True\n':
        server_file = open(PATH_TO_SRV_FILE, 'a')
        server_file.writelines(f'{new_server}\n')
        return True
    return False


def error_add_server():
    messagebox.showerror(title="Error", message="Server is not available")


def del_server():
    # remember the index of the selected element
    selection = server_listbox.curselection()
    # remember the content of the element
    selected_server = server_listbox.get(selection[0])

    # remove element from form
    server_listbox.delete(selection[0])

    # remove element from file
    server_list = open_server_file(PATH_TO_SRV_FILE)
    server_list.remove(str(selected_server))
    server_file = open(PATH_TO_SRV_FILE, 'w')
    for server in server_list:
        server_file.writelines(f'{server}\n')


def open_tasks():
    # remember the index of the selected element
    selection = server_listbox.curselection()
    # remember the content of the element
    selected_server = server_listbox.get(selection[0])
    open_tasks_form(selected_server)


def open_cache():
    # remember the index of the selected element
    selection = server_listbox.curselection()
    # remember the content of the element
    selected_server = server_listbox.get(selection[0])
    open_cache_form(selected_server)


# root this is our field
servers_form = Tk()

# set parameters for root
servers_form['bg'] = '#fafafa'  # background color
servers_form.title('ATK')  # title
servers_form.geometry('+800+300')
servers_form.resizable(width=False, height=False)

icon = PhotoImage(file=PATH_TO_IMAGE)
servers_form.iconphoto(False, icon)

canvas = Canvas(servers_form, height=440, width=246)
canvas.pack()


# top panel (add server)
frame_top = Frame(servers_form, bg="#202020")
frame_top.place(relwidth=1, height=75)


title_add_server = Label(frame_top, text='Add server:',
                         bg='#202020', font=40, foreground='#C0C0C0')
title_add_server.place(x=10, y=10)


server_entry = Entry(frame_top, bg='#202020', width=30,
                     foreground='#C0C0C0', font=35)
server_entry.place(x=10, y=35, height=25, width=190)


add_server_button = Button(frame_top, command=add_server, text='Add', bg='#202020',
                           fg='#C0C0C0')
add_server_button.place(x=200, y=35, height=26, width=40)


# center panel (server list)
frame_center = Frame(servers_form, bg="#606060")
frame_center.place(relwidth=1, height=250, y=75)


servers = Variable(value=open_server_file(PATH_TO_SRV_FILE))
server_listbox = Listbox(frame_center, listvariable=servers, bg="#202020",
                         bd=0, highlightbackground='#202020', fg='#C0C0C0',
                         font=30, selectbackground='#48BA6B')
server_listbox.place(height=230, width=230, x=10, y=10)


# bottom panel
frame_bottom = Frame(servers_form, bg="#202020")
frame_bottom.place(relwidth=1, height=140, y=325)

del_server_button = Button(frame_bottom, text='Delete', bg='#202020',
                           fg='#C0C0C0', command=del_server)
del_server_button.place(x=10, y=10, height=26, width=60)

open_button = Button(frame_bottom, text='Open tasks', bg='#202020',
                     fg='#C0C0C0', command=open_tasks)
open_button.place(x=160, y=10, height=26, width=80)

open_button = Button(frame_bottom, text='Clear cache', bg='#202020',
                     fg='#C0C0C0', command=open_cache)
open_button.place(x=160, y=46, height=26, width=80)

open_button = Button(frame_bottom, text='Power', bg='#202020',
                     fg='#C0C0C0', command=open_tasks)
open_button.place(x=160, y=82, height=26, width=80)


def main():
    servers_form.mainloop()


if __name__ == '__main__':
    main()
