#CALCULAR AUMENTO DE SALARIO

salario = int(input('degite seu salario'))
porcentagem10 = 10
aumento10 = (porcentagem10 / 100) * salario

porcentagem15 = 15
aumento15 = (porcentagem15 / 100) * salario

if salario > 1250:
 salariocomalmento = salario + aumento10
 print(salariocomalmento)
else:
    print('sem aumento')

if salario < 1250:
    salarioatual = salario + porcentagem15
    print(salarioatual)