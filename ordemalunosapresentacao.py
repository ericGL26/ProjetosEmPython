import random
alunos = ['joao', 'pedro', 'maria', 'duda', 'alex']
ordem_alunos = []
for i in range(5):
    sorteio = random.choice(alunos)
    ordem_alunos.append(sorteio)
    alunos.remove(sorteio)
if len(ordem_alunos) > 1:
    print('a ordem de alunos é {}'.format(ordem_alunos))
