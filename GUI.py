from Belfoldi import BelfoldiJarat
from Nemzetkozi import NemzetkoziJarat


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

    def list_jaratok(self):
        for jarat in self.jaratok:
            print(jarat.get_info())


class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas_hozzaadasa(self, jarat, nev):
        self.foglalasok.append({"nev": nev, "jarat": jarat})
        print(f"Foglalás sikeres: {nev} - {jarat.jaratszam}")
        return jarat.jegyar

    def foglalas_lemondasa(self, jaratszam, nev):
        for foglalas in self.foglalasok:
            if foglalas["jarat"].jaratszam == jaratszam and foglalas["nev"] == nev:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás lemondva: {nev} - {jaratszam}")
                return
        print("Nincs ilyen foglalás.")

    def list_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Név: {foglalas['nev']}, Járat: {foglalas['jarat'].jaratszam}")


def main():
    legi_tarsasag = LegiTarsasag("FlySafe Airlines")
    jarat1 = BelfoldiJarat("B123", "Budapest", 10000)
    jarat2 = NemzetkoziJarat("I456", "New York", 50000)
    jarat3 = BelfoldiJarat("B789", "Debrecen", 8000)

    legi_tarsasag.add_jarat(jarat1)
    legi_tarsasag.add_jarat(jarat2)
    legi_tarsasag.add_jarat(jarat3)

    foglalasok = JegyFoglalas()
    foglalasok.foglalas_hozzaadasa(jarat1, "Kovács Anna")
    foglalasok.foglalas_hozzaadasa(jarat2, "Nagy Béla")

    while True:
        print("\n1. Járatok listája\n2. Jegy foglalása\n3. Foglalás lemondása\n4. Foglalások listázása\n5. Kilépés")
        valasztas = input("Válasszon egy opciót: ")

        if valasztas == "1":
            legi_tarsasag.list_jaratok()
        elif valasztas == "2":
            nev = input("Adja meg a nevét: ")
            jaratszam = input("Adja meg a járatszámot: ")
            for jarat in legi_tarsasag.jaratok:
                if jarat.jaratszam == jaratszam:
                    foglalasok.foglalas_hozzaadasa(jarat, nev)
                    break
            else:
                print("Nem található ilyen járat.")
        elif valasztas == "3":
            nev = input("Adja meg a nevét: ")
            jaratszam = input("Adja meg a járatszámot: ")
            foglalasok.foglalas_lemondasa(jaratszam, nev)
        elif valasztas == "4":
            foglalasok.list_foglalasok()
        elif valasztas == "5":
            break
        else:
            print("Érvénytelen opció.")


if __name__ == "__main__":
    main()
