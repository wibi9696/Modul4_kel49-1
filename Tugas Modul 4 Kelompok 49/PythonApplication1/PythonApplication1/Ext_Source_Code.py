class main:
    def __init__ (self, nama, email, HP):
        self.nama=nama
        self.email=email
        self.HP=HP
        self.logam=["Emas","Logam"]
        self.harga=[732600,216044]

    def welcome (self):
        print(f"Selamat datang, {self.nama} ! Selamat bertransaksi di Mesin Toko Emas Otomatis Kelompok 49!")
        print("Mesin ini akan melakukan bunga harga sebagai berikut:")
        print("Penjualan\t:5%")
        print("Pembelian\t:10%")

    def pembelian_fitur(self):
        print("Masukkan jenis logam yang ingin anda beli")
        count=1
        for x in self.logam :
            print (count,".",x)
            count=count+1
