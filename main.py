import time
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
my_font = customtkinter.CTkFont(size=56)
hour = 59
minutes = 60
def clock():
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

label = customtkinter.CTkLabel(master=app, text="",font=my_font)
label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
label.pack(pady=40)



button = customtkinter.CTkButton(master=app, text="CTkButton", command=clock())
button.pack(padx=20, pady=10)

clock()
app.mainloop()


