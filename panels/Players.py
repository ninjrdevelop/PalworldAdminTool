from tkinter import LEFT

import customtkinter as ctk
from classes.PlayersList import PlayersList


class Players(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        l = ctk.CTkLabel(master=self, text="", width=450)
        l.pack()

        playersList = PlayersList(master=self, width=450)
        playersList.pack(side=LEFT)


