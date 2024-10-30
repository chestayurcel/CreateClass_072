# Membuat kelas PersegiPanjang
class PersegiPanjang:
    def __init__(self, panjang, lebar): # Konstruktor untuk menginisialisasi
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self): # Metode menghitung keliling
        return 2 * (self.panjang + self.lebar)
    
    def luas(self): # Metode menghitung luas
        return self.panjang * self.lebar
    
    def __str__(self): # Metode untuk string
        return f"Persegi Panjang dengan Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"
    
pp = PersegiPanjang(8, 5)
print(pp.__str__())
print("Kelilingnya adalah = ", pp.keliling(), "cm") 
print("Luasnya adalah = ", pp.luas(), "cm")