from tkinter import *
from task_killer.functions.main_form_functions import *
from task_killer.functions.general_functions import add_server
from task_killer.parser import open_server_file
from task_killer.constants import PATH_TO_SRV_FILE
from task_killer.forms import *


def run_main_form():
    # root this is our field
    servers_form = Tk()

    # set parameters for root
    servers_form['bg'] = '#fafafa'  # background color
    servers_form.title('ATK')  # title
    servers_form.geometry('+800+300')
    servers_form.resizable(width=False, height=False)

    # icon = PhotoImage(file=PATH_TO_IMAGE)
    # servers_form.iconphoto(False, icon)

    canvas = Canvas(servers_form, height=440, width=246)
    canvas.pack()

    main_menu = Menu()

    options_menu = Menu(tearoff=0)
    options_menu.add_command(label="Power",
                             command=lambda: open_power_form(server_listbox))
    options_menu.add_command(label="Memory",
                             command=lambda: open_memory_form(server_listbox))
    options_menu.add_separator()
    options_menu.add_command(label="Exit")

    main_menu.add_cascade(label="Options", menu=options_menu)
    servers_form.config(menu=main_menu)

    # top panel (add server)
    frame_top = Frame(servers_form, bg="#202020")
    frame_top.place(relwidth=1, height=75)

    title_add_server = Label(frame_top, text='Add server:',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=10, y=10)

    server_entry = Entry(frame_top, bg='#202020', width=30,
                         foreground='#C0C0C0', font=35)
    server_entry.place(x=10, y=35, height=25, width=190)

    add_server_button = Button(frame_top,
                               command=lambda: add_server(server_entry, server_listbox),
                               text='Add',
                               bg='#202020',
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

    del_server_button = Button(frame_bottom,
                               text='Delete',
                               bg='#202020',
                               fg='#C0C0C0',
                               command=lambda: del_server(server_listbox))
    del_server_button.place(x=10, y=10, height=26, width=60)

    open_button = Button(frame_bottom,
                         text='Open tasks',
                         bg='#202020',
                         fg='#C0C0C0',
                         command=lambda: open_form(server_listbox, open_tasks_form))
    open_button.place(x=160, y=10, height=26, width=80)

    open_button = Button(frame_bottom,
                         text='Clear cache',
                         bg='#202020',
                         fg='#C0C0C0',
                         command=lambda: open_form(server_listbox, open_cache_form))
    open_button.place(x=160, y=46, height=26, width=80)

    servers_form.mainloop()
