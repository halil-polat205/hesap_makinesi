p = input("parola : ")

if p != "hesap":
	print("hatalı parola giriniz...")
	quit()

else :
    print("""
 ----------------------**0**--------------------
 Programı Yazan     :       HALİL POLAT        -
                                              -
 Yazıldığı Dil      :       PYTHON 3           -
                                              -
 ---------------------**0**---------------------

 """)
	
def topla(a,b):
	print("sonuç : ",a+b)

def cıkar(a,b):
	print("sonuc : ",a-b)

def us_al(a,b):
	print("sonuc : ",a**b)

def bol(a,b):
	print("sonuc : ",a/b)

def carp(a,b):
	print("sonuc : ",a*b)



print("""
(1)toplama
(2)cıkarma
(3)us_alma
(4)bolme
(5)karekök
(6)küpkök
(7)daire_alanı
(8)daire_cevresi
(9)yoğunluk_hesaplama
(10)ısı_hesaplama
(11)carpma
(C)cıkıs
""")

import time


while True:
	islem=input("islem numarasnı giriniz : ")

	if islem == "1" :
		x = input("ilk sayı : ")
		x = float(x)
		y = input("ikinci sayı : ")
		y = float(y)
		topla(x,y)
		continue

	elif islem == "2":
		x = input("büyük sayı :")
		x = float(x)
		y = input("küçük sayı : ")
		y = float(y)
		cıkar(x,y)
		continue

	elif islem ==	"3":
		x = input("taban : ")
		y = input("üs : ")
		x = float(x)
		y = int(y)
		us_al(x,y)
		continue

	elif islem =="4":
		x = input("bolunen : ")
		y = input("bolen : ")

		x = float(x)
		y = float(y)
		bol(x,y)
		continue

	elif islem =="5" :
		x = input("neyin karekoku : ")
		x = int(x)
		us_al(x,1/2)
		continue

	elif islem =="6":
		x = input("neyin küpkökü : ")
		x = int(x)
		us_al(x,1/3)
		continue

	elif islem =="7" :
		pi = 3.14
		r = input("yarıcap : ")
		r = float(r)
		carp(pi,r**2)
		continue

	elif islem =="8" :
		pi = 3.14
		r = input("yarıcap : ")
		r = float(r)
		carp(2,pi*r)

	elif islem =="9" :
		m = input("cismin kütlesi (gr) : ")
		V = input("cismin hacmi (cm3) : ")
		m = float(m)
		V = float(V)
		bol(m,V)

	elif islem =="10" :
		m = input("kütle(gr) : ")
		c = input("özısı(Cal/gr*C) : ")
		Δt = input("Sıcaklık farkı(*C) : ")
		m = float(m)
		c = float(c)
		Δt = float(Δt)
		carp(m,c*Δt)

	elif islem =="11" :
		x = input("ilk sayı : ")
		y = input("ikinci sayı : ")
		x = float(x)
		y = float(y)
		carp(x,y)

	elif islem == "C" or islem =="c" :
		print("bizi tercih ettiğiniz için tesekkur ederiz")
		print("cıkılıyor...")
		time.sleep(3)
		quit()
	else :
	  print("hatalı girdiniz")
	  quit()   

