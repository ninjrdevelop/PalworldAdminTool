import customtkinter as ctk


class ServerInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        l = ctk.CTkLabel(master=self, text="", width=450)
        l.pack()

