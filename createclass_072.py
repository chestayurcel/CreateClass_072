class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi Panjang dengan Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"
    
def main():
    try:
        panjang = float(input("Masukkan panjangnya : "))
        lebar = float(input("Masukkan lebarnya : "))
        if panjang <= 0 or lebar <= 0:
            print ("Nilai harus positif")
            return
        pp = PersegiPanjang(panjang, lebar)
        print (pp.keliling())
        print (pp.luas())
    except ValueError:
        print("Nilai harus sesuai")
main()