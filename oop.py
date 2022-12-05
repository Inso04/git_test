class Bil:
    colour = ""
    maks_fart = 0
    min_fart = 0

    def __init__(self, maksfart, minfart):
        self.maks_fart = maksfart
        self.min_fart = minfart

    def kjør(self):
        print(f"Bilen kjører {self.maks_fart}km/t")
    def sving(self):
        print(f"Bilen svinger i {self.min_fart}km/t \n")

bmw = Bil(60, 5)
toyota = Bil(50, 2)

toyota.kjør()
bmw.sving()


print(bmw.colour)