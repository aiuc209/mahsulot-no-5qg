class Mahsulot:
    def __init__(self, nom, stok):
        self.nom = nom
        self.stok = stok

    def yetkazib_berish(self):
        if self.stok < 5:
            return "Tezda yetkazib berish kerak"
        else:
            return "Stok yetarli"

class Doimler:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qoshish(self, nom, stok):
        self.mahsulotlar.append(Mahsulot(nom, stok))

    def mahsulotlar_royxati(self):
        for mahsulot in self.mahsulotlar:
            print(f"Mahsulot: {mahsulot.nom}, Stok: {mahsulot.stok}, {mahsulot.yetkazib_berish()}")

doimler = Doimler()
doimler.mahsulot_qoshish("Apple", 3)
doimler.mahsulot_qoshish("Samsung", 10)
doimler.mahsulotlar_royxati()
