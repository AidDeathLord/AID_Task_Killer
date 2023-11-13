from task_killer.constants import PATH_TO_SRV_FILE
from task_killer.parser import open_server_file
from task_killer.errors import error_server_not_selected


def del_server(listbox):
    try:
        # remember the index of the selected element
        selection = listbox.curselection()
        # remember the content of the element
        selected_server = listbox.get(selection[0])

        # remove element from form
        listbox.delete(selection[0])

        # remove element from file
        server_list = open_server_file(PATH_TO_SRV_FILE)
        server_list.remove(str(selected_server))
        server_file = open(PATH_TO_SRV_FILE, 'w')
        for server in server_list:
            server_file.writelines(f'{server}\n')
    except IndexError:
        error_server_not_selected()


def open_form(server_listbox, form):
    try:
        # remember the index of the selected element
        selection = server_listbox.curselection()
        # remember the content of the element
        selected_server = server_listbox.get(selection[0])
        form(selected_server)
    except IndexError:
        error_server_not_selected()
