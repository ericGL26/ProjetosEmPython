print('-'*60)
escolha = input('Quer comecar? [s \ n')
masculino = 0
maiordeidade = 0
mulhermenoridade = 0
primeiraiteracao = True
while escolha == 's':
    escolha = input('Quer continuar? [s \ n')
    if escolha == 's':
        print('CADASTRE UMA PESSOA!')
        idade = int(input('Idade:'))
        sexo = input('Sexo: [m \ f]')
        if sexo == 'm':
            masculino += 1
        if idade > 17:
            maiordeidade += 1
        if sexo == 'f' and idade < 20:
            mulhermenoridade += 1
    else:
        print('Codigo cancelado')

print(f'Total de pessoas com mais de 18 anos sao {maiordeidade}')
print(f'ao todo temos {masculino} homens cadastrados')
print(f'E temos {mulhermenoridade} mulher com menos de 20 anos')