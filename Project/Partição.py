import random


def sum_perf(x_barra,k): # VALOR DE perf(x_barra,k)
	assert k <= len(x_barra) and k>=1
	res = 0
	for i in x_barra:
		res = res + i
	return (res/k)


def blocos_perf(x_barra,part,k,t): # BLOCOS PERFEITOS E INSTANTE t EM QUE FORAM CRIADOS
	blocos_perfeitos = []
	i = 1
	while i <= k:
		res = 0
		for j in range(len(part)): # pois len(particao) == len(x_barra)
			if part[j] == i:
				res = res + x_barra[j]
		if res == sum_perf(x_barra,k):
			blocos_perfeitos = blocos_perfeitos + [[i,t]]
		i = i + 1
	return blocos_perfeitos


def coef_inadp(x_barra,part,k): # COEF DE INADAPTAÇÃO DE UMA PARTICAO ASSOCIADA A UM INDIVIDUO
	res = 0
	for i in range(1,k):
		res1 = 0
		for j in range(len(part)): # pois len(particao) == len(x_barra)
			if part[j] == i:
				res1 = res1 + x_barra[j]
		res = res + abs((res1 - sum_perf(x_barra,k)))
	return res/k


def apaga1(w,k): #APAGA ELEMENTO DE UMA LISTA
    i = 0
    while i < len(w):
        if w[i] == k:
            w = w[:i] + w[i+1:]
            break
        i = i + 1
    return w


def meme(w,k): #APAGA ELEMENTO DE UMA LISTA DE LISTAS
    i = 0
    while i < len(w):
        j = 0
        while j < len(w[i]):
            if w[i][j] == k:
                w[i] = w[i][:j] + w[i][j+1:]
                return w[:i] + [w[i]] + w[i+1:]
            j = j + 1
        i = i + 1
    return "O valor dado como k não é um elemento desta lista"


def dude(w,k): #K-PARTICAO ALEATORIA DE X_BARRA
	res = []
	w_copy = w
	while len(w) > 0 and k > 1:
		n = len(w)
		res1 = []
		z = random.choice(list(range(1,n-k+2)))
		for i in range(z):
			l = random.choice(w)
			res1 = res1 + [l]
			w = apaga1(w,l)
		k = k - 1
		res = res + [res1]
	if k == 1:
		res = res + [w]
	#print(res)
	new = []
	for j in w_copy:
		a = 0
		bol = False
		while a < len(res) and not(bol):
			for b in res[a]:
				if j == b:
					new = new + [a+1]
					res = meme(res,j)
					bol = True
					break
			a = a + 1
	return new

def sum_bloco(part,x_barra,k): #SOMA DOS ELEMENTOS DE UM BLOCO PERTENCENTE A UMA DADA PARTICAO
		res = []
		i = 0
		while i < len(part):
			if k == part[i]:
				res = res + [i]
			i = i + 1
		soma = 0
		for x in res:
			soma = soma + x_barra[x]
		return soma


def indices_bloco_k(x_barra,part,k): #INDICES DOS ELEMENTOS DE X_BARRA QUE PERTENCEM AO BLOCO K
	indices = []
	i = 0
	while i < len(part):
		if part[i] == k:
			indices = indices + [i]
		i = i + 1
	return indices

def blocos_imperfeitos(x_barra,part,k): #BlOCOS IMPERFEITOS (SEM OS INSTANTES) DE UMA PARTICAO
	blocos_imperfeitos = []
	i = 1
	while i <= k:
		res = 0
		for j in range(len(part)): # pois len(particao) == len(x_barra)
			if part[j] == i:
				res = res + x_barra[j]
		if res != sum_perf(x_barra,k):
			blocos_imperfeitos = blocos_imperfeitos + [i]
		i = i + 1
	return blocos_imperfeitos

def segrep(pai,mae): # FUNÇÃO QUE RETORNA TRUE SE PAI PODE SER CONSTRUIDO A PARTIR DE MAE
	for i in pai:
		for j in range(len(mae)):
			if i == mae[j]:
				pai = apaga1(pai,i)
	if pai == []:
		return True
	else:
		return False







