from ex3 import Aluno

a = Aluno(200,10)

print(f'Faltas permitidas: {a.calcula_faltas():.0f}\n')
print(f'{a.verifica_aprovacao()}')