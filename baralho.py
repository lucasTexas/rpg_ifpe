baralho = input("Digite as cartas prontas para serem embaladas: ")

copas = ["01C", "02C", "03C", "04C", "05C", "06C", "07C", "08C", "09C", "10C", "11C", "12C", "13C"]
espadas = ["01E", "02E", "03E", "04E", "05E", "06E", "07E", "08E", "09E", "10E", "11E", "12E", "13E"]
ouros = ["01U", "02U", "03U", "04U", "05U", "06U", "07U", "08U", "09U", "10U", "11U", "12U", "13U"]
paus = ["01P", "02P", "03P", "04P", "05P", "06P", "07P", "08P", "09P", "10P", "11P", "12P", "13P"]

contador_copas = 13
contador_espadas = 13
contador_ouros = 13
contador_paus = 13

if len(baralho) == 156:
	print(0)
	print(0)
	print(0)
	print(0)
else:
	for i in copas:
		if baralho.__contains__(i):
			contador_copas -= 1
	for i in espadas:
		if baralho.__contains__(i):
			contador_espadas -= 1
	for i in ouros:
		if baralho.__contains__(i):
			contador_ouros -= 1
	for i in paus:
		if baralho.__contains__(i):
			contador_paus -= 1
	print(contador_copas)
	print(contador_espadas)
	print(contador_ouros)
	print(contador_paus)