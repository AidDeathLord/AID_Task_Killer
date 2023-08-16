import os
import subprocess


NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# open file with servers list
def open_server_file(path):
    # check_server_file()
    servers = open(path, 'r')
    server_str = servers.readlines()
    result = []
    for i in server_str:
        result.append(i.strip())
    return sorted(result)


# if file does not exist creates it
# def check_server_file():
#     if not os.path.exists('server_list'):
#         os.mkdir('server_list')
#     if not os.path.exists('server_list/servers.txt'):
#         with open('server_list/servers.txt', 'x'):
#             pass


# opens tasks list on remote computer and outputs in the desired format
def get_tasks(server: str, user_id: str) -> list:
    # get tasks in str format
    tasks = subprocess.check_output(f'powershell.exe [Console]::OutputEncoding = [System.Text.Encoding]::UTF8\n'
                                    f' tasklist /Nh /fo:csv /s:{server}', universal_newlines=True)

    format_result = list()
    for elem in tasks.split('\n'):
        format_result.append(elem.split(','))

    result = list()
    for elem in format_result:
        if elem != ['']:
            if elem[3].replace('"', '') == user_id:
                result.append([elem[0].replace('"', ''), elem[1].replace('"', '')])

    return result


def get_users(server: str) -> dict:
    users = subprocess.check_output(f'powershell.exe Get-TerminalSession -ComputerName {server}| '
                                    f'Select-Object UserName, Id |'
                                    f' Format-Table -HideTableHeaders', universal_newlines=True)
    users_list = users.split()
    result = dict()
    index = 0
    while users_list[index][0] in NUMBERS:
        index += 1
    while index < len(users_list) - 1:
        result[users_list[index]] = users_list[index + 1]
        index += 2
    return result
