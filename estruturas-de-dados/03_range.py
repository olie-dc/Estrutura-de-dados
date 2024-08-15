"""
range() é uma função da linguagem Python que gera uma faixa de números. É muito usada em associação com listas e com instrução for.
"""

# 1) range() com *UM* paramentro
#   Gera uma faixa numérico que vai de 0 (zero)  até o valor do parametro
for num in range(10):
    print(num)

print("-" * 80)

# 2) range() com *DOIS* parametros
#   1º parametro ~> valor inicial da faixa
#   2° parametro ~> valor final da faixa (*NÃO INCLUIDO*)
for x in range(10, 16):
    print(x)

print("-" * 80)