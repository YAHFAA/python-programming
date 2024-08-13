umur = int (input("masukan umur anda:"))

if umur < 13: 
    print("Andamasih anak anak")
elif umur >= 13 and umur < 18:
    print("Anda remaja")
elif umur >= 18 and umur < 60:
    print("anda dewasa")
else:
    print("andasudah tua")