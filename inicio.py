from ex3 import Aluno

a = Aluno(200,10)

print(f'Percentual de faltas: {a.calcula_faltas():.1f}\n')
print(f'{a.verifica_aprovacao()}')