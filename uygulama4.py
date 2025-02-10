"""uygulama 1: yarıcapı verılen bır daırenın alan ve cevresını hesaplayınız
alan:pi*r^2
cevre:2*pi*r
uygulama 2:klavyeden gırılen km bılgısını mil çınsınden hesaplayınız
mil=km/1.609344
"""
pi=3.14
r=float(input("yarı capı:"))
alan=pi*(r**2)
cevre=2*pi*r
print("alan:"+str(alan))
print("cevre:"+str(cevre))


mesafekm=input("km:")
mesafemil=float(mesafekm)/1.609344
mesafemil=round(mesafemil,2)
print(mesafekm+"km="+str(mesafemil)+"mil")