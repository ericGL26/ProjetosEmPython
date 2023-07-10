
#calcular emprestimo
salario = int(input('degite seu salario'))
valorcasa = int(input('degite o valor da casa'))
parcelas = int(input('quantas parcelas deseja pagar?'))
porcemtagem = 30
limite = (valorcasa * porcemtagem) / 100

if salario > limite:
    print('negado')
else:
    taxamensal = valorcasa / parcelas
    print('a prestacao mensal será de {}'.format(taxamensal))
    tempo = valorcasa / taxamensal
    print('levará {} anos para quitar a casa'.format(tempo))