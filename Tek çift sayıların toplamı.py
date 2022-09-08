sayı1 = 0
toplam_Cift = 0
toplam_Tek = 0
while (sayı1< 1000):
    sayı1 = sayı1 +1
    if(sayı1%2==0):
        toplam_Cift+=sayı1

    else:
        toplam_Tek+=sayı1

    print(f"toplam çift sayı: ",toplam_Cift)
    print(f"Toplam Tek sayı: ", toplam_Tek)
