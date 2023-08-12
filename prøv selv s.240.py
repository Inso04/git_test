import matplotlib.pyplot as plt

#Oppgave 1
def drueliggene():
    uker = ['Uke 1', 'Uke 2', 'Uke 3', 'Uke 4']
    kg_druer = [2.1, 1.7, 2.4, 0.2]
    plt.barh(uker, kg_druer)
    plt.title('Mengde druer kastet per uke')
    plt.xlabel('Kilogram')
    plt.show()

def druestående():
    uker = ['Uke 1', 'Uke 2', 'Uke 3', 'Uke 4']
    kg_druer = [2.1, 1.7, 2.4, 0.2]
    plt.bar(uker, kg_druer)
    plt.title('Mengde druer kastet per uke')
    plt.xlabel('Kilogram')
    plt.show()

#Oppgave 2
def brød():
    elever = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    brødskiver = [38, 26, 8, 25, 32, 38, 17, 41, 37, 19, 33, 29]
    plt.bar(elever, brødskiver)
    plt.title('Antall brødskiver elever spiser per uke')
    plt.xlabel('brød')
    plt.show()

#Oppgave 3
def temp():
    måneder = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']
    temperatur = [1.2, 1.1, 2.8, 5.5, 9.9, 12.8, 14.1, 14.4, 11.7, 8.8, 4.8, 2.5]
    plt.plot(måneder, temperatur, '-o')
    plt.title('Middeltemperaturen i Stavanger på ett år')
    plt.xlabel('celsius')
    plt.show()

#Oppgave 4
def strøm():
    måneder = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai']
    kwh = [650, 400, 350, 300, 200]
    plt.plot(måneder, kwh, '-o')
    plt.grid(True)
    plt.title('Mengden kWh jeg har brukt de siste månedene')
    plt.xlabel('kWh')
    plt.show()

#Oppgave 5
def dyr():
    plt.pie([5, 8, 2, 12], labels=['hund', 'katt', 'undulat', 'ingen kjæledyr'], autopct='%.1f%%')
    plt.show()

def atomos():
    plt.pie([78.1, 20.9, 0.9, 0.038], labels=['nitrogen', 'oksygen', 'argon', 'karbondioksid'], autopct='%.1f%%')
    plt.show()

def nettlesere():
    plt.pie([13, 10, 1], labels=['google', 'edge', 'Opera GX'], autopct='%.1f%%')
    plt.show()

drueliggende()
druestående()
brød()
temp()
strøm()
dyr()
atomos()
nettlesere()