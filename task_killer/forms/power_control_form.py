# from tkinter import *
from task_killer.parser import open_server_file
from task_killer.constants import PATH_TO_SRV_FILE
from task_killer.functions.general_functions import add_server
from task_killer.functions.power_control_functions import *


def open_power_form(main_listbox):

    # tasks form
    cache_form = Toplevel()
    cache_form.title(f'Power control')

    cache_form['bg'] = '#fafafa'  # background color
    cache_form.geometry('+600+300')
    cache_form.resizable(width=False, height=False)

    # icon = PhotoImage(file='image/logo.png')
    # task_form.iconphoto(False, icon)

    canvas = Canvas(cache_form, height=415, width=570)
    canvas.pack()

    # top panel #
    frame_top = Frame(cache_form, bg='#202020')
    frame_top.place(relwidth=1, height=70)

    title_add_server = Label(frame_top, text='Add server:',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=10, y=10)

    title_select_server = Label(frame_top, text='Select server',
                                bg='#202020', font=40, foreground='#C0C0C0')
    title_select_server.place(x=200, y=40)

    title_select_server = Label(frame_top, text='Select action',
                                bg='#202020', font=40, foreground='#C0C0C0')
    title_select_server.place(x=360, y=40)

    server_entry = Entry(frame_top, bg='#202020', width=30,
                         foreground='#C0C0C0', font=35)
    server_entry.place(x=10, y=35, height=25, width=80)

    add_server_button = Button(frame_top,
                               command=lambda: add_server(server_entry,
                                                          servers_listbox,
                                                          main_listbox),
                               text='Add',
                               bg='#202020',
                               fg='#C0C0C0')
    add_server_button.place(x=90, y=35, height=25, width=40)

    # center panel
    frame_center = Frame(cache_form, bg='#606060')
    frame_center.place(relwidth=1, height=300, y=70)

    action = StringVar(value='reset')
    action_radiobutton = Radiobutton(frame_center,
                                     bg='#606060',
                                     activebackground='#606060',
                                     font=30,
                                     foreground='#202020',
                                     text='reset',
                                     value='reset',
                                     variable=action)
    action_radiobutton.place(x=360, y=10)

    action_radiobutton2 = Radiobutton(frame_center,
                                      bg='#606060',
                                      activebackground='#606060',
                                      font=30,
                                      foreground='#202020',
                                      text='off',
                                      value='off',
                                      variable=action)
    action_radiobutton2.place(x=440, y=10)

    title_select_server = Label(frame_center, text='Select time',
                                bg='#606060', font=40, foreground='#202020')
    title_select_server.place(x=360, y=40)

    time = StringVar(value='after')
    time_radiobutton = Radiobutton(frame_center,
                                   bg='#606060',
                                   activebackground='#606060',
                                   font=30,
                                   foreground='#202020',
                                   text='after',
                                   value='after',
                                   variable=time,
                                   command=lambda: on_select_after(time_entry))
    time_radiobutton.place(x=360, y=60)

    time_radiobutton2 = Radiobutton(frame_center,
                                    bg='#606060',
                                    activebackground='#606060',
                                    font=30,
                                    foreground='#202020',
                                    text='to',
                                    value='to',
                                    variable=time,
                                    command=lambda: on_select_to(time_entry))
    time_radiobutton2.place(x=440, y=60)

    servers = Variable(value=open_server_file(PATH_TO_SRV_FILE))
    servers_listbox = Listbox(frame_center, listvariable=servers, bg='#202020',
                              bd=0, highlightbackground='#202020', fg='#C0C0C0',
                              font=30, selectbackground='#48BA6B')
    servers_listbox.place(height=280, width=120, x=10, y=10)

    selected_servers = Listbox(frame_center, bg='#202020',
                               bd=0, highlightbackground='#202020', fg='#C0C0C0',
                               font=30, selectbackground='#48BA6B')
    selected_servers.place(height=280, width=120, x=190, y=10)

    select_server_button = Button(frame_center,
                                  command=lambda: add_server_in_select_list(servers_listbox,
                                                                            selected_servers),
                                  text='==|>',
                                  bg='#202020',
                                  fg='#C0C0C0')
    select_server_button.place(x=140, y=80, height=25, width=40)

    select_server_button = Button(frame_center,
                                  command=lambda: remove_from_select_list(servers_listbox,
                                                                          selected_servers),
                                  text='<|==',
                                  bg='#202020',
                                  fg='#C0C0C0')
    select_server_button.place(x=140, y=110, height=25, width=40)

    time_entry = Entry(frame_center,
                       bg='#202020',
                       foreground='#C0C0C0',
                       font=35,
                       textvariable=StringVar(value='5'))
    time_entry.place(x=320, y=85, height=25, width=160)

    title_select_time = Label(frame_center, text='Enter message',
                              bg='#606060', font=40, foreground='#202020')
    title_select_time.place(x=360, y=120)

    time_button = Button(frame_center,
                         command=lambda: insert_text(time_entry, text_entry, action, time),
                         text='OK',
                         bg='#202020',
                         fg='#C0C0C0')
    time_button.place(x=480, y=85, height=25, width=40)

    text_entry = Text(frame_center,
                      height=8,
                      width=30,
                      background='#202020',
                      foreground='#C0C0C0',
                      wrap='word')
    text_entry.place(x=320, y=158)
    insert_text_asd = ('Пожалуйста сохраните все свои файлы и завершите корректно ваши сессии в программах. '
                       'Сервер будет перезагружен, через 5 минут. С уважением, отдел технической поддержки')
    text_entry.insert(END, insert_text_asd)

    # bottom panel
    frame_bottom = Frame(cache_form, bg='#202020')
    frame_bottom.place(relwidth=1, height=50, y=370)

    reset_server_button = Button(frame_bottom,
                                 command=lambda: run_shutdown(selected_servers,
                                                              time_entry,
                                                              text_entry,
                                                              action,
                                                              time),
                                 text='run shutdown',
                                 bg='#202020',
                                 fg='#C0C0C0')
    reset_server_button.place(x=360, y=10, height=25, width=100)

    cancel_button = Button(frame_bottom,
                           command=lambda: cancel_reset(selected_servers),
                           text='cancel shutdown',
                           bg='#202020',
                           fg='#C0C0C0')
    cancel_button.place(x=10, y=10, height=25, width=100)

    cache_form.mainloop()
