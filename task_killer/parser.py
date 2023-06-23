import os


def open_file():
    check_file()
    servers = open('server_list/servers.txt', 'r')
    server_str = servers.readlines()
    result = []
    for i in server_str:
        result.append(i.strip())
    return sorted(result)


def check_file():
    if not os.path.exists('server_list'):
        os.mkdir('server_list')
    if not os.path.exists('server_list/servers.txt'):
        with open('server_list/servers.txt', 'x'):
            pass
