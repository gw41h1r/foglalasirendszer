from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def get_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar} Ft"
