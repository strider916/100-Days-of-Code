import customtkinter
import time
import logging
import threading
from queue import Queue
from PIL import Image

# GUI Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
width = 350
height = 500
spawn_x = int((root.winfo_screenwidth()-width)/2)
spawn_y = int((root.winfo_screenheight()-height)/2)
root.geometry(f"{width}x{height}+{spawn_x}+{spawn_y}")
root.minsize(width=350, height=500)
root.title("SSH Credential Test")
default_button_color = ['#3a7ebf', '#1f538d']
default_text_color = "white"
validate_button_color = "yellow"
validate_text_color = "black"
current_image = 0
images = [
    customtkinter.CTkImage(Image.open('C:\\Users\\T\\PycharmProjects\\100-Days-of-Code\\Tkinter\\hide.png'),
                           size=(26, 26)),
    customtkinter.CTkImage(Image.open('C:\\Users\\T\\PycharmProjects\\100-Days-of-Code\\Tkinter\\show.png'),
                           size=(26, 26))]

# Program Variables
results = []
start_time = 0.0

# Logging Startup Config
logging.basicConfig(
    filename="",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
    )

# Multithreading Functions
queue = Queue()


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


# GUI Functions
def on_closing():
    root.destroy()


def toggle_hide():
    global current_image
    if current_image == 0:
        current_image = 1
        image_button.configure(image=images[1])
        tacacs_pwd.configure(show="")
        dnac_ro_pwd.configure(show="")
        local_pwd.configure(show="")
    else:
        current_image = 0
        image_button.configure(image=images[0])
        tacacs_pwd.configure(show="*")
        dnac_ro_pwd.configure(show="*")
        local_pwd.configure(show="*")


def check_fields():
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
    if not checkbox1.get() == 1:
        checkbox1.configure(border_color="red")


def revalidate():
    if (not tacacs_user.get() or not tacacs_pwd.get() or not dnac_ro_pwd.get()
            or not local_pwd.get() or not checkbox1.get()):
        button.configure(text="Validate", command=validation_check, fg_color="red", hover_color="yellow",
                         text_color="black")
        validation_check()
    else:
        execute()


def validation_check():
    global validate_text_color, validate_button_color
    if tacacs_user.get() and tacacs_pwd.get() and dnac_ro_pwd.get() and local_pwd.get() and checkbox1.get():
        button.configure(text="Execute", command=revalidate, fg_color="green", hover_color="green")
        checkbox1.configure(fg_color="green", border_color="green", hover_color="green")
        check_fields()
    else:
        button.configure(text="Validate", command=validation_check, fg_color=validate_button_color,
                         text_color=validate_text_color)
        # add offset
        popup_x = root.winfo_x() + 85
        popup_y = root.winfo_y() + 180

        popup = customtkinter.CTkToplevel(root)
        # set toplevel in new position
        popup.geometry(f'+{popup_x}+{popup_y}')
        popup.grab_set()
        popup.title("Validation Failed")
        popuplabel = customtkinter.CTkLabel(popup, text="Missing information.")
        popuplabel.pack(padx=20, pady=10)
        popupbutton = customtkinter.CTkButton(popup, text="Acknowledge", command=popup.destroy)
        popupbutton.pack(padx=20, pady=10)
        check_fields()


def execute():
    global start_time
    start_time = time.time()
    logging.warning(f'------------------------------ Start runtime Log ------------------------------')
    # some_function(8)
    print(tacacs_user.get())
    print(tacacs_pwd.get())
    time.sleep(1)
    print(dnac_ro_pwd.get())
    print(local_pwd.get())
    root.quit()


# noinspection PyGlobalUndefined
def generate_interface():
    global tacacs_user, tacacs_pwd, dnac_ro_pwd, local_pwd, button, checkbox1, image_button
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=50, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Credentials", font=("Roboto", 20))
    label.pack(pady=12, padx=10)

    tacacs_user = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Username", width=175)
    tacacs_user.pack(pady=12, padx=10)

    tacacs_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="TACACS Password", width=175, show="*")
    tacacs_pwd.pack(pady=12, padx=10)

    dnac_ro_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="DNAC TACACS Password", width=175, show="*")
    dnac_ro_pwd.pack(pady=12, padx=10)

    local_pwd = customtkinter.CTkEntry(master=frame, placeholder_text="Local Device Password", width=175, show="*", )
    local_pwd.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Validate", command=validation_check,
                                     fg_color=validate_button_color,
                                     text_color=validate_text_color, hover_color=validate_button_color)
    button.pack(pady=12, padx=10)

    checkbox1 = customtkinter.CTkCheckBox(master=frame, text="I have read the README file")
    checkbox1.pack(pady=12, padx=10)

    image_button = customtkinter.CTkButton(master=frame, text="", image=images[current_image], compound="left",
                                           fg_color="transparent", width=26, command=toggle_hide)
    image_button.pack()


# GUI initialization
generate_interface()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()


# Final log Data
logging.warning(f'Process finished in {round((time.time() - start_time), 2)} seconds.')
logging.warning(f'------------------------------- End runtime Log --------------------------------')
