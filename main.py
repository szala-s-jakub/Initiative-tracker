import tkinter as tk
from tkinter import messagebox
from ui.EntityEntry import EntityEntryWidget
from ui.AddEntityWidget import AddEntityWidget
from ui.EntityTable import EntityTable
from logic import *


# data
order = order()
order._append(entity("Kobold", 24, -2))
order._append(entity("Istota", 12, 4))
order._append(entity("Smok", 200, 10))

#  UI
okno = tk.Tk()
okno.title("Obsługa kolejki inicjatywa")
okno.geometry("600x400")

entities_table = EntityTable(parent=okno, order=order)

okno.mainloop()
