import tkinter as tk
from ui.components.AddEntityWidget import AddEntityWidget
from ui.components.EntityEntry import EntityEntryWidget


class EntityTable(tk.Frame):
    def __init__(self, parent, order):
        self.order = order
        self.entity_widget_list = []
        self.entities_frame = tk.Frame(parent)
        self.entities_frame.grid(row=2)
        # Konfiguracja kolumn aby istoty wyświetlały się równo
        for i in range(4):
            self.entities_frame.columnconfigure(i, minsize=120)

        # Nagłówki kolumn
        header_frame = tk.Frame(parent, relief="raised", borderwidth=1)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.columnconfigure(0, minsize=150)
        header_frame.columnconfigure(1, minsize=150)
        header_frame.columnconfigure(2, minsize=150)
        header_frame.columnconfigure(3, minsize=150)

        tk.Label(header_frame, text="Nazwa").grid(row=0, column=0)
        tk.Label(header_frame, text="Bonus Inicjatywy").grid(row=0, column=1)
        tk.Label(header_frame, text="Inicjatywa").grid(row=0, column=2)

        # Widget dodawania istot
        add_entity_widget = AddEntityWidget(
            parent=parent, order_object=self.order, onAdd=self.refresh_entities
        )
        add_entity_widget.grid(row=0, column=0, sticky="ew")

        # Przycisk rzucania inicjatywy
        roll_button = tk.Button(
            parent, text="Rzuć inicjatywę", command=self.roll_initiative
        )
        roll_button.grid(row=0, column=0)

        self.refresh_entities()  # Inicjalne wypełnienie tabeli

    def refresh_entities(self):
        for widget in self.entity_widget_list:
            widget.destroy()
        self.entity_widget_list.clear()
        for index, ent in enumerate(self.order):
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
