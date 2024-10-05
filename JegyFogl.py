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
