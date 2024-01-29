import customtkinter as ctk


class AdminTools(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        l = ctk.CTkLabel(master=self, text="", width=450)
        l.pack()

        self.broadcastBtn = ctk.CTkButton(master=self, text="Broadcast Message", command=self.broadcast)
        self.broadcastBtn.pack()

        self.shutdownBtn = ctk.CTkButton(master=self, text="Shutdown", command=self.shutdown)
        self.shutdownBtn.pack()

    def shutdown(self):
        dialog = ctk.CTkInputDialog(text='Enter message to send to players:', title="Shutdown Message")
        text = dialog.get_input().replace(' ', '_')

        if text:
            print(f'Shutting down server in 60s with the message: "{text}"')

    def broadcast(self):
        dialog = ctk.CTkInputDialog(text='Enter message to send to players:', title="Broadcast Message")
        text = dialog.get_input().replace(' ', '_')

        if text:
            print(f'Broadcasting message to players: "{text}"')
