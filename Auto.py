class Auto:

    def __init__(self, ev, nev, ossz):
        self.ev= int(ev)
        self.nev= str(nev)
        self.ossz= int(ossz)


    def __str__(self):
        print(f"Kor: {self.ev}, elnevezés: {self.nev}, összesen: {self.ossz}.")
