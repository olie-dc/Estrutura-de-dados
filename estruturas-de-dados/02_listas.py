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






