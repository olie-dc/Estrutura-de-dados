"Lista é uma estrutura de dados nativa da lingugem Python. Ela permite que varios valores sejam associados a uma unica variavel"

#Listas Strings
legumes = ["batata", "cenoura", "beterraba","mandioca", "nabo"]

#Lista de numeros 
nums =  [3, 10, -7, 12.8, -0.5, 4, 22]

#Lista com valores de varios tipos (pouco comum)
mistureba =  ["Joaquim", 37, 1.81, 79, True]

#### Operações sobre listas ####

#1) PERCURSO 
#Percorrer uma lista significa visitar cada um de seus itens e fazer algo com ele. No exemplo a seguir, vamos dar print() em cada um dos legumes.
#Após o leg pode ser subtituido por qualquer varivel - o que não pode mudar é o nome da lista, o for e o in. for X in Lista
for leg in legumes:
    print(leg)

#Traço separador
print("-" * 80)

#Percorrendo a lista de numeros e exibindo o valor do dobro de cada item 
for n in nums:
    print(n * 2)

#Traço separador
print("-" * 80)

#2) INSERÇÃO DE UM NOVO ELEMENTO NO FIM DA LISTA: append()
print('legumes, antes:', legumes)
print('nums, antes', nums)

#Iserindo novos itens ao final da lista 
legumes.append('batata-doce')
nums.append(-11)

print('legumes, depois:', legumes)
print('nums, depois', nums)

#3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert(), 
# PARAMENTROS:
#   1º ~> aposição onde sera feita a inserção (a contagem começa em zero)
#   2º ~> o novo elemento a ser inserido

#Inserindo um novo elemento na QUARTA posição:
legumes.insert(3, 'mandioquinha')
print(legumes)

#Inserindo um novo elemento na PRIMEIRA posição:
legumes.insert(0, 'cebola')
print(legumes)

# 4) ACESSANDO VALORES, INFORMANDO A RESPECTIVA POSIÇÃO 
print("Elemento da QUINTA posição:", legumes[4])
print("Elemento da PRIMEIRA posição:", legumes[0])
print("Elemento da ÚLTIMA posição:", legumes[-1])
print("Elemento da PENÚLTIMA posição:", legumes[-2]) 

#Traço separador
print("-" * 80)

# 5)SUBSTITUINDO VALORES EXISTENTES
print("ANTES:", legumes)

#Substituindo o valor na posição 3 (QUARTA posição)
legumes[3] = "vagem"

#Substituindo o valor n posição 0 (Primeira posição)
legumes[0] = "cará"

#Substituindo o valor na posição -1 (ULTIMA posição)
legumes[-1] = "inhame"

print("DEPOIS", legumes)

# 6) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()
print("Quantidade de elementos da lista de legumes:", len(legumes))
print("Quantidades de elementos da lista de números:", len(nums))

print("-" * 80)

# 7) REMOVENDO O *ULTIMO* ELEMENTO DE UMA LISTA: pop() (sem parametro)
print("ANTES:", legumes)
removido = legumes.pop()
print("Valor removido:", removido)
print("Depois:", legumes)

print("-" * 80)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() (com paramentro)

removido = legumes.pop(3)
print("Elemento removido da posição:", removido)
print(legumes)

removido = legumes.pop(0)
print("Valor removido da posição:", removido)
print(legumes)

print("-" * 80)

# 9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
legumes.remove("mandioquinha") #Não retorna valor
print(legumes)

print("-" * 80)

# 10) AUMENTANDO A UMA LISTA COM ELEMENTOS DE OUTRA LISTA: extend()
mais_legumes = ["abobrinha", "quiabo", "jiló", "cabotiá", "chuchu"]
legumes.extend(mais_legumes)
print(legumes)

print("-" * 80)

# 11) FATIANDO UMA LISTA
#     Fatiar significa copiar um pedaço da lista (uma sublista), criando uma nova lista 

# Criar uma sublista que contém os elementos das posições 2 a 5 
# (posição 6 *NÃO ENTRA*)
sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5:", sublista2_5)

# Criar uma sublista que contem os elementos dese o inicio ate a posição 6 (posição 7 *NÃO ENTRA*)
sublista_inicio_6 = legumes[:7]
print("Sublista do inicio da posição 6:", sublista_inicio_6)

#Criar uma sublista que contem os elementos da posição 4 ate o final da lista
sublista4_fim = legumes[4:]
print("Sublista da posição 4 ate o final da lista:", sublista4_fim)

