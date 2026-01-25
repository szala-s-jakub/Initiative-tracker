#  UI

import tkinter as tk
from ui.components.EntityTable import EntityTable
from logic import order


def init_ui(order_object: order):
    root = tk.Tk()
    root.title("Obsługa kolejki inicjatywy")
    root.geometry("900x400")

    entities_table = EntityTable(parent=root, order=order_object)

    root.mainloop()
