import tkinter as tk
from tkinter import messagebox
from logic import *


class AddEntityWidget(tk.Frame):
    def __init__(self, parent, order_object: order, onAdd):
        tk.Frame.__init__(self, parent)
        self.order_object = order_object
        self.onAdd = onAdd

        self.nameLabel = tk.Label(self, text="Nazwa").grid(row=0, column=0)
        self.initiativeLabel = tk.Label(self, text="PW").grid(row=0, column=1)
        self.initiativeLabel = tk.Label(self, text="Inicjatywa").grid(row=0, column=2)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.grid(
            row=1, column=0
        )  # położenie widgetu jest robione w osobnym kroku aby self.NameEntry miało poprawną wartość. Grid nie zwraca referencji do widgetu

        self.healthEntry = tk.Entry(self)
        self.healthEntry.grid(
            row=1, column=1
        )  # położenie widgetu jest robione w osobnym kroku aby self.NameEntry miało poprawną wartość. Grid nie zwraca referencji do widgetu

        self.initiativeEntry = tk.Entry(self)
        self.initiativeEntry.grid(
            row=1, column=2
        )  # położenie widgetu jest robione w osobnym kroku aby self.NameEntry miało poprawną wartość. Grid nie zwraca referencji do widgetu
        self.add_button = tk.Button(self, text="Add", command=self.add_entity).grid(
            row=1, column=3
        )

        self.config(relief="groove", borderwidth=2)
        self.config(padx=5, pady=5)

    def add_entity(self):
        try:
            name = self.nameEntry.get()
            initiative = int(self.initiativeEntry.get())
            health = int(self.healthEntry.get())
            new_entity = entity(name, health, initiative, 0)
            self.order_object.append_entity(new_entity)
            self.onAdd()
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawne dane wejściowe")
