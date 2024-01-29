from tkinter import X

import customtkinter as ctk

from panels.Players import Players
from panels.AdminTools import AdminTools
from panels.ServerInfo import ServerInfo


class App(ctk.CTk):
    currentRow = 0

    def __init__(self):
        super().__init__()

        self.title("Palworld Admin Tool")

        self.geometry('500x400')

        self.tabview = ctk.CTkTabview(master=self)
        self.tabview.pack(padx=20, pady=20)

        self.tabview.add("Server Info")
        self.tabview.add("Players")
        self.tabview.add("Admin Tools")

        self.serverinfo = ServerInfo(master=self.tabview.tab("Server Info"))
        self.serverinfo.pack(fill=X)

        self.players = Players(master=self.tabview.tab("Players"))
        self.players.pack(fill=X)

        self.admintools = AdminTools(master=self.tabview.tab("Admin Tools"))
        self.admintools.pack(fill=X)

        # self.frame = AppFrame(master=self, activeSettingsToUse=activeSettings, width=550, height=700)
        # self.frame.grid(row=0, column=0, sticky='nsew')

        # lbl = ctk.CTkLabel(self, text="Admin Tools:")
        # lbl.grid(row=self.useRow(), column=1)
        #
        # self.saveBtn = ctk.CTkButton(self, text="Save", command=self.save)
        # self.saveBtn.grid(row=self.useRow(), column=1)

    def useRow(self):
        row = self.currentRow
        self.currentRow += 1

        self.grid_rowconfigure(row, weight=row, pad=1)

        return row

    def save(self):
        print('save')


app = App()
app.mainloop()
