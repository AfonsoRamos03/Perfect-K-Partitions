import Individuo

def newP(): # CRIA UMA POPULAÇÃOO VAZIA
    return []

def eliminaI(Id,pop): # ELIMINA O INDIVÍDUO COM IDENTIFICADOR Id DA POPULAÇÃO
    return pop[:Id]+pop[Id+1:]

def addI(Ind,pop): # ADICIONA UM INDIVÍDUO  À POPULAÇÃO
	if pop == []:
		return [Ind]
	else:
		return pop[:Individuo.Ident(Ind)] + [Ind] + pop[Individuo.Ident(Ind):]

def menor_coef(pop): # DÁ O MENOR COEF DE INADAPTAÇÃO QUE VAI SER UM DOS OUTPUTS DO SIMULADOR
	coef = Individuo.coefI(pop[0])
	for i in pop:
		if Individuo.coefI(i) < coef:
			coef = Individuo.coefI(i)
	return coef

def melhor_part(pop):  # DÁ A MELHOR PARTIÇÃO ASSOCIADA AO MENOR COEF DE INADAPTAÇÃO, QUE TAMBÉM VAI SER UM DOS OUTPUTS DO SIMULADOR
	coef = Individuo.coefI(pop[0])
	part = Individuo.partI(pop[0])
	for i in pop:
		if Individuo.coefI(i) < coef:
			coef = Individuo.coefI(i)
			part = Individuo.partI(i)
	return part

def Indi(pop,Id): # DEVOLOVE O INDIVÍDUO COM IDENTIFICADOR Id
	return pop[Id]



