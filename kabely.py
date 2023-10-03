class Kabely:
	def __init__(self, nacti_ze_vstupu):
		self.zadani = []
		self.zarizeni = []

		if nacti_ze_vstupu:
			self.nactiZeVstupu()
		else:
			self.nactiZeSouboru("C:/Users/Riky/Downloads/input.txt")

		# print(zadani)
		# print(zarizeni)

		self.odpovedi = []
		for cyklus in range(len(self.zadani)):
			aktualni_zarizeni = self.zarizeni[cyklus]

			konec = False
			if len(aktualni_zarizeni) % 2:
				konec = True

			while len(aktualni_zarizeni) > 0 and not konec:
				konec = True
				for i in range(len(aktualni_zarizeni)):
					if i + 1 < len(aktualni_zarizeni):
						if aktualni_zarizeni[i] == aktualni_zarizeni[i + 1]:
							aktualni_zarizeni.pop(i + 1)
							aktualni_zarizeni.pop(i)
							konec = False
							break
					else:
						if aktualni_zarizeni[i] == aktualni_zarizeni[0]:
							aktualni_zarizeni.pop(i)
							aktualni_zarizeni.pop(0)
							konec = False
							break

			if konec:
				self.odpovedi.append("ajajaj")
			else:
				self.odpovedi.append("pujde to")

			print(cyklus)
			if cyklus == 13:
				print(14)

		# Vypise odpovedi
		for odpoved in self.odpovedi:
			print(odpoved)

	def nactiZeVstupu(self):
		print("funcion deparced")
		exit()
		pocet_zadani = int(input())

		# Načtení dat do polí
		self.zadani = []
		self.zarizeni = []
		for i in range(pocet_zadani):
			self.zadani.append([int(inpt) for inpt in input().split(" ")])
			zarizeni_informace = {}
			for i2 in range(self.zadani[-1][2]):
				y, x, c = input().split(" ")
				if c not in zarizeni_informace.keys():
					zarizeni_informace[c] = []
				zarizeni_informace[c].append([int(y), int(x)])
			self.zarizeni.append(zarizeni_informace)

	def nactiZeSouboru(self, nazev_souboru):
		soubor = open(nazev_souboru, "r")

		pocet_zadani = int(soubor.readline().rstrip('\n'))

		self.zadani = []
		self.zarizeni = []
		for i in range(pocet_zadani):
			self.zadani.append([int(inpt) for inpt in soubor.readline().rstrip('\n').split(" ")])

			max_delka = self.zadani[-1][1]
			max_sirka = self.zadani[-1][0]

			zarizeni_informace = {}
			for i2 in range(self.zadani[-1][2]):
				y, x, c = soubor.readline().rstrip('\n').split(" ")
				y, x = int(y), int(x)

				# Horní řádek
				if y == 0:
					zarizeni_informace[x] = c

				# Pravý sloupeček
				elif x == max_delka:
					zarizeni_informace[max_delka + y] = c

				# Dolní řádek
				elif y == max_sirka:
					zarizeni_informace[max_sirka + max_delka + max_sirka - x] = c

				# Levý sloupeček
				elif x == 0:
					zarizeni_informace[max_sirka + max_delka + max_sirka + max_delka - y] = c
			self.zarizeni.append(list(dict(sorted(zarizeni_informace.items())).values()))

		soubor.close()


Kabely(False)
