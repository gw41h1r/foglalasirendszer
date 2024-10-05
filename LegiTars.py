class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

    def list_jaratok(self):
        for jarat in self.jaratok:
            print(jarat.get_info())
