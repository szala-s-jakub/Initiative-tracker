import tkinter as tk
from logic import *


class EntityEntryWidget(tk.Frame):
    def __init__(self, parent, ent: entity, onDelete):
        self.entity = ent
        self.onDelete = onDelete
        tk.Frame.__init__(self, parent)

        # Konfiguracja kolumn tak aby wyświetlały sie równo razem z nagłówkami
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(1, minsize=120)
        self.columnconfigure(2, minsize=120)
        self.columnconfigure(3, minsize=120)
        self.columnconfigure(4, minsize=120)

        self.entity_name = tk.Label(self, text=ent.name, anchor="center")
        self.entity_name.grid(row=0, column=0, sticky="ew", padx=5)

        self.entity_hp = tk.Label(self, text=ent.hp, anchor="center")
        self.entity_hp.grid(row=0, column=1, sticky="ew", padx=5)

        self.entity_base_initiative_stat = tk.Label(
            self, text=ent.initiative_bonus, anchor="center"
        )
        self.entity_base_initiative_stat.grid(row=0, column=2, sticky="ew", padx=5)

        self.entity_initiative = tk.Label(self, text=ent.initiative, anchor="center")
        self.entity_initiative.grid(row=0, column=3, sticky="ew", padx=5)
        self.entity_initiative.config(font=("Arial", 12, "bold"))

        self.delete_button = tk.Button(self, text="X", command=self.onDelete)
        self.delete_button.grid(row=0, column=4, padx=5)

    def update_display(
        self,
        ent: entity,
    ):
        """Update the widget to display new entity data"""
        self.entity = ent
        self.entity_name.config(text=ent.name)
        self.entity_base_initiative_stat.config(text=ent.initiative_bonus)
        self.entity_initiative.config(text=ent.initiative)
