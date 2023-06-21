servers = open('server_list/servers.txt', 'r')

server_str = servers.readlines()
result = []
for i in server_str:
    result.append(i.strip())

server_list = sorted(result)
print(server_list)
