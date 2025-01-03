import customtkinter
import time
import logging
import threading
from queue import Queue
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500+500+250")
root.title("SSH Credential Test")
results = []
start_time = 0.0
queue = Queue()
logging.basicConfig(
    filename="",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
    )
hide_icon = customtkinter.CTkImage(Image.open('hide.png'), size=(26, 26))
show_icon = customtkinter.CTkImage(Image.open('show.png'), size=(26, 26))


def worker():
    while not queue.empty():
        host = queue.get()
        assign_workers(host)


def assign_workers(threads):
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


def on_closing():
    root.destroy()


def execute():
    global start_time
    start_time = time.time()
    logging.warning(f'------------------------------ Start Runtime Log ------------------------------')
    # some_function(8)
    print(tacacs_user.get())
    print(tacacs_pwd.get())
    print(dnac_ro_pwd.get())
    print(local_pwd.get())


def toggle_hide():
    if pwd_visibility.get():
        tacacs_pwd.configure(show="")
        dnac_ro_pwd.configure(show="")
        local_pwd.configure(show="")
        pwd_visibility.configure(text="Unhide")
    else:
        tacacs_pwd.configure(show="*")
        dnac_ro_pwd.configure(show="*")
        local_pwd.configure(show="*")
        pwd_visibility.configure(text="Hide")


def run_check():
    if (tacacs_user.get() and tacacs_pwd.get() and dnac_ro_pwd.get() and local_pwd.get() and checkbox1.get()
            and checkbox2.get() and checkbox3.get()):
        button.configure(text="Execute", command=execute, hover_color="green")
    else:
        # get main window position
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()

        # add offset
        popup_x = root_x + 165
        popup_y = root_y + 150

        popup = customtkinter.CTkToplevel()

        # set toplevel in new position
        popup.geometry(f'+{popup_x}+{popup_y}')
        popup.title("Validation Failed")
        popuplabel = customtkinter.CTkLabel(popup, text="Please fill all fields.")
        popuplabel.pack(padx=20, pady=10, )
        popupbutton = customtkinter.CTkButton(popup, text="Acknowledge", command=popup.destroy)
        popupbutton.pack(padx=20, pady=10)

        if not tacacs_user.get():
            tacacs_user.configure(border_color="red")
        else:
            tacacs_user.configure(border_color="green")
        if not tacacs_pwd.get():
            tacacs_pwd.configure(border_color="red")
        else:
            tacacs_pwd.configure(border_color="green")
        if not dnac_ro_pwd.get():
            dnac_ro_pwd.configure(border_color="red")
        else:
            dnac_ro_pwd.configure(border_color="green")
        if not local_pwd.get():
            local_pwd.configure(border_color="red")
        else:
            local_pwd.configure(border_color="green")
        if not checkbox1.get():
            checkbox1.configure(border_color="red")
        else:
            checkbox1.configure(border_color="green")
        if not checkbox2.get():
            checkbox2.configure(border_color="red")
        else:
            checkbox2.configure(border_color="green")
        if not checkbox3.get():
            checkbox3.configure(border_color="red")
        else:
            checkbox3.configure(border_color="green")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Required Fields:", font=("Roboto", 20))
label.pack(pady=12, padx=10)

image_button = customtkinter.CTkButton(master=frame, text="", image=hide_icon, )
image_button.pack()

pwd_visibility = customtkinter.CTkCheckBox(master=frame, height=2, width=10, command=toggle_hide, text="Unhide")
pwd_visibility.pack()

tacacs_user = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Username", width=200)
tacacs_user.pack(pady=12, padx=10)

tacacs_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Password", width=200, show="*")
tacacs_pwd.pack(pady=12, padx=10)


dnac_ro_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="DNAC TACACS Password", width=200, show="*")

dnac_ro_pwd.pack(pady=12, padx=10)

local_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="Local Device Password", width=200, show="*", )
local_pwd.pack(pady=12, padx=10)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Input file in CSV format")
checkbox1.pack(pady=12, padx=10)

checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Input file contains IP_Address and Hostname columns")
checkbox2.pack(pady=12, padx=10)

checkbox3 = customtkinter.CTkCheckBox(master=frame, text="Input file in CSV format", )
checkbox3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Validate", command=run_check, hover_color="red")
button.pack(pady=12, padx=10)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
logging.warning(f'Process finished in {round((time.time() - start_time), 2)} seconds.')
logging.warning(f'------------------------------- End Runtime Log --------------------------------')
