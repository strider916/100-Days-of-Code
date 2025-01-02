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
root.geometry("500x300")


def login():
    print("Test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()


tacacs_user = input("TACACS Username: ")
tacacs_pwd = getpass("TACACS Password: ")
dnac_ro_pwd = getpass("CCHCS-DNAC TACACS Password: ")
local_pwd = getpass("Local Device Password: ")
df = pd.read_csv('device_list.csv')
df.columns = [c.replace(' ', '_') for c in df.columns]
data_dict = df.to_dict(orient='records')
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
for device in data_dict:
    queue.put(device)


def connect(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    device_dict = {
        "Device_Name": host["Device_Name"],
        "IP_Address": host["IP_Address"],
        "Status": ""
    }
    try:
        print(f'Attempting SSH to {host["IP_Address"]} using TACACS.')
        logging.warning(f'Attempting SSH to {host["IP_Address"]} using TACACS.')
        ssh.connect(hostname=host["IP_Address"], username=tacacs_user, password=tacacs_pwd, timeout=5)
        device_dict["Status"] = "Success"
        print(f'TACACS Authentication to {host["IP_Address"]} was successful.')
        logging.warning(f'TACACS Authentication to {host["IP_Address"]} was successful.')
    except paramiko.ssh_exception.NoValidConnectionsError:
        device_dict["Status"] = "Connection Failure"
        print(f'Connection to {host["IP_Address"]} was unsuccessful.')
        logging.critical(f'Connection to {host["IP_Address"]} was unsuccessful.')
    except (paramiko.SSHException, paramiko.AuthenticationException, paramiko.BadAuthenticationType):
        try:
            print(f'User TACACS Failed. Attempting SSH to {host["IP_Address"]} using RO TACACS.')
            logging.critical(f'User TACACS Failed. Attempting SSH to {host["IP_Address"]} using RO TACACS.')
            ssh.connect(hostname=host["IP_Address"], username="cchcs-dnac", password=dnac_ro_pwd, timeout=4)
            device_dict["Status"] = "DNAC TACACS authentication Success"
            logging.warning(f'DNAC TACACS authentication to {host["IP_Address"]} was successful.')
        except (paramiko.SSHException, paramiko.AuthenticationException, paramiko.BadAuthenticationType):
            try:
                print(f'User and RO TACACS Failed. Attempting SSH to {host["IP_Address"]} using Local.')
                logging.critical(f'User and RO TACACS Failed. Attempting SSH to {host["IP_Address"]} using Local.')
                ssh.connect(hostname=host["IP_Address"], username="cchcs", password=local_pwd, timeout=4)
                print(f'Local authentication to {host["IP_Address"]} was successful.')
                logging.warning(f'Local authentication to {host["IP_Address"]} was successful.')
                device_dict["Status"] = "Local authentication Successful"
            except (paramiko.SSHException, paramiko.AuthenticationException, paramiko.BadAuthenticationType):
                print(f'Local Authentication to {host["IP_Address"]} was unsuccessful.')
                logging.critical(f'Local Authentication to {host["IP_Address"]} was unsuccessful.')
                device_dict["Status"] = "TACACS/Local authentication Failure"
    except socket.timeout:
        device_dict["Status"] = "Connection Timeout"
        print(f'Connection to {host["IP_Address"]} timed out.')
        logging.critical(f'Connection to {host["IP_Address"]} timed out.')
    results.append(device_dict)
    ssh.close()


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


connect_all(8)
df_results = pd.DataFrame(results)
try:
    df_results.to_csv('Connection_results.csv', index=False, mode='w')
    print("Results successfully exported to Connection_results.csv")
except PermissionError:
    print("Permission denied: You don't have the necessary permissions to create or modify Connection_results.csv.")
logging.warning(f'Process finished in {round((time.time() - start_time), 2)} seconds.')
logging.warning(f'------------------------------ End Runtime Log ------------------------------')
input(f'Process finished in {round((time.time() - start_time), 2)} seconds.\nPress enter to exit.')