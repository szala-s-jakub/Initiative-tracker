import tkinter as tk
from logic import order
from ui.components.AddEntityWidget import AddEntityWidget
from ui.components.EntityEntry import EntityEntryWidget


class EntityTable(tk.Frame):
    def __init__(self, parent, order, width=600):
        self.order = order
        self.index = 0
        self.entity_widget_list = []
        self.entities_frame = tk.Frame(parent)
        self.entities_frame.grid(row=2)
        # Konfiguracja kolumn aby istoty wyświetlały się równo
        COLUMN_COUNT = 5
        for i in range(COLUMN_COUNT):
            self.entities_frame.columnconfigure(i, minsize=width // 10 // COLUMN_COUNT)

        # Nagłówki kolumn
        header_frame = tk.Frame(parent, relief="raised", borderwidth=1)
        header_frame.grid(row=1, column=0, sticky="ew")

        COLUMN_COUNT = 5
        for i in range(COLUMN_COUNT):
            header_frame.columnconfigure(i, minsize=width // COLUMN_COUNT)
        # header_frame.columnconfigure(1, minsize=150)
        # header_frame.columnconfigure(2, minsize=150)
        # header_frame.columnconfigure(4, minsize=150)
        # header_frame.columnconfigure(3, minsize=150)

        tk.Label(header_frame, text="Nazwa").grid(row=0, column=0)
        tk.Label(header_frame, text="PW").grid(row=0, column=1)
        tk.Label(header_frame, text="Bonus Inicjatywy").grid(row=0, column=2)
        tk.Label(header_frame, text="Inicjatywa").grid(row=0, column=3)

        # Widget dodawania istot
        add_entity_widget = AddEntityWidget(
            parent=parent, order_object=self.order, onAdd=self.refresh_entities
        )
        add_entity_widget.grid(row=0, column=0, sticky="ew")

        # Przycisk rzucania inicjatywy
        roll_button = tk.Button(
            parent, text="Rzuć inicjatywę", command=self.roll_initiative
        )
        roll_button.grid(row=0, column=1, sticky="e")

        next_button = tk.Button(parent, text="Następna tura")
        next_button.grid(row=0, column=2, sticky="e")
        next_button["command"] = self.next_turn
        self.refresh_entities()  # Inicjalne wypełnienie tabeli


    def refresh_entities(self):
        self.index = 0
        for widget in self.entity_widget_list:
            widget.destroy()
        self.entity_widget_list.clear()
        for index, ent in enumerate(
            sorted(self.order, key=lambda e: e.initiative, reverse=True)
        ):
            ent_widget = EntityEntryWidget(
                parent=self.entities_frame,
                ent=ent,
                onDelete=lambda idx=index: self.delete_entity(idx),
            )
            ent_widget.grid(row=index + 1, column=0, sticky="ew")
            self.entity_widget_list.append(ent_widget)

    def delete_entity(self, index):
        self.order.remove_at_index(index)
        self.refresh_entities()

    def roll_initiative(self):
        self.order.roll_i_for_all()
        self.refresh_entities()
    def next_turn(self):
        # colors current to yellow
        self.entity_widget_list[self.index].config(bg="yellow")
        # colors children of widget to yellow
        for child in self.entity_widget_list[self.index].winfo_children():
            child.config(bg="yellow")
        prev_index = (self.index - 1) % len(self.entity_widget_list)
        self.entity_widget_list[prev_index].config(bg="SystemButtonFace")
        for child in self.entity_widget_list[prev_index].winfo_children():
            child.config(bg="SystemButtonFace")
            
        self.index = (self.index + 1) % len(self.entity_widget_list)

