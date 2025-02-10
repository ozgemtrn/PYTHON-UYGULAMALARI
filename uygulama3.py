""" pyhon veri tipleri ->numeric(int,float),text(str),boolean(bool)"""

isim="cınar"
yas=7
kilo=15.1
ogrencimi=True

print(type(isim))
print(type(yas))
print(type(kilo))
print(type(ogrencimi))
# farklı turdekı degıskenlerı aynı anda ekrana yazdırmaya calılısınca type error alırız bunun gıbı
#print(isim+yas)
#bunun ıcın

print(isim+str(yas))

""" eger ınput la deger alırsak bu bıze strıng turunde gelır"""

sayi1=input("sayı1 gırın:")
sayi2=input("sayı2 grın:")

toplam=sayi1+sayi2
print(toplam)

#suan ıkı str verıyı yan yana yazddırdı bunun olmaması ıcın

sayi3=int(input("sayı3 gırın:"))
sayi4=int(input("sayı4 grın:"))

toplam1=sayi3+sayi4
print(toplam1)
#float degerlerı strıng sekılde de ınt e gonderılırse hata alırız
x=int("10.5")

#float degerlerı float sekılde de ınt e gonderılırse hata alırız
x=int(10.5)
print(x)
#bu sekılde de float kısmını atar ve 10 olarak yazar