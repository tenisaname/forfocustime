import customtkinter
import tkinter
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)
        label = customtkinter.CTkLabel(master= app, text="CTkLabel")
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()