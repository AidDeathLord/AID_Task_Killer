import subprocess
from task_killer.parser import get_users
from task_killer.errors import *
from task_killer.parser import open_server_file
from task_killer.constants import PATH_TO_SRV_FILE


def open_users(server):
    users_info = get_users(server)
    return sorted(list(users_info.keys()))


def add_server(entry, *args):
    new_server = entry.get()
    server_list = open_server_file(PATH_TO_SRV_FILE)
    if new_server in server_list:
        error_server_in_the_list()
    else:
        if add_srv_in_txt(new_server):
            for listbox in args:
                listbox.insert(0, new_server)
        elif new_server == '':
            error_empty_string()
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
