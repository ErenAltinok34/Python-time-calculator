#girdi:saniye tutari
#cikti gun saat dakika saniye
#ornek 134 saniye
#2 dakika 14 saniye
#5486 saniye
#1 saat 31 dakika 26 saniye
def zaman(sure):
    if (sure < 60):
        sani = sure
        print(sani, "saniye")

    elif (sure < 3600):
        daki = int(sure / 60)
        sani = sure - daki * 60
        print(daki, "dakika", sani, "saniye")

    elif (sure < 86400):
        saat = int(sure / 3600)
        daki = int((sure - saat * 3600) / 60)
        sani = sure - saat * 3600 - daki * 60
        print(saat, "saat", daki, "dakika", sani, "saniye")



sure = int(input("Saniye gir: "))
zaman(sure)