from tkinter import *
from tkinter import messagebox
from task_killer.parser import get_users
import winreg
import os


GUID_LEN = 45
GUID_LEN_1C = 36


def open_users(server):
    users_info = get_users(server)
    return sorted(list(users_info.keys()))


def get_path_to_roaming(server: str, user='') -> list:
    result = []
    location = winreg.HKEY_LOCAL_MACHINE
    path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
    # get access to the registry of a remote computer
    remote_comp_location = winreg.ConnectRegistry(server, location)
    # link to registry key profile list
    profile_list = winreg.OpenKeyEx(remote_comp_location, path)
    # get the number of users
    profiles = winreg.QueryInfoKey(profile_list)
    users_number = profiles[0]
    for profile_num in range(users_number):
        user_guid = winreg.EnumKey(profile_list, profile_num)
        if len(user_guid) == GUID_LEN:
            try:
                user_path = path + '\\' + user_guid + '\\fdeploy'
                user_directs = winreg.OpenKeyEx(remote_comp_location, user_path)
                directs = winreg.QueryInfoKey(user_directs)
                directs_number = directs[0]
                for direct_num in range(directs_number):
                    direct = winreg.EnumKey(user_directs, direct_num)
                    direct_path = user_path + '\\' + direct
                    key = winreg.OpenKeyEx(remote_comp_location, direct_path)
                    a = winreg.QueryValueEx(key, 'PathEffective')
                    path_to_roaming = a[0]
                    if 'Roaming' in path_to_roaming:
                        if user in path_to_roaming:
                            path_to_cache = path_to_roaming + '\\1C\\1cv8'
                            result.append(path_to_cache)
            except FileNotFoundError:
                continue
    print(result)
    return result


def get_path_to_local(server, user=''):
    result = []
    location = winreg.HKEY_LOCAL_MACHINE
    path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
    # get access to the registry of a remote computer
    remote_comp_location = winreg.ConnectRegistry(server, location)
    # link to registry key profile list
    profile_list = winreg.OpenKeyEx(remote_comp_location, path)
    # get the number of users
    profiles = winreg.QueryInfoKey(profile_list)
    users_number = profiles[0]
    for profile_num in range(users_number):
        user_guid = winreg.EnumKey(profile_list, profile_num)
        if len(user_guid) == GUID_LEN:
            user_key = path + '\\' + user_guid
            key = winreg.OpenKeyEx(remote_comp_location, user_key)
            path_info = winreg.QueryValueEx(key, 'ProfileImagePath')
            path_to_direct = path_info[0]
            if user in path_to_direct:
                path_to_local = f'\\\\{server}\\C$\\Users\\{user}\\AppData\\Local\\1C\\1cv8'
                result.append(path_to_local)
    print(result)
    return result


def delete_cache(direct_list):
    result = ''
    for elem in direct_list:
        for filename in os.listdir(elem):
            if len(filename) == GUID_LEN_1C:
                result = result + filename + '\n'
    return result


def open_cache_form(server):
    def clear_cache():
        user = user_entry.get()
        users_roaming = get_path_to_roaming(server, user)
        users_local = get_path_to_local(server, user)

        message = delete_cache(users_local) + delete_cache(users_roaming)

        messagebox.showinfo(title='Result', message=message)

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

    run_button = Button(frame_center, command=clear_cache, text='Run', bg='#202020',
                        fg='#C0C0C0')
    run_button.place(x=490, y=35, height=26, width=40)

    # bottom panel
    frame_bottom = Frame(cache_form, bg="#202020")
    frame_bottom.place(relwidth=1, height=50, y=390)

    cache_form.mainloop()
