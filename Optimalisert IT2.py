#Oppgave 1
def handleliste():
    handleliste = ["ost", "paprika", "brød", "kaviar"]
    m = str(input("legg til et element i lista: "))
    handleliste.insert(0, m)
    handleliste.remove("kaviar")
    handleliste[3] = "knekkebrød"
    print(handleliste)

handleliste()