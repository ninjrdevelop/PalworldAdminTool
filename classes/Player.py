from tkinter import LEFT

import customtkinter as ctk
import pyperclip


class Player(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.pid = kwargs['pid']
        name = kwargs['name']

        del kwargs['pid']
        del kwargs['name']

        super().__init__(master, **kwargs)

        self.name = ctk.CTkLabel(master=self, text=name, width=200)
        # self.name.grid(row=0, column=0)
        self.name.pack(side=LEFT)

        self.goto = ctk.CTkButton(master=self, text="Go To", command=self.goto, width=100)
        # self.goto.grid(row=0, column=1)
        self.goto.pack(side=LEFT)

        self.bring = ctk.CTkButton(master=self, text="Bring", command=self.bring, width=100)
        # self.bring.grid(row=0, column=2)
        self.bring.pack(side=LEFT)

    def bring(self):
        pyperclip.copy(f'/TeleportToMe {self.pid}')

    def goto(self):
        pyperclip.copy(f'/TeleportToPlayer {self.pid}')
