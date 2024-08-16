import Evento

def nova_agenda(): #Função que devolve uma agenda vazia
    return []

def delE(c): #Função que elimina o evento atual da agenda c
    if len(c)>0:
        return c[1:]
    else:
         print("ERRO POIS AGENDA ESTÁ VAZIA")

def prox_evt(c): #Função que devolve o evento atual da agenda c
    if len(c)>0:
        return c[0]
    else:
        print("ERRO POIS AGENDA ESTÁ VAZIA")

# Se queremos adicionar um evento à agenda, temos que ter em conta os instantes de tempo
# Assumir que lista está ordenada por ordem crescente de tempos

def add_evt(c,e): #Função que adiciona o evento e à agenda c
    return [e1 for e1 in c if Evento.tempo(e1)<Evento.tempo(e)]+[e]+\
           [e1 for e1 in c if Evento.tempo(e1)>Evento.tempo(e)]



