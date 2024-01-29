import json
from pprint import pprint

import customtkinter as ctk

from classes.Player import Player


class PlayersList(ctk.CTkScrollableFrame):
    players = {}

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        try:
            with open('staticPlayers.json') as f:
                fileContent = f.read()
        except FileNotFoundError:
            self.createPlayersJson()
            fileContent = "{}"

        if fileContent == "":
            self.createPlayersJson()
            fileContent = "{}"

        players = json.loads(fileContent)
        pprint(players)

        self.setPlayers(players)

    def setPlayers(self, players):
        pprint(self.players)

        # Remove any players that aren't listed in the new list
        for pid in self.players.keys():
            if pid not in players.key():
                self.players[pid]['panel'].destroy()
                del self.players[pid]

        pprint(self.players)

        # Go over all players we've been given
        for pid in players.keys():
            # They already exist, nothing to do
            if pid in self.players.keys():
                ...
            # They don't exist, add them
            else:
                ply = self.createPlayerFrame(pid=pid, name=players[pid]['name'])

                self.players[pid] = {
                    'name': players[pid],
                    'panel': ply,
                }

        pprint(self.players)

    def createPlayerFrame(self, pid, name):
        ply = Player(master=self, pid=pid, name=name)
        ply.pack(expand=True)
        return ply

    def createPlayersJson(self):
        with open('staticPlayers.json', 'w') as f:
            f.write('{}')
