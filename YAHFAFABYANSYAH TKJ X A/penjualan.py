def  hitung_harga(usia_jumlah_tiket) :
    if "usia" < 12:
        harga = 30000 # harga
     "tiket_anak_anak"
    elif "usia" <= 60:
        harga = 50000 # harga 
        "tiket_dewasa"
    else:
        harga = 35000 # harga
        "tiket lansia"

        total_harga = harga * usia_jumlah_tiket
        return total_harga

        #memproses beberapa pembeli tiket
        jumlah_pembeli =
        int(input("masukan jumlah_pembeli:")) 

        for i in range(jumlah_pembeli):
            print(f"\npembeli {i + i}:")
            usia = int(input("masukan usia pembeli: "))
            # hitung total harga tiket 
            total = hitung_harga(usia,jumlah_tiket)
            print(f"total harga untuk pembeli { 1 + 1 }: Rp: (total")