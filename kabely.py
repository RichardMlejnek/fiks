"""def kdeJeHodnota(seno, jehla, existuje):
	ret = False

	for a in range(len(seno)):
		for b in range(len(seno[a])):
			if seno[a][b] == jehla and a != existuje[0] and b != existuje[1]:
				ret = [a, b]

	return ret"""


class Kabely:
	def __init__(self, nacti_ze_vstupu):
		self.zadani = []
		self.zarizeni = []

		if nacti_ze_vstupu:
			self.nactiZeVstupu()
		else:
			self.nactiZeSouboru("TODO")  # TODO

		# print(zadani)
		# print(zarizeni)
	def jeOkrajVolny(self, pole, sour1, sour2):
		max_delka = len(pole)
		max_sirka = len(pole[0])

		lze_projit = False
		druhy_smer = False
		for cyklus in range(2):
			poz_x, poz_y = sour1
			zmena_x, zmena_y = 0, 0
			koeficient = 0

			if poz_x <= 0:
				zmena_y = 1
			elif poz_x >= max_delka:
				zmena_y = -1
			elif poz_y <= 0:
				zmena_x = -1
				koeficient = -1
			elif poz_y >= max_sirka:
				zmena_x = 1
				koeficient = -1

			koliduje = []
			je_dvakrat = []  # Zařízení které jsou mezi hledanými zařízeními dvakrát
			for q in range(2 * (max_sirka + max_delka)):
				if [poz_x, poz_y] == sour2:
					lze_projit = True
					break

				if pole[poz_x][poz_y] is not False and pole[poz_x][poz_y] != pole[sour2[0]][sour2[1]]:
					# Když jsou v trase dva stejne lze je obejit TODO
					if pole[poz_x][poz_y] in koliduje:
						koliduje.remove(pole[poz_x][poz_y])
						je_dvakrat.append(pole[poz_x][poz_y])
					else:
						koliduje.append(pole[poz_x][poz_y])

				if poz_x <= 0 and poz_y <= 0:
					zmena_x = 0
					zmena_y = 1
					koeficient = 0

				if poz_x <= 0 and poz_y >= max_sirka - 1:
					zmena_x = 1
					zmena_y = 0
					koeficient = -1

				if poz_x >= max_delka - 1 and poz_y >= max_sirka - 1:
					zmena_x = 0
					zmena_y = -1
					koeficient = 0

				if poz_x >= max_delka - 1 and poz_y <= 0:
					zmena_x = -1
					zmena_y = 0
					koeficient = -1

				# Prohozeni smeru a pridani koeficientu
				if druhy_smer:
					poz_x += zmena_y * koeficient
					poz_y += zmena_x * koeficient
				else:
					poz_x += zmena_x
					poz_y += zmena_y

			if lze_projit and len(koliduje) > 0:
				lze_projit = False

			if lze_projit:
				break
			else:
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

	def nactiZeSouboru(self, soubor):
		pass


odpovedi = []
for i in range(len(zadani)):
	ajajaj = False
	h, w, n = zadani[i]
	podlaha = [[False] * (w + 1) for i in range(h + 1)]

	# Nacteni zarizeni do pole
	for nazev_zarizeni in zarizeni[i].keys():
		for [y, x] in zarizeni[i][nazev_zarizeni]:
			podlaha[y][x] = nazev_zarizeni

	for nazev_zarizeni in zarizeni[i].keys():
		if len(zarizeni[i][nazev_zarizeni]) < 2:
			ajajaj = True
			continue
		elif len(zarizeni[i][nazev_zarizeni]) > 2:
			raise "Zarizeni je tu mockrat - " + nazev_zarizeni + ", Cyklus - " + i

		c1, c2 = zarizeni[i][nazev_zarizeni]
		jeOkrajVolny(podlaha, c1, c2)




	# Projde pole od levého horního rohu a najde k zařízením jejich dvojici a cestu
	"""radek = 0
	sloupec = 0
	ajajaj = False
	prvni_policko = True
	for velikost in range(max(h, w) + 1):
		for zvetsit in [[0, 1], [1, 0]]:
			if velikost * zvetsit[0] < h + 1:
				radek = velikost * zvetsit[0]
			if velikost * zvetsit[1] < w + 1:
				sloupec = velikost * zvetsit[1]

			# Odfiltrovat souradnice [0,0]
			if radek <= 0 and sloupec <= 0 and not prvni_policko:
				continue
			prvni_policko = False

			# Co se na policku nachazi
			hodnota = pole[radek][sloupec]
			if hodnota is False or hodnota is True:
				continue

			# Zjistit jsetli a kde je druha hodnota
			pozice = kdeJeHodnota(pole, hodnota, [radek, sloupec])
			if not pozice:
				# Pokud neni druha hodnota, nelze ulohu splnit
				ajajaj = True
				continue

			print(radek, sloupec)

			konec = False
			for krok in range(max(pozice[0], radek) - min(pozice[0], radek)):
				if pole[radek + krok][sloupec] == hodnota:
					konec = True
					break
				elif pole[radek + krok][sloupec] is True:
					print("error")
					ajajaj = True
					konec = True
				pole[radek + krok][sloupec] = True

			if konec:
				continue

			for krok in range(max(pozice[1], sloupec) - min(pozice[1], sloupec)):
				if pole[radek][sloupec + krok] == hodnota:
					konec = True
					break
				elif pole[radek][sloupec + krok] is True:
					print("error")
					ajajaj = True
					konec = True
				pole[radek][sloupec + krok] = True

		if ajajaj:
			continue"""

	for p in podlaha:
		print(p)

	if ajajaj:
		odpovedi.append("ajajaj")
	else:
		odpovedi.append("pujde to")

for odpoved in odpovedi:
	print(odpoved)
