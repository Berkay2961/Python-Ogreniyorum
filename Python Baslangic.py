print("Merhaba Python")
print("Ad:Berkay")
print("Soyad:Sahin")
print("Yas:20")
print("Meslek:Ogrenci")
#ekrana yazdirma diger yol
print("Ad:Berkay,Soyad:Sahin,Yas:20,Meslek:Ogrenci")
print("elma","armut","seftali","kiraz",sep="\n",end="...")

#degisken tanimlama ve ekrana yazdirma

yas=20
boy=1.85
kilogram=90
print("\nYas✔",yas)
print("Boy✔",boy)
print("Kilogram✔",kilogram)


#iki sayi tanimla ve dort islem metni yazdir
sayi1= 18
sayi2 = 22

toplam=sayi1+sayi2
fark=sayi1-sayi2
carpim=sayi1*sayi2
bolum=sayi1/sayi2

print("Toplam",toplam)
print("Fark",fark)
print("Carpim",carpim)
print("Bolum",bolum)

#kullanicidan yas bilgisini alip 5 yil sonraki yasini yazdirma
yas= int(input("Yasinizi girin:"))
gelecekYas= yas+5
print("5 yil sonraki yasiniz:", gelecekYas)


#type fonksiyonuyla farklı veri türlerini yazdırma(bir değişkenin veri türünü öğrenmek için kullanılır)

sayi1 = 10
sayi2 = 3.14
print(type(sayi1))  # int
print(type(sayi2))  # float
metin = "Merhaba"
print(type(metin))  # str
liste = [1, 2, 3]
print(type(liste))  # list
demet = (1, 2, 3)   
print(type(demet))  # tuple
set_veri = {1, 2, 3}
print(type(set_veri))  # set
sozluk = {"ad": "Ahmet", "yas": 30}
print(type(sozluk))  # dict

#tip dönüşüm hataları
sayi =int(12,5)  # Hata: int() fonksiyonu sadece tam sayıları alır, ondalıklı sayıları kabul etmez.
# sayi = int("Merhaba")  # Hata: "Merhaba" metni tam sayıya dönüştürülemez.
# sayi = float("123abc")  # Hata: "123abc" metni float'a dönüştürülemez.
sayi = int((float(12.5)))  # Doğru: float'ı önce int'e dönüştürür.

sayi=int([1, 2, 3])  # Hata: Liste doğrudan int'e dönüştürülemez.

sayi = int({"ad": "Ali"})  # Hata: Sözlük doğrudan int'e dönüştürülemez.

#Girilen yaşa göre reşit olup olmadığını kontrol etme
yas=int(input("Yasinizi girin: "))
if yas>=18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")  

#Kullanıcıdan alınan nota göre geçti veya kaldı bilgisini yazdırma
notu = int(input("Notunuzu girin: "))
if notu >= 50:
    print("Geçtiniz.")
else:
    print("Kaldınız.")

    #Basit bir sayı tahmin oyunu(sabit sayı ile karşılaştırma)

    sabit_sayi = 7
tahmin = int(input("Bir sayı tahmin edin (1-10): "))
if tahmin == sabit_sayi:
    print("Tebrikler! Doğru tahmin ettiniz.")
elif tahmin < sabit_sayi:
    print("Tahmininiz çok düşük. Daha yüksek bir sayı deneyin.")
else:
    print("Tahmininiz çok yüksek. Daha düşük bir sayı deneyin.")

    #üç sayıdan en büyüğünü bulma
sayi1 = int(input("Birinci sayiyi girin: "))
sayi2 = int(input("İkinci ssayiyi girin: "))
sayi3 = int(input("Üçüncü sayiyi girin: "))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    print("En büyük sayı:", sayi1)
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print("En büyük sayı:", sayi2)
else:
    print("En büyük sayı:", sayi3)

    #sayının pozitif, negatif veya sıfır olduğunu yazdıran kod
    sayi=int(input("Sayiyi girin:  "))
    if sayi>0:
        print("Sayi pozitif.")
    elif sayi<0:
        print("Sayi negatif.")
    else:
        print("Sayi sifir.")

        #1 den 100 e kadar olan tek sayıları yazdırma
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")

        #kullancıdan 5 sayı alıp bu sayıların  ortalamasını hesaplama
sayi_listesi = []
for i in range(5):
    sayi = float(input(f"{i + 1}. sayiyi girin: "))
    sayi_listesi.append(sayi)
ortalama = sum(sayi_listesi) / len(sayi_listesi)
print("Girilen sayilarin ortalamasi:", ortalama)

#1 den 10 a kadar çarpım tablosunu yazdır
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
    # 100 e kadar olan sayıların toplamını hesaplama
toplam = 0
for i in range(1, 101):
    toplam += i 
print(" 100'e kadar olan sayıların toplamı:", toplam)

# kullanıcının girdiği sayıya kadar olan çift sayıları listeleme
sayi = int(input("Bir sayi girin: "))
cift_sayilar = []
for i in range(2, sayi + 1, 2):
    cift_sayilar.append(i)
print("Girilen sayıya kadar olan çift sayılar:", cift_sayilar)










