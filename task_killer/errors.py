from tkinter import messagebox


def error_add_server():
    messagebox.showerror(title="Error", message="Server is not available")


def error_server_in_the_list():
    messagebox.showerror(title="Error", message="Server is already in the list")


def error_empty_string():
    messagebox.showerror(title="Error", message="Server is not entered")


def error_server_not_selected():
    messagebox.showerror(title="Error", message="Server not selected")
