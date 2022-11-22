def push(liste, ting):
    #legger til et element på starten av listen
    liste.insert(0, ting)

def pop(liste):
    #fjerner et element fra slutten av listen
    liste.remove(liste[len(liste)- 1])

handlekurv = ["ost", "paprika", "brød", "kaviar"]
push(handlekurv, "ketchup")
handlekurv[3] = "knekkebrød"
pop(handlekurv)
print(handlekurv)