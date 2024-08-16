import Partição


def criarInd(Id,bloc_inst,coef,part): #Função que devolve um indivíduo sobre a forma de uma lista com as suas características:
	return [Id,bloc_inst,coef,part]   #Identificador, blocos perfeitos e os seus instantes de formação, coeficiente de inadaptação e partição 
                                      #inicial de um indivíduo

def Ident(i): #Função que devolve o identificador do indivíduo
	return i[0]

def bloc_instI(i): #Função que devolve os blocos perfeitos de um indivíduo e os seus instantes de formação
	return i[1]

def coefI(i): #Função que devolve o coeficiente de inadaptação de um indivíduo
	return i[2]

def partI(i): #Função que devolve a partição inicial de um indivíduo
	return i[3]

def Indinicial(x_barra,part,k,Id): # Aquele zero corresponde ao instante de tempo zero
	return [Id,Partição.blocos_perf(x_barra,part,k,0),Partição.coef_inadp(x_barra,part,k),part]
#Função que devolve um indivíduo com as suas características no instante de tempo zero


