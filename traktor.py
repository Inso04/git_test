class traktor:
    def __init__(self, foran, bak, venstre, høyre):
        self._foran = foran
        self._bak = bak
        self._venstre = venstre
        self._høyre = høyre

    def kjør(self):
        print(f"Traktoren kjører i {self._foran}km/t")
    
    def rygge(self):
        print(f"Traktoren rygger i {self._bak}km/t")
        
    def venstre(self):
        print(f"Traktoren svinger til venstre i {self._venstre}km/t")
    
    def høyre(self):
        print(f"Traktoren svinger til høyre i {self._høyre}km/t")
    
    def stopp(self):
        print("Traktoren stoppet")

suukhiimobil = traktor(30, 5, 10, 10)
matsmobil = traktor(40, 5, 15, 15)

matsmobil.venstre()