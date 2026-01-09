from tkinter  import *

def pole():
    p = float(pole1.get())*float(pole2.get()) # Pobiera tekst z pól tekstowych
    pole3.delete(0.0, END)
    pole3.insert(0.0, str(p))

def obwod():
    o=2*float(pole1.get())+2*float(pole2.get())
    pole4.delete(0.0,END)
    pole4.insert(0.0,str(o))


okno = Tk()
okno.title("Prostokat")
okno.geometry("400x240")
ramka = Frame(okno)
ramka.grid()

etykieta1 = Label(text = "Podaj bok a:")
etykieta1.grid(row=0, column=0, sticky=W)
pole1 = Entry()
pole1.grid(row=0, column=1, sticky=W)


etykieta2=Label(text="Podaj bok b:")
etykieta2.grid(row=1, column=0, sticky=W)
pole2=Entry()
pole2.grid(row=1, column=1, sticky=W)

przycisk1=Button(text="Oblicz pole", width=15)
przycisk1.grid(row=2, column=3, sticky=W)
przycisk1["command"] = pole
przycisk2=Button(text="Oblicz obwód", width=15)
przycisk2.grid(row=3, column=3, sticky = W)
przycisk2["command"] = obwod

etykieta3=Label(text="Pole:")
etykieta3.grid(row=4, column = 0, sticky=W)
pole3=Text(width=10, height=1, wrap=WORD)
pole3.grid(row=4, column= 1, sticky=W)

etykieta4=Label(text="Obwód:")
etykieta4.grid(row=3, column=0, sticky=W)
pole4=Text(width=10, height=1, wrap=WORD)
pole4.grid(row=4, column=1, sticky=W)

okno.mainloop()