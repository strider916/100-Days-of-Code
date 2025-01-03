import customtkinter
import paramiko
import pandas as pd
import socket
import time
import logging
import threading
from queue import Queue
from getpass import getpass

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")


def execute():
    print(tacacs_user.get())
    print(tacacs_pwd)
    print(dnac_ro_pwd)
    print(local_pwd)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Switch Credential Test", font=("Roboto", 24))
label.pack(pady=12, padx=10)

tacacs_user = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Username")
tacacs_user.pack(pady=12, padx=10)

tacacs_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Password", show="*")
tacacs_pwd.pack(pady=12, padx=10)

dnac_ro_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="DNAC TACACS Password", show="*")
dnac_ro_pwd.pack(pady=12, padx=10)

local_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="Local Device Password", show="*", )
local_pwd.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Execute", command=execute)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me", )
checkbox.pack(pady=12, padx=10)


root.mainloop()
results = []
queue = Queue()
start_time = time.time()
logging.basicConfig(
    filename="auth.log",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
    )




logging.warning(f'------------------------------ Start Runtime Log ------------------------------')

def worker():
    while not queue.empty():
        host = queue.get()
        connect(host)


def connect_all(threads):
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


some_function(8)
logging.warning(f'Process finished in {round((time.time() - start_time), 2)} seconds.')
logging.warning(f'------------------------------ End Runtime Log ------------------------------')
input(f'Process finished in {round((time.time() - start_time), 2)} seconds.\nPress enter to exit.')