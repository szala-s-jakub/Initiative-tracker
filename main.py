from tkinter import *

okno=Tk()

okno.title("Obsługa kolejki inicjatywa")
okno.geometry("500x400")

ramka = Frame(okno)
ramka.grid()

przycisk=Button(ramka)
przycisk["text"] = "Kliknięto 0 razy"
przycisk.grid()
przycisk.licznik=0 #utworzenie atrybutu klasy

def update():
    przycisk.licznik += 1
    przycisk["text"] = "Kliknieto " + str(przycisk.licznik) + " razy"
przycisk["command"] = update #bierzemy naszą funkcję bez nawiasów

etykieta = Label(ramka)
etykieta["text"] = "To jest etykieta"
etykieta.grid()
okno.mainloop()


