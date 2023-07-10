listaaluno = []
listanota = []
while True:
    escolha = input('Quer continuar: [s/n]')
    if escolha == 's':
        listaalunotemp = []
        listanotatemp = []
        nomealuno = input('Digite seu nome:')
        nota1 = int(input('Digite sua primeira nota:'))
        nota2 = int(input('Digite sua segunda nota:'))
        media = (nota1 + nota2) / 2
        listanotatemp.append([nota1, nota2])
        listanota.append(listanotatemp[:])
        listaalunotemp.append([nomealuno, media])
        listaaluno.append(listaalunotemp)
    else:
        break
print('-'*40)
print('   Aluno,Media')

for i in listaaluno:
    nome = i[0][0]
    media = i[0][1]
    print(nome, media, end='\n')
print(listanota)
#Parte de printar aluno escolhido
while True:
    escolhaalum = int(input('Quer verificar a media de qual aluno?, 999 interrompe'))
    if escolhaalum != 999:
        print(f'Notas de {listaaluno[escolhaalum][0][0]} são {listanota[escolhaalum]}')
    else:
        break