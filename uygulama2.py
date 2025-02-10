#degıskne tanımlama kuralları
#degıskne ısımlerı sayı ıle baslamaz,degıskeenler ıcınde "_" harıcınde dıgerlerı kullanılamaz
#geleneksel olarak camelcase kullanılır
#buyuk kucuk harf duyarlılıgı vardır
#komut ısımlerı kullnılmamalı mesela print
sayı2=49

yas=40
Yas=40
#farklı bellek adreslerı kullanılır


x="101"
y="20"

print(x+y)#bırlestırılme yapılır toplama ıcın tur donusumu yapılmalı


x,y,z=30,40,50

x,y,z=80


"""
aş. musterının bılgılerını ve satın aldıgı urun bılgılerını degıskenler ıcerısınde saklayınız
toplam odenen ucret nedır?
odenen mıktarın kdv oranı nedır?(%18)

ozge turan
05367892837821
jljdskl@gmaıl.com
turkey

urun adı=mouse
fıyat=550
urun adı=klavye
fıyat=650
urun adı=pc
fıyat=55000
"""

musteri_adi="ozge"
musteri_soyad="turan"
musteri_tel="05367892837821"
musteri_mail="jljdskl@gmaıl.com"
musteri_ulke="turkey"

urunadi="mouse"
fiyat=550
urunadi="klavye"
fiyat2=650
urunadi="pc"
fiyat3=55000

toplam=fiyat+fiyat2+fiyat3
print(toplam)
kdvlitoplam=toplam+(fiyat*0.18+fiyat2*0.18+fiyat3*0.18)
print(kdvlitoplam)