"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem Python
capaz de armazenar múltiplos valores em uma única variável, por
meio de pares de chave-valor (key-value).
Um dicionário é delimitado por chaves {}. Diferentemente da 
lista, que tem posições numeradas, o dicionário possui posições
NOMEADAS. Cada uma das posições nomeadas de um dicionário (ou
seja, cada par de chave-valor) é chamada de PROPRIEDADE.
"""

#Um dicionario representando os dados de uma pessoa
pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos": ["Zeferino", "Adamastor", "Gercina"]
}

#Acessando o valor das propriedades 
print(f"Nome:", pessoa["nome"])
print(f"Idade:", pessoa["idade"])
print(f"Aposentado?", pessoa["aposentado"])

print("-" * 80)

#calculando o IMC (Indice de Massa Corporal)

imc =  pessoa["peso"] / pessoa["altura"] ** 2

#Nos f-strings delimitados por aspas duplas, é necessario usar aspas simples nos nomes das propriedades, e vice-versa
print(f"O IMC de {pessoa['nome']} é {imc}.")

######################################################################################################################################

#Usando dicionarios para represnetar formas geometricas 

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"      #Retangulo
}
forma2 = {
    "base": 6,
    "altura": 3,
    "tipo": "T"      #Triangulo 
}
forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"      #Elipse/ circulo      
}
forma4 = {
    "legume": 10,
    "fruta": 6.2,
    "tipo": "T"
}
forma5 = {
    "base": "batata",
    "altura": False,
    "tipo": "E"
}

from math import pi

def calc_area(forma):
    """
    Função que calcula a area de uma forma geometrica, dados a base, a altura e tipo passados dentro de um dicionario
    """
    match forma["tipo"]:
        case "R":           #Retangulo
            return forma["base"] * forma["altura"] 
        
        case "T":           #Triangulo
            return forma["base"] * forma["altura"] / 2
        
        case "E":           #Elipse/ circulo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        
        case _:             #Forma invalida
            return None  

print("-" * 80)

#Testes coma função calc_area()

print(f"Base: {forma1['base']}; altura: {forma1['altura']}; tipo: {forma1['tipo']}, area: {calc_area(forma1)}")

print(f"Base: {forma2['base']}; altura: {forma2['altura']}; tipo: {forma2['tipo']}, area: {calc_area(forma2)}")

print(f"Base: {forma3['base']}; altura: {forma3['altura']}; tipo: {forma3['tipo']}, area: {calc_area(forma3)}")

#print(f"Base: {forma4['base']}; altura: {forma4['altura']}; tipo: {forma4['tipo']}, area: {calc_area(forma4)}") #vai dar erro

#print(f"Base: {forma5['base']}; altura: {forma5['altura']}; tipo: {forma5['tipo']}, area: {calc_area(forma5)}") #vai dar erro


