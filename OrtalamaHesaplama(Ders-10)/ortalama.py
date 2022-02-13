#Bir text dosyasından öğrencilerin notlarını çağırıp ortalamasını hesaplayan ve bu ortalamayı başka bir dosyaya yazdıran python programı


def not_hesaplama(satır):

    satır = satır[:-1]


    #virgüle kadar olan her bir elemanı listenin yeni bir elemanı olarak tanımlayalım
    liste = satır.split(",")
    #print(liste)


    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])


    ortalama = not1*0.3+not2*0.3+not3*0.4

    if ortalama >= 90:
        harf = "AA"

    #görüntülemek için
    #print(f"{ortalama}" )

    #verileri başka bir fonkksiyonda kullanmak için return parametresini unutmayalım...!
    return isim + "---" + "Not Ortalaması: " + str(ortalama) + "\n" 




with open("notlar.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesaplama(i))

with open("ortalamalar.txt", "w", encoding="utf-8") as file2:
    for i in eklenecekler_listesi:
        file2.write(str(i))