from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def get_info(self):
        return f"Belföldi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar} Ft"
