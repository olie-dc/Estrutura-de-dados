comps = trocas = passd = None    #Variaveis de estaticas



def bubble_sort(lista):
    """
    ALGORITIMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas, trocando entre si dois elementos adjacentes sempre que 
    o segundo for MENOR que o primeiro. Efetua tantas passadas quando necessaria, até que, na ultima passada, 
    nenhuma troca tenha sido efetuada.
    """

    global comps, trocas, passd
    comps = trocas = passd = 0

    #Loop eterno: não sabemos antecipadamente quantas passadas serao necessarias

    while True:

        passd += 1            #inicio de uma nova passada"

        #Variavel que controla e houve troca na passada 
        trocou = False

        #Percurso da lista, do primeiro ao PENULTIMO elemento, com acesso a cada posição

        for pos in range(len(lista) -1):
            #Se o valor que esta a frente na çlista (pos + 1) for MENOR que aquele que esta atras (pos), efetuamos a troca entre eles
            
            comps += 1          #compração d eif abaixo 

            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista [pos] = lista[pos], lista[pos + 1]
                trocas += 1 
                trocou = True    #Houve troca na passada

        # cuidado com a identação aqui 
        # Se não houve troca na passada (trocou é false), a lista esta ordenada e interrompemos o loop eterno while
        if not trocou:
            break

#########################################################################################################################################

# nums = [7, 9, 5, 4, 0, 3, 8, 1, 6,2]

#Pior caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#Melhor caso
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]

print("ANTES:", nums)
bubble_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; Passadas: {passd}")


############################################################################################################################################

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTES COM A LISTA DE NOMES
from data.nomes_desord import nomes

#Recortando os 100k primeiros nomes
nomes = nomes[:100000]

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()

print(nomes)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")