import winreg
import os
import shutil
from tkinter import messagebox


GUID_LEN = 45
GUID_LEN_1C = 36


def get_paths(server: str, user='') -> list:
    def get_path_to_roaming():
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
                        return path_to_cache
        except FileNotFoundError:
            return get_path_to_local_files('Roaming')

    def get_path_to_local_files(directory):
        user_key = path + '\\' + user_guid
        key = winreg.OpenKeyEx(remote_comp_location, user_key)
        path_info = winreg.QueryValueEx(key, 'ProfileImagePath')
        path_to_direct = path_info[0]
        if user in path_to_direct:
            user_name = path_to_direct.split('\\')[-1]
            path_to_local = f'\\\\{server}\\C$\\Users\\{user_name}\\AppData\\{directory}\\1C\\1cv8'
            return path_to_local

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
        if len(user_guid) == GUID_LEN or len(user_guid) == 44:
            result.append(get_path_to_roaming())
            result.append(get_path_to_local_files('Local'))
    return result


def delete_cache(direct_list):
    result = ''
    error = 'Error:\n'
    for elem in direct_list:
        try:
            for filename in os.listdir(elem):
                if len(filename) == GUID_LEN_1C:
                    path_to_rm_direct = elem + '\\' + filename
                    try:
                        shutil.rmtree(path_to_rm_direct)
                        result = result + elem + '\\' + filename + '\n'
                    except PermissionError:
                        error = error + elem + '\\' + filename + '\n'

        except FileNotFoundError:
            error = error + elem + '\n'

    return result, error


def clear_cache(entry, server):
    user = entry.get()
    info = get_paths(server, user)
    result, error = delete_cache(info)
    message = result + error
    messagebox.showinfo(title='Result', message=message)
