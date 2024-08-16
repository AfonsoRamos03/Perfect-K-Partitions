import Individuo
import Populacao
import Partição
import Obsrandom
import Evento
import Agenda
import random

def simulador(In,w,k,Tfim,TMut,TRep,TMor):
	ct = 0
	populacao = Populacao.newP()
	a = 0
	while a < In: # adicionar individuos à população com identidade de 1 a In-1
		populacao = Populacao.addI(Individuo.Indinicial(w,Partição.dude(w,k),k,a),populacao)
		a = a + 1
	agenda = Agenda.nova_agenda()
	b = 0
	while b < In: # adicionar eventos à agenda
		agenda = Agenda.add_evt(agenda,Evento.evt(Obsrandom.exprandom(TMut),"Mutação",b)) # aqui Id interessa
		b = b + 1
	agenda = Agenda.add_evt(agenda,Evento.evt(Obsrandom.exprandom(TRep),"Reprodução",0)) # Id não interessa muito, acho
	agenda = Agenda.add_evt(agenda,Evento.evt(Obsrandom.exprandom(TMor),"Morte",0)) # Id não interessa muito, acho

	while ct <= Tfim and Populacao.menor_coef(populacao) > 0:
		evento_atual = Agenda.prox_evt(agenda)
		ct = Evento.tempo(evento_atual)
		i = Evento.identificador(evento_atual)

		if Evento.tipo(evento_atual) == "Mutação":
			part = Individuo.partI(Populacao.Indi(populacao,i))

			sum_blocos_maior = [] # lista de blocos cuja soma é maior que sum_perf para se escolher aleatoriamente um desses blocos
			sum_blocos_menor = [] # same here
			for c in range(1,k+1):
				if Partição.sum_bloco(part,w,c) > Partição.sum_perf(w,k):
					sum_blocos_maior = sum_blocos_maior + [c]
				elif Partição.sum_bloco(part,w,c) < Partição.sum_perf(w,k):
					sum_blocos_menor = sum_blocos_menor + [c]
			y_mais = random.choice(sum_blocos_maior) # escolhe-se então o bloco, aleatoriamente
			y_menos = random.choice(sum_blocos_menor) # same here
			dif = Partição.sum_bloco(part,w,y_mais) - Partição.sum_bloco(part,w,y_menos)
			# vamos trabalhar com indices em vez de listas pois torna-se tudo mais fácil
			ind_mais = [random.choice(Partição.indices_bloco_k(w,part,y_mais))] # escolhe um indice da lista de indices do bloco y_mais, aleatoriamente
			x_mais = w[ind_mais[0]] # o valor de x_mais é então o valor de w que se encontra no indice "ind_mais"
			ind_menos = Partição.indices_bloco_k(w,part,y_menos) # same here
			imp_ind_menos = [] # é importante mais á frente para transferir os valores escolhidos de y_menos para y_mais
			comprimento = len(ind_menos)
			soma = 0
			d = 0
			while soma < (x_mais - (dif/2)) and d < comprimento: # condição do 3º tópico da mutacao (enunciado)
				ind = random.choice(ind_menos) # escolhe-se um elemento aleatoriamente de y_menos através do seu indice
				imp_ind_menos = imp_ind_menos + [ind] # mete-se o indice do elemento na tal lista que vai ser importante
				soma = soma + w[ind] # soma-se o valor do elemento à variável soma
				ind_menos = Partição.apaga1(ind_menos,ind) # retiramos o valor da lista para não correr o risco de se escolher outra vez
				d = d + 1

			for e in imp_ind_menos: # transferir os valores escolhidos de y_menos para y_mais
				part = part[:e] + [y_mais] + part[e+1:]
			for f in ind_mais: # transferir o valor x_mais para o bloco y_menos
				part = part[:f] + [y_menos] + part[f+1:]
			# agora que temos a nova partição, ganhamos diretamente o coef de inadp e o Id não muda. Só temos de ver os blocos_perfeitos
			# notar que náo podemos apenas somar aos blocos perfeitos iniciais, os possiveis blocos perfeitos que se formaram durante a
			# mutação, pois assim para alguns blocos perfeitos temos múltiplos instantes de formação e nós só queremos os originais
			blocos_perfeitos_iniciais = Individuo.bloc_instI(Populacao.Indi(populacao,i))
			blocos_perfeitos = Partição.blocos_perf(w,part,k,ct)
			for g in blocos_perfeitos_iniciais:
				h = 0
				while h < len(blocos_perfeitos):
					if g[0] == blocos_perfeitos[h][0]:
						blocos_perfeitos = blocos_perfeitos[:h] + blocos_perfeitos[h+1:]
					h = h + 1
			blocos_perfeitos = blocos_perfeitos_iniciais + blocos_perfeitos
			populacao = Populacao.eliminaI(i,populacao) # eliminamos o individuo antigo e adicionamos o mesmo individuo depois da mutação
			populacao = Populacao.addI(Individuo.criarInd(i,blocos_perfeitos,Partição.coef_inadp(w,part,k),part),populacao)
			agenda = Agenda.delE(agenda) # apagamos o evento que decorreu da agenda e adiciona-se outro
			agenda = Agenda.add_evt(agenda,Evento.evt(ct + Obsrandom.exprandom(TMut),"Mutação",i))


		elif Evento.tipo(evento_atual) == "Reprodução":
			pai = random.choice(populacao) # escolhe-se da populacao um individuo como pai
			mae = random.choice(Partição.apaga1(populacao,pai)) # escolhe-se da populacao (sem pai pois pai != mae) um individuo como mae
			if len(Individuo.bloc_instI(pai)) > 0: # condicao do 1º tópico da Reproduçáo (enunciado) para continuar com o evento

				bloco_pai = random.choice(Individuo.bloc_instI(pai)) # escolhe-se um bloco perfeito do pai, aleatoriamente
				blocos_mae_imp = Partição.blocos_imperfeitos(w,Individuo.partI(mae),k)
				indices_pai = Partição.indices_bloco_k(w,Individuo.partI(pai),bloco_pai[0])
				indices_mae_imp = []
				for j in blocos_mae_imp:
					indices_mae_imp = indices_mae_imp + Partição.indices_bloco_k(w,Individuo.partI(mae),j)
				if Partição.segrep(indices_pai,indices_mae_imp)==True:
					blocos_mae_perf = Individuo.bloc_instI(mae)
					bl = 1
					n = 0
					part_filho = [0]*len(w)
					while n < len(blocos_mae_perf):
						r = [i for i in range(0,len(w)) if Individuo.partI(mae)[i] == blocos_mae_perf[n]]
						for u in r:
							part_filho = part_filho[:u] + [bl] + part_filho[u+1:]
						bl = bl + 1
						n = n + 1
					s = [i for i in range(0,len(w)) if Individuo.partI(pai)[i] == bloco_pai[0] ]
					for t in s:
						part_filho = part_filho[:t] + [bl+1] + part_filho[t+1:]
					v1 = [i for i in range(0,len(w)) if part_filho[i]==0]
					v2 = [w[i] for i in v1]
					subpart = Partição.dude(v2,k-(bl+1))
					for x in range(0,len(w)):
						if part_filho[x]==0:
							part_filho = part_filho[:x] + [subpart[0]+bl+1] + part_filho[x+1:]
							subpart = subpart[1:]
					# falta qualquer coisa para os blocos perfeitos
					filho = Individuo.criarInd(In,Partição.blocos_perf(w,part_filho,k,ct),Partição.coef_inadp(w,part_filho,k),part_filho)
					populacao = Populacao.addI(filho,populacao)
					agenda = Agenda.add_evt(agenda,Evento.evt(ct + Obsrandom.exprandom(TMut),"Mutação",In))
					In = In + 1
			agenda = Agenda.delE(agenda)
			#agenda = Agenda.add_evt(agenda,Evento.evt(ct + Obsrandom.exprandom(TMut),"Mutação",0))
			agenda = Agenda.add_evt(agenda,Evento.evt(ct + Obsrandom.exprandom(TRep),"Reprodução",0))

		else:
			for l in populacao:
				if len(Individuo.bloc_instI(l)) >= 1 and Individuo.bloc_instI(l)[-1][1] > 2*(Individuo.bloc_instI(l)[0][1]):
					populacao = Populacao.eliminaI(Individuo.Ident(l),populacao)
			if populacao == []:
				m = 0
				while m < In: # adicionar individuos à população com identidade de 0 a (In-1)
					#populacao = Populacao.addI(Individuo.Indinicial(w,Partição.dude(w,k),k,m),populacao)
					nova_part = Partição.dude(w,k)
					populacao = Populacao.addI(Individuo.criarInd(m,Partição.blocos_perf(w,nova_part,k,ct),Partição.coef_inadp(w,nova_part,k),nova_part))
					m = m + 1
			agenda = Agenda.delE(agenda)
			agenda = Agenda.add_evt(agenda,Evento.evt(ct + Obsrandom.exprandom(TMor),"Morte",0))

		evento_atual = Agenda.prox_evt(agenda)
		ct = Evento.tempo(evento_atual)
		i = Evento.identificador(evento_atual)
	return (Populacao.melhor_part(populacao),Populacao.menor_coef(populacao)) # Retorna a melhor partiçao e coef de inadaptacao do ind da pop