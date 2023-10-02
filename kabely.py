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
		for i in range(len(self.zadani)):
			ajajaj = False
			h, w, n = self.zadani[i]
			podlaha = [[False] * (w + 1) for i in range(h + 1)]

			# Nacteni zarizeni do pole
			for nazev_zarizeni in self.zarizeni[i].keys():
				for [y, x] in self.zarizeni[i][nazev_zarizeni]:
					podlaha[y][x] = nazev_zarizeni

			for nazev_zarizeni in self.zarizeni[i].keys():
				if len(self.zarizeni[i][nazev_zarizeni]) < 2:
					ajajaj = True
					continue
				elif len(self.zarizeni[i][nazev_zarizeni]) > 2:
					raise Exception("Zarizeni je tu mockrat - " + nazev_zarizeni + ", Cyklus - " + str(i + 1))

				c1, c2 = self.zarizeni[i][nazev_zarizeni]
				if not self.jeOkrajVolny(podlaha, c1, c2):
					ajajaj = True
					break

			# for p in podlaha:
			# 	print(p)

			if ajajaj:
				self.odpovedi.append("ajajaj")
			else:
				self.odpovedi.append("pujde to")

		# Vypise odpovedi
		for odpoved in self.odpovedi:
			print(odpoved)

	def jeOkrajVolny(self, pole, sour1, sour2):
		max_delka = len(pole)
		max_sirka = len(pole[0])

		lze_projit = False
		druhy_smer = False
		for cyklus in range(2):
			poz_x, poz_y = sour1
			zmena_x, zmena_y = 0, 0

			if poz_x <= 0:
				zmena_y = -1 if druhy_smer else 1
			elif poz_x >= max_delka - 1:
				zmena_y = 1 if druhy_smer else -1
			elif poz_y <= 0:
				zmena_x = 1 if druhy_smer else -1
			elif poz_y >= max_sirka - 1:
				zmena_x = -1 if druhy_smer else 1

			koliduje = []
			je_dvakrat = []  # Zařízení které jsou mezi hledanými zařízeními dvakrát
			for q in range(2 * (max_sirka + max_delka)):
				if [poz_x, poz_y] == sour2:
					lze_projit = True
					break

				if pole[poz_x][poz_y] is not False and pole[poz_x][poz_y] != pole[sour1[0]][sour1[1]]:
					# Když jsou v trase dva stejne lze je obejit
					if pole[poz_x][poz_y] in koliduje:
						koliduje.remove(pole[poz_x][poz_y])
						je_dvakrat.append(pole[poz_x][poz_y])
					else:
						koliduje.append(pole[poz_x][poz_y])

				if poz_x in [0, max_delka - 1] and poz_y in [0, max_sirka - 1]:
					zmena_x = 0
					zmena_y = 0

				if poz_x <= 0 and poz_y <= 0:
					if not druhy_smer:
						zmena_y = 1
					else:
						zmena_x = 1

				if poz_x <= 0 and poz_y >= max_sirka - 1:
					if not druhy_smer:
						zmena_x = 1
					else:
						zmena_y = -1

				if poz_x >= max_delka - 1 and poz_y >= max_sirka - 1:
					if not druhy_smer:
						zmena_y = -1
					else:
						zmena_x = -1

				if poz_x >= max_delka - 1 and poz_y <= 0:
					if not druhy_smer:
						zmena_x = -1
					else:
						zmena_y = 1

				poz_x += zmena_x
				poz_y += zmena_y

			if lze_projit and len(koliduje) > 0:
				lze_projit = False

			if lze_projit:
				break
			elif not druhy_smer:
				druhy_smer = True

		return lze_projit

	def nactiZeVstupu(self):
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

		# Načtení dat do polí
		self.zadani = []
		self.zarizeni = []
		for i in range(pocet_zadani):
			self.zadani.append([int(inpt) for inpt in soubor.readline().rstrip('\n').split(" ")])
			zarizeni_informace = {}
			for i2 in range(self.zadani[-1][2]):
				y, x, c = soubor.readline().rstrip('\n').split(" ")

				if c not in zarizeni_informace.keys():
					zarizeni_informace[c] = []

				zarizeni_informace[c].append([int(y), int(x)])
			self.zarizeni.append(zarizeni_informace)

		soubor.close()


Kabely(False)
