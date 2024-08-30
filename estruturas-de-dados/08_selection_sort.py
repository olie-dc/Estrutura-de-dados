def selection_sort(lista):
    """
    ALgoritimo de ordenação selection sort
    Isola (Seleciona) o primeiro elemento da lista e, em seguida, encontra o menir valor entre os elementos do restante da lista.
    Seo valor encontrado for MENOR que o valor previamente selecionado efetua a troca entre eles. Continuando, sleeciona o segundo elemento da lista,
    buscando pelo meno nas posições subsequentes. Faz a troca entre os dois valores, se necessario. O processo se repete ate o penultimo 
    elemento da lista seja selecionado, comparado com o ultimo e feita a troca entre eles, se for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    for pos_sel in range(len(lista) -1):
        passd += 1 #iNICIA UMA NOVA PASSADA

        #Inicia supondo que a posição do menor valor da lista é o que imediatamente a frente do valor selecionado
        pos_menor = pos_sel + 1


        #Percorre o retsante da lista, da posição seguinte a pos_menor ate a altima posição

        for pos in range(pos_menor + 1 ,len(lista)):
            #Se o valor que estiver na posição (pos) atual for menor que aquele apontado por pos_menor, ajusta pos_menor para o mesmo valor de pos
            
            comps += 1 #Comparação do if abaixo
            if lista[pos] < lista[pos_menor]: pos_menor = pos


        #Cuidado com a identação
        #Neste ponto, ja terminamos de percorre o restante da lista e sabemos a posição do menor valor que ha nele.
        #Comparamos, então, os valores da posições pos_menor e pos_sel. Se o primeiro for MENOR que o segundo, fazemos a troca entre eles.
        
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

##################################################################################################################################################
            
nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]

print("ANTES:", nums)
selection_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; Trocas: {trocas}; passadas: {passd}")


