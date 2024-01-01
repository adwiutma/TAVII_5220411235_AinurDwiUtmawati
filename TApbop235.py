# Class Induk
class Kuliner:
    def __init__(self, nama, harga):
        self.__nama = nama  # private attribute
        self.__harga = harga  # private attribute

    # public method
    def tampilkan_menu(self):
        print(f"{self.__nama} - Rp {self.__harga}")

    # overriding method
    def deskripsi(self):
        print(f"Ini adalah menu {self.__nama}")

    # overloading method
    def hitung_total(self, jumlah_pesanan=1):
        return self.__harga * jumlah_pesanan


# Class Anak Pertama
class Makanan(Kuliner):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)  # inheritance
        self.__jenis = jenis  # private attribute

    # overriding method
    def deskripsi(self):
        print(f"Ini adalah makanan {self._Kuliner__nama} ({self.__jenis})")

    # public method
    def promo_makanan(self):
        print("Promo spesial: Gratis minuman untuk setiap pembelian makanan!")


# Class Anak Kedua
class Minuman(Kuliner):  # inheritance
    def __init__(self, nama, harga, jenis, ukuran):
        super().__init__(nama, harga)  # inheritance
        self.__jenis = jenis  # private attribute
        self.__ukuran = ukuran  # private attribute

    # overriding method
    def deskripsi(self):
        print(f"Ini adalah minuman {self._Kuliner__nama} ({self.__jenis}), ukuran: {self.__ukuran}")

    # public method
    def promo_minuman(self):
        print("Promo minuman: Diskon 20% untuk pembelian 2 minuman atau lebih!")

class MinumanSpesial(Minuman):
    def __init__(self, nama, harga, jenis, ukuran, tambahan):
        super().__init__(nama, harga, jenis, ukuran)  # inheritance
        self.__tambahan = tambahan  # private attribute

    # overriding method
    def deskripsi(self):
        print(f"Ini adalah minuman spesial di kedai ini {self._Kuliner__nama} ({self._Minuman__jenis}), ukuran: {self._Minuman__ukuran}")
        print(f"Tambahan spesial: {self.__tambahan}")

    # public method
    def promo_minuman(self):
        print("Promo minuman spesial: Dapatkan potongan harga khusus untuk minuman spesial ini!")

def pesan_menu(menu, jumlah_pesanan):
    total_harga = menu.hitung_total(jumlah_pesanan)
    print(f"Terima kasih telah memesan {jumlah_pesanan} {menu._Kuliner__nama}. Total harga: Rp {total_harga}")
    return total_harga


def main():
    # Objek dari class Menu
    menu1 = Kuliner("Spaghetti Carbonara", 55000)
    menu1.tampilkan_menu()
    pesanan_menu1 = pesan_menu(menu1, 3)

    print("\n")

    # Objek dari class Makanan
    makanan1 = Makanan("Sop Iga", 35000, "Pedas")
    makanan1.tampilkan_menu()
    pesanan_makanan1 = pesan_menu(makanan1, 2)

    print("\n")

    # Objek dari class Minuman
    minuman1 = Minuman("Ice Tea", 10000, "Manis", "Large")
    minuman1.tampilkan_menu()
    pesanan_minuman1 = pesan_menu(minuman1, 4)
    
    # Objek dari class MinumanSpesial
    minuman_special1 = MinumanSpesial("Green Thai Tea", 15000, "Ice", "Large", "Jelly")
    minuman_special1.tampilkan_menu()
    pesanan_minuman_special1 = pesan_menu(minuman_special1, 1)

    # Menjumlahkan pesanan dan total harga
    total_pesanan = pesanan_menu1 + pesanan_makanan1 + pesanan_minuman1 + pesanan_minuman_special1
    print(f"\nTotal pesanan untuk semua menu: {total_pesanan}")

main()
