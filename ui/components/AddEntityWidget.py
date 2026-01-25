import tkinter as tk
from tkinter import messagebox
from logic import *


class AddEntityWidget(tk.Frame):
    def __init__(self, parent, order_object: order, onAdd):
        tk.Frame.__init__(self, parent)
        self.order_object = order_object
        self.onAdd = onAdd

        self.nameLabel = tk.Label(self, text="Nazwa").grid(row=0, column=0)
        self.initiativeLabel = tk.Label(self, text="Maks. PW").grid(row=0, column=1)
        self.initiativeLabel = tk.Label(self, text="Bonus Inicjatywy").grid(row=0, column=2)
        self.ammountLabel= tk.Label(self, text="Ilość").grid(row=0, column=3)
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
        
        self.ammountEntry = tk.Entry(self)
        self.ammountEntry.grid(
            row=1, column=3
        )
        self.ammountEntry.insert(0, "1")
        self.add_button = tk.Button(self, text="Add", command=self.add_entity).grid(
            row=1, column=4
        )

        self.config(relief="groove", borderwidth=2)
        self.config(padx=5, pady=5)

    def add_entity(self):
        try:

            name = self.nameEntry.get()
            initiative = int(self.initiativeEntry.get())
            health = int(self.healthEntry.get())
            if int(self.ammountEntry.get()) < 1:
                raise ValueError("Ilość musi być większa niż 0")
            elif int(self.ammountEntry.get()) == 1:
                new_entity = entity(name, health, initiative, 0)
                self.order_object.append_entity(new_entity)
            else:
                for i in range(int(self.ammountEntry.get())):
                    new_entity = entity(name + " " + str(i+1), health, initiative, 0)
                    self.order_object.append_entity(new_entity)
            self.onAdd()
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))
