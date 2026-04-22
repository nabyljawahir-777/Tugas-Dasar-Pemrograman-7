text = "mang kasir aplikasi sederhana"
jumlahKarakter = 0
jumlahKata = 0
for char in text:
    jumlahKarakter += 1
    if char == " ":
        jumlahKarakter -= 1
        jumlahKata += 1
print("Jumlah karakter:", jumlahKarakter)
print("Jumlah kata:", jumlahKata + 1)