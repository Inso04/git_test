#Importerer biblotek
import csv
import matplotlib.pyplot as plt

#Lager klassen Datasett
class Datasett:
    def __init__(self, filnavn):
        # Konstruktøren tar inn filnavnet og oppretter variabler for startlokasjoner og antall turer per dag
        self.filnavn = filnavn
        self.startlokasjoner = {}
        self.turer_per_dag = {}

    def count_startlokasjoner(self):
        # Teller antall ganger av hver startlokasjon i filen
        with open(self.filnavn, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                startlokasjon = row['start_station_name']
                if startlokasjon in self.startlokasjoner:
                    self.startlokasjoner[startlokasjon] += 1
                else:
                    self.startlokasjoner[startlokasjon] = 1

    def mestBrukteStasjon(self):
        #Finner de tre mest brukte startlokasjonene
        return sorted(self.startlokasjoner.items(), key=lambda x: x[1], reverse=True)[:3]

    def minstBrukteStasjon(self):
        #Finner de tre minst brukte startlokasjonene
        return sorted(self.startlokasjoner.items(), key=lambda x: x[1])[:3]

    def count_turer_per_dag(self):
        #Teller antall turer per dag i måneden
        for dag in range(1, 32):
            self.turer_per_dag[dag] = 0

        with open(self.filnavn, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                starttidspunkt = row['started_at']
                dag = int(starttidspunkt.split('-')[2].split()[0])
                self.turer_per_dag[dag] += 1

    def plot_turer_per_dag(self):
        #Lager et diagram som viser antall turer per dag i måneden
        antall_turer = [self.turer_per_dag[dag] for dag in range(1, 32)]

        plt.bar(range(1, 32), antall_turer, color="green")
        plt.title('Antall turer i mai')
        plt.xlabel('Dager i mai')
        plt.ylabel('Antall turer')
        plt.show()

    def run(self):
        #Kjører alle de andre metodene i riktig rekkefølge
        self.count_startlokasjoner()
        mest_brukt = self.mestBrukteStasjon()
        minst_brukt = self.minstBrukteStasjon()

        print("De tre mest brukte startlokasjonene er:")
        for lokasjon, antall in mest_brukt:
            print(f"{lokasjon} {antall} ganger")

        print("\nDe tre minst brukte startlokasjonene er:")
        for lokasjon, antall in minst_brukt:
            print(f"{lokasjon} {antall} ganger")

        self.count_turer_per_dag()
        self.plot_turer_per_dag()

if __name__ == '__main__':
    data = Datasett('05.csv')
    data.run()