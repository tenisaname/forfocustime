import time
import tkinter
import customtkinter
import webbrowser
from win10toast_click import ToastNotifier

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
toaster = ToastNotifier()
app.geometry("400x240")
my_font = customtkinter.CTkFont(size=56)
hour = 59
minutes = 60
def clock():
    if running:
        global hour 
        global minutes
        if (minutes == 0):
            hour = hour  - 1
            minutes = 60
        minutes = minutes - 1
        label.configure(text= str(hour) + ":" + str(minutes))
        label.after(1000, clock)
        if (hour == 0):
            label.configure(text = "Focus is over")

def button_event():
    clock()
    button.configure(text="Stop Focus",command=stop)

def stop():
    global running
    running = False
    button.configure(text="Start Focus",command=start)
    
page_url = 'https://music.yandex.ru/users/TheChilledCow/playlists/1000'    
def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

def start():
    global running
    running = True
    button_event()
    toaster.show_toast(
    "Start Focus", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )

def restart():
    global hour 
    global minutes
    hour = 59
    minutes = 60
    label.configure(text="60:00")
    
label = customtkinter.CTkLabel(master=app, text="60:00",font=my_font)
label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
label.pack(pady=40)

button = customtkinter.CTkButton(master=app, text="Start Focus", command=start)
button2 = customtkinter.CTkButton(master=app, text="Retry", command=restart)
button.pack(padx=20, pady=10)
button2.pack(padx=10, pady=10)
app.mainloop()


