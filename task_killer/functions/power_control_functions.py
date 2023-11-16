from tkinter import *
import subprocess
import datetime


def add_server_in_select_list(listbox, selected_servers_listbox):
    # add selected server in second listbox
    selection = listbox.curselection()
    selected_server = listbox.get(selection[0])
    selected_servers_listbox.insert(0, selected_server)
    # remove element from first listbox
    listbox.delete(selection[0])


def remove_from_select_list(listbox, selected_servers_listbox):
    selection = selected_servers_listbox.curselection()
    selected_server = selected_servers_listbox.get(selection[0])
    listbox.insert(0, selected_server)
    selected_servers_listbox.delete(selection[0])


def get_time(time_entry, time_variable):
    if time_variable.get() == 'after':
        return int(time_entry.get()) * 60
    elif time_variable.get() == 'to':
        current_time = datetime.datetime.now()
        dt_obj = datetime.datetime.strptime(time_entry.get(), '%H:%M %d-%m-%Y')
        time_delta = dt_obj - current_time
        seconds = time_delta.total_seconds()
        return int(seconds)


def run_shutdown(selected_servers_listbox,
                 time_entry, text_entry,
                 action_variable,
                 time_variable):

    selected_servers = selected_servers_listbox.get(0, END)
    text = text_entry.get('1.0', END)
    time = get_time(time_entry, time_variable)

    if action_variable.get() == 'reset':
        for server in selected_servers:
            command = f"powershell.exe [Console]::OutputEncoding = [System.Text.Encoding]::UTF8\n" \
                      f"shutdown /r /m \\\\{server} /t {str(time)} /c '{text}'"
            subprocess.call(command)
    if action_variable.get() == 'off':
        for server in selected_servers:
            command = f"powershell.exe [Console]::OutputEncoding = [System.Text.Encoding]::UTF8\n" \
                      f"shutdown /s /t {str(time)} /m \\\\{server} /c '{text}'"
            subprocess.call(command)


def off(selected_servers_listbox, time_entry, text_entry, variable):
    selected_servers = selected_servers_listbox.get(0, END)
    text = text_entry.get('1.0', END)
    time = get_time(time_entry, variable)

    for server in selected_servers:
        command = f"powershell.exe [Console]::OutputEncoding = [System.Text.Encoding]::UTF8\n" \
                  f"shutdown /r /m \\\\{server} /t {str(time)} /c '{text}'"
        subprocess.call(command)


def cancel_reset(selected_servers_listbox):
    selected_servers = selected_servers_listbox.get(0, END)
    for server in selected_servers:
        command = f'shutdown /a /m \\\\{server}'
        subprocess.call(command)


def on_select_after(entry):
    entry.delete(0, END)
    entry.insert(0, '5')


def on_select_to(entry):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M %d-%m-%Y")
    entry.delete(0, END)
    entry.insert(0, current_time)


def insert_text(time_entry, text_entry, action_variable, time_variable):
    def insert(entry, text):
        entry.delete(1.0, END)
        entry.insert(1.0, text)
    if action_variable.get() == 'reset':
        if time_variable.get() == 'after':
            time = time_entry.get()
            new_text = (f'Пожалуйста сохраните все свои файлы и завершите корректно ваши сессии в программах. '
                        f'Сервер будет перезагружен, через {time} минут. С уважением, отдел технической поддержки.')
            insert(text_entry, new_text)
        elif time_variable.get() == 'to':
            time = time_entry.get()
            new_text = f'Сервер будет перезагружен  в {time}. С уважением, отдел технической поддержки.'
            insert(text_entry, new_text)
    if action_variable.get() == 'off':
        if time_variable.get() == 'after':
            time = time_entry.get()
            new_text = f'Сервер будет выключен, через {time} минут.'
            insert(text_entry, new_text)
        elif time_variable.get() == 'to':
            time = time_entry.get()
            new_text = f'Сервер будет выключен {time}.'
            insert(text_entry, new_text)
