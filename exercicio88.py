import random
print('-='*40)
print('MEGA SENA')
print('-='*40)
jogosrodados = 0
quantidadejogos = int(input('Quantos jogos voce deseja? '))
for i in range(0, quantidadejogos):
        numale = random.sample(range(1, 61), 6)
        jogosrodados += 1
        print(f'jogo {jogosrodados}: {numale}')

print(' =-=-=-=-=-=-=-=-=-=-=-BOA SORTE! =-=-=-=-=-=-=-=-=-=-=')