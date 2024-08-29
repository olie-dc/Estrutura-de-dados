def bubble_sort(lista):
    """
    ALGORITIMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas, trocando entre si dois elementos adjacentes sempre que 
    o segundo for MENOR que o primeiro. Efetua tantas passadas quando necessaria, até que, na ultima passada, 
    nenhuma troca tenha sido efetuada.
    """

    #Loop eterno: não sabemos antecipadamente quantas passadas serao necessarias

    while True:

        #Variavel que controla e houve troca na passada 
        trocou = False

        #Percurso da lista, do primeiro ao PENULTIMO elemento, com acesso a cada posição

        for pos in range(len(lista) -1):
            #Se o valor que esta a frente na çlista (pos + 1) for MENOR que aquele que esta atras (pos), efetuamos a troca entre eles
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista [pos] = lista[pos], lista[pos + 1]
                trocou = True    #Houve troca na passada

        # cuidado com a identação aqui 
        # Se não houve troca na passada (trocou é false), a lista esta ordenada e interrompemos o loop eterno while
        if not trocou:
            break

#########################################################################################################################################

nums = [7, 9, 5, 4, 0, 3, 8, 1, 6,2]

print("ANTES:", nums)
bubble_sort(nums)
print("DEPOIS:", nums)