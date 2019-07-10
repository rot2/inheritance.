class Hayvan():
	def __init__(self,nefes = ("Nefes verili"),yemekye = ("Yemek yemiyor."),suiç = ("Su içmiyor.")):
		self.nefes = nefes

		self.yemekye = yemekye

		self.suiç = suiç


	def nefesal(self):
		print("Nefes alınıyor...")
		self.nefes = ("Nefes alıyor.")

	def nefesver(self):
		print("Nefes verildi...")
		self.nefes = ("Nefes verili.")

	def yemekye(self):
		print("Yemek yeniyor.")
		self.yemekye = "Yemek Yiyor."

class Kediler(Hayvan):

	def __init__(self,miyavla = "Miyavlamıyor.",nefes = "Nefes verildi",yemekye = "Yemek yemiyor",suiç = "Su içmiyor"):
		self.miyavla = miyavla

		self.nefes = nefes

		self.yemekye = yemekye

		self.suiç = suiç
	def miyav(self):
		print("Miyavlıyor...")
		self.miyavla = "Miyav"

	def sus(self):
		print("Sustu..")
		self.miyavla = "Miyavlamıyor."

	def __str__(self):
		return("\nHayvan durumu: {}\nSes: {}\nAçlık: {}\nSusuzluk: {}".format(self.nefes,self.miyavla,self.yemekye,self.suiç))

class Kuş(Hayvan):
		
	def __init__(self,öt = "Ötmüyor.",nefes = "Nefes almıyor",yemekye = "Yemek yemiyor",suiç = "Su içmiyor"):
		self.öt = öt

		self.nefes = nefes

		self.yemekye = yemekye

		self.suiç = suiç

	def ötsün(self):
		print("Cikcikcik!")
		self.öt = "Ötüyor..."

	def ötme(self):
		print("...sustu")
		self.öt = "Suskun"

	def __str__(self):
		return("\nHayvan durumu: {}\nSes: {}\nAçlık: {}\nSusuzluk: {}\n".format(self.nefes,self.öt,self.yemekye,self.suiç))


kedi = Kediler()
kuş = Kuş()

print("""
1-KEDİ
2-KUŞ
3-AT
Çıkmak için 'q'
""")


secenek = input("Secenek:")
while True:
	if secenek == "q":
		print("Programdan çıkılıyor.")
		break
	if secenek == "1":

		cevap = input("İşlem:")
		if cevap == "q":
			break
		if cevap == "1":
			kedi.nefesal()
		elif cevap == "2":
			kedi.nefesver()
		elif cevap == "3":
			kedi.miyav()
		elif cevap == "4":
			kedi.sus()
		elif cevap == "5":
			print(kedi)
		else:
			print("Geçersiz işlem..")


	elif secenek == "2":

		k = input("İşlem:")
		if k == "q":
			print("Çıkış yapılıyor.")
			break
		if k == "1":
			kuş.nefesal()
		elif k == "2":
			kuş.nefesver()
		elif k == "3":
			kuş.ötsün()
		elif k == "4":
			kuş.ötme()
		elif k == "5":
			print(kuş)
		else:
			print("Geçersiz işlem..")

