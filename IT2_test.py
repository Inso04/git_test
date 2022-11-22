#funksjoner
def push(liste, ting):
    #legger til et element på starten av listen
    liste.insert(0, ting)

def pop(liste):
    #fjerner et element fra slutten av listen
    liste.remove(liste[len(liste)- 1])

def rem(liste, antall):
    #fjerner så mange elementer man vil fra listen
    length = len(liste)
    for i in range(antall):
        liste.remove(liste[(length - antall)])

#oppgave 1
handlekurv = ["ost", "paprika", "brød", "kaviar"]
push(handlekurv, "ketchup")
handlekurv[3] = "knekkebrød"
pop(handlekurv)
print(handlekurv)

#oppgave 2
tretyper = ["lønn", "hassel", "bjørk", "eik", "blodlønn", "furu", "gran"]
tretyper.remove("eik")
tretyper[2] = "hengebjørk"
rem(tretyper, 2)
tretyper.append("fjellbjørk")
tretyper.append("dvergbjørk")
tretyper = sorted(tretyper)
print(tretyper)

#oppgave 3


#oppgave 4


#oppgave 5
tall = [4, 45, 32, 19, 100]
tall = sorted(tall)
print(tall)

#oppgave 6
liste = []
a = int(input("Skriv hvor mange elementer du vi ha i listen: "))

for i in range(0, a):
    liste.append(input(f"Element {i+1}: "))

print(liste)