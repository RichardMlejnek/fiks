"""def kdeJeHodnota(seno, jehla, existuje):
	ret = False

	for a in range(len(seno)):
		for b in range(len(seno[a])):
			if seno[a][b] == jehla and a != existuje[0] and b != existuje[1]:
				ret = [a, b]

	return ret"""


pocet_zadani = int(input())

# Načtení dat do polí
zadani = []
zarizeni = []
for i in range(pocet_zadani):
	zadani.append([int(inpt) for inpt in input().split(" ")])
	zarizeni_informace = {}
	for i2 in range(zadani[-1][2]):
		y, x, c = input().split(" ")
		if c not in zarizeni_informace.keys():
			zarizeni_informace[c] = []
		zarizeni_informace[c].append([int(y), int(x)])
	zarizeni.append(zarizeni_informace)

# print(zadani)
# print(zarizeni)

odpovedi = []
for i in range(len(zadani)):
	h, w, n = zadani[i]
	podlaha = [[False] * (w + 1) for i in range(h + 1)]

	# Nacteni zarizeni do pole
	for c in zarizeni[i].keys():
		y, x = zarizeni[c]
		podlaha[y][x] = c

	for c in zarizeni[i].keys():
		y, x = zarizeni[c]
		

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
