import numpy as np
import os

lista_notas = []
lista = ['primeira','segunda','terceira']

for rank in lista:
    valor = int(input(f'Digite a {rank} nota: '))
    lista_notas.append(valor)

os.system('cls')

print(f'A soma das notas é : {sum(lista_notas)}')
print(f'A média das notas é : {np.mean(lista_notas):.2f} \n')

if np.mean(lista_notas) >= 7:
    print("Aluno promovido.")
else:
    print("Aluno retido.")