#Oppgave 1
def handleliste():
    handleliste = ["ost", "paprika", "brød", "kaviar"]
    m = str(input("legg til et element i lista: "))
    handleliste.insert(0, m)
    handleliste.remove("kaviar")
    handleliste[3] = "knekkebrød"
    print(handleliste)

handleliste()

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

tretyper()