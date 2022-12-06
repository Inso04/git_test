'''
Data:
- Kjønn
- Høyde
- Alder
- Hårfarge
- Øyenfarge
- Favorittfarge

Metoder:
- Gå
- Sove (alder)
- Spille 
- Sitte (kjønn)
- Løpe
- - > Hastighet (høyde)

- Tisse
- - > Står eller sitter (kjønn)
- - > Vanskelighetsgrad (alder)

- Spise
- Drikke
'''

class Person:
    def __init__(self, kjønn: str, høyde: int, alder: int, hårfarge: str, øyenfarge: str, favfarge: str):
        self._kjønn = kjønn
        self._høyde = høyde
        self._alder = alder
        self._hårfarge = hårfarge
        self._øyenfarge = øyenfarge
        self._favorittfarge = favfarge

    def Gå(self):
        print("Personen går")

    def Sove(self):
        if self._alder < 3 or self._alder > 50:
            print("Personen sover i 8 timer")
        else:
            print("Personen sover i 6 timer")

    def Spille(self):
        print("Personen spiller")

    def Sitte(self):
        if self._kjønn == "Mann":
            print("Personen manspreader")
        else:
            print("Personen sitter")

    def Løpe(self):
        if self._høyde < 150:
            print("Personen løper i lav hastighet")
        elif self._høyde > 180:
            print("Personen løper i høy hastighet")
        else:
            print("Personen løper i normal hastighet")

    def Tisse(self):
        if self._kjønn == "Mann":
            print("Personen står å tisser")
        else:
            print("Personen sitter og tisser")
        
        if self._alder > 75:
            print("Personen har vansker med å tisse")
        else:
            print("Personen tisser normalt")

    def Spise(self):
        print("Personen spiser")

    def Drikke(self):
        print("Personen drikker")
