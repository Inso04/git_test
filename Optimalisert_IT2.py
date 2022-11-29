#Oppgave 1
def handleliste():
    handleliste = ["ost", "paprika", "brød", "kaviar"]
    m = str(input("legg til et element i lista: "))
    handleliste.insert(0, m)
    handleliste.remove("kaviar")
    handleliste[3] = "knekkebrød"
    print(handleliste)

#Oppgave 2
def tretyper():
    tre = ["lønn", "hassel", "bjørk", "eik", "blodlønn", "furu", "gran"]
    tre.remove("eik")
    tre[2] = "hengebjørk"
    tre.remove("furu")
    tre.remove("gran")
    tre.append("fjellbjørk")
    tre.append("dvergbjørk")
    tre = sorted(tre)
    print(tre)

#Oppgave 3


#Oppgave 4


#Oppgave 5
def tall():
    tall = []
    for i in range(0, 5):
        tall.append(int(input(f"Element {i+1}: ")))
    tall = sorted(tall)
    print(tall)

#Oppgave 6a
def liste():
    liste = []
    a = int(input("Skriv hvor mange elementer du vi ha i listen: "))
    for i in range(0, a):
        liste.append(input(f"Element {i+1}: "))
    print(liste)

#Oppgave 6b
from tkinter import *
def list_with_select_element():
    liste = []
    slutt = int(input("Skriv hvor mange elementer du vil ha i listen: "))
    for i in range(0, slutt):
         liste.append(input(f"Element {i+ 1}: ")) 

    start = Tk()
    start.geometry( "200x200" )
    var = StringVar()

    drop = OptionMenu( start , var ,*liste )
    drop.pack()
    start.mainloop()

#Oppgave svarene
handleliste()
tretyper()
#Oppg 3
#Oppg 4
tall()
liste()
list_with_select_element()