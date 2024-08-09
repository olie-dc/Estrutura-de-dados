"Calculo IMC - Funções basicas." 

from pickle import NONE


def imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado

print(f'O IMC de uma pesoa com 1,74m e 81kg é:', imc(81, 1.74))
##################################################################################################################################

"Calculo area de formas geometricas planas - Funções basicas."

def calc_area(base, altura, tipo):
    if tipo == 'R':
        return base * altura
    elif tipo == 'T':
        return base * altura / 2
    elif tipo == 'E':
        return (base / 2 ) * (altura / 2) * 3.14
    else:
        return NONE     

print(f"Area do retangulo 22x47: {calc_area(22, 47,'R')}")
print(f"A area do triangulo 12, 5x25: {calc_area(12.5, 25 , 'T')}")
print(f"Area elipse 20x30: {calc_area(20, 30, 'E')}")
print(F"Area invalida 8x11, 5: {calc_area(8, 11.5, 'W')}")
##################################################################################################################################
