### Psuedo koden ###
# -- Eksempel: [1, 2, 2, 3, 4, 5, 5, 5, 6] --
#SET liste = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# -- Setter liste som lengde --
#SET lengde = LENGHT(liste)
# -- lager en tom liste --
#SET nyliste = []

# -- Antall like tall --
#FOR i = lengde TO 0 DO
    # -- Går igjennom alle tall i liste --
    #FOR j = MAX(liste) TO MIN(liste) DO
        # -- Tester om det er flere av samme tall --
        #IF(COUNT(j) == i) DO
            # -- Legger til like mange tall i ny liste --
            #FOR k = i TO 0 DO
                #SET nyliste[LENGHT(nyliste)] = j
            #ENDFOR
        #ENDIF
    #ENDFOR
#ENDFOR
#Resultat av eksempel [5, 5, 5, 2, 2, 6, 4, 3, 1]
#PRINT nyliste


### Python kode ###
# Funksjonen sorterer en liste etter typetall
def typetall(liste):
    lengde = len(liste)
    nyliste = []

    for i in range(lengde, 0, -1):
        for j in range(max(liste), min(liste)-1,-1):
            if liste.count(j) == i:
                for k in range(i, 0, -1):
                    nyliste.append(j)
    return nyliste


liste = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print(typetall(liste))