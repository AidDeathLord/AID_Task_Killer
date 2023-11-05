from tkinter import *
from task_killer.functions.cache_form_functions import *
from task_killer.functions.general_functions import open_users


def open_cache_form(server):
    # tasks form
    cache_form = Toplevel()
    cache_form.title(f"{server}")

    cache_form['bg'] = '#fafafa'  # background color
    cache_form.geometry('+600+300')
    cache_form.resizable(width=False, height=False)

    # icon = PhotoImage(file='image/logo.png')
    # task_form.iconphoto(False, icon)

    canvas = Canvas(cache_form, height=430, width=600)
    canvas.pack()

    # top panel #
    frame_top = Frame(cache_form, bg="#202020")
    frame_top.place(relwidth=1, height=40)

    # Label Users
    title_add_server = Label(frame_top, text='Users',
                             bg='#202020', font=40, foreground='#C0C0C0')
    title_add_server.place(x=120, y=8)

    # center panel #
    frame_center = Frame(cache_form, bg="#606060")
    frame_center.place(relwidth=1, height=350, y=40)

    users = Variable(value=open_users(server))
    users_listbox = Listbox(frame_center, listvariable=users, bg="#202020",
                            bd=0, highlightbackground='#202020', fg='#C0C0C0',
                            font=30, selectbackground='#48BA6B')
    users_listbox.place(height=330, width=280, x=10, y=10)

    user_entry = Entry(frame_center, bg='#202020', width=30,
                       foreground='#C0C0C0', font=35)
    user_entry.place(x=300, y=10, height=25, width=190)

    run_button = Button(frame_center,
                        command=lambda: clear_cache(user_entry, server),
                        text='Run',
                        bg='#202020',
                        fg='#C0C0C0')
    run_button.place(x=490, y=35, height=26, width=40)

    # bottom panel
    frame_bottom = Frame(cache_form, bg="#202020")
    frame_bottom.place(relwidth=1, height=50, y=390)

    cache_form.mainloop()
