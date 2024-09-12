def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITIMO DE ORDENAÇÃO QUICK SORT      
    Escolhe um dos elementos da lista para ser o pivô (na implementação
    será o ulitmo) e, na pimeira passada, divide a lista, a partir da posição final do pivô,
    em uma sublista a esquerda, contendo apenas valores menores que o pivô, e outra sublista a direitas, contendo apenas
    valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada uma das sublistas, até que toda a lista esteja ordenada.
    """
    #Quando não soubermos o valor da variavel 'fim', atribuimos a ela o valor da ultima posição da lista
    if fim is None: fim = len(lista) - 1


    #Para que o algoritimo de ordenação possa ser aplicado, é necessario que a faixa delimitada pelas variaveis  'ini' e 'fim' tenha, pelo menos, 
    #dois elementos. Caso contrario, saimos da função sem fazer nada
    if fim <= ini: return

    #Inicialização das variaveis
    pivot = fim
    div = ini -1

    #Percorre a lista na posição 'ini' ate a posição 'fim' -1
    for pos in range(ini, fim):
        #Se o elemento da posição 'pos' for MENOR  do que o elemento da posição 'pivot', executa algumas ações
        if lista[pos] < lista[pivot]:
            div += 1     #Avança 'div' em 1 posição 
            #Efetua a troca entre os elementos das posições 'pos' e 'div', caso sejam diferentes entre si
            if (pos != div):
                lista[pos], lista[div], = lista[div]. lista[pos] 

    #<~ Cuidado com a Identação aqui
    #Após o 'pos' chegar a sua posição final, 'div' deve ser incrementado uma ultima vez
    div += 1

    #Troca os elementos nas posições 'div' e 'pivot' entre si, colocando este ultimo em seu lugar definitivo, se ambos forem diferentes entre si
    if div != pivot:
        lista[div], lista[pivot] = lista[pivot], lista[div]

    #Agora, todos os elementos a esquerda do pivo sao menores do que ele, enquanto todos os elementos a sua direita
    #sao MAIORES que ele. Chamamos a função recursivamente para casa uma dessas sublistas
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

################################################################################################################################################
    
nums = [7, 9, 5, 4, 0, 3, 8, 1, 2]
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
print(f'Antes: ', nums)
quick_sort(nums)
print(f'Depois: ', nums)