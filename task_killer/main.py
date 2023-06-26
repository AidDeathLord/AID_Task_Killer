import re
import subprocess
from tkinter import *
from tkinter import messagebox
from task_killer.parser import open_file


def add_server():
    new_server = server_entry.get()
    server_list = open_file()
    if new_server in server_list:
        open_server()
    else:
        if add_srv_in_txt(new_server):
            server_listbox.insert(0, new_server)
            open_server()
        else:
            error_add_server()


def add_srv_in_txt(new_server):
    if subprocess.check_output(f"powershell.exe tnc {new_server} -I Quiet",
                               universal_newlines=True) == 'True\n':
        server_file = open('server_list/servers.txt', 'a')
        server_file.writelines(f'{new_server}\n')
        return True
    return False


def error_add_server():
    messagebox.showerror(title="Error", message="Server is not available")


def open_server():
    messagebox.showerror(title="Error", message="open")

# root this is our field
root = Tk()

# set parameters for root
root['bg'] = '#fafafa'  # background color
root.title('ATK')  # title
root.resizable(width=False, height=False)

icon = PhotoImage(file='image/logo.png')
root.iconphoto(False, icon)

canvas = Canvas(root, height=370, width=250)
canvas.pack()


# top panel (add server)
frame_top = Frame(root, bg="#202020")
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
frame_center = Frame(root, bg="#606060")
frame_center.place(relwidth=1, height=250, y=75)


servers = Variable(value=open_file())
server_listbox = Listbox(frame_center, listvariable=servers, bg="#202020",
                         bd=0, highlightbackground='#202020', fg='#C0C0C0',
                         font=30, selectbackground='#48BA6B')
server_listbox.place(height=230, width=230, x=10, y=10)


# bottom panel
frame_bottom = Frame(root, bg="#202020")
frame_bottom.place(relwidth=1, height=80, y=325)

del_server_button = Button(frame_bottom, text='Delete', bg='#202020',
                           fg='#C0C0C0')
del_server_button.place(x=10, y=10, height=26, width=60)

open_button = Button(frame_bottom, text='Open', bg='#202020',
                     fg='#C0C0C0')
open_button.place(x=180, y=10, height=26, width=60)

root.mainloop()
