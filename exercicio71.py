seunumero = int(input('digite seu numero'))
listanumeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
if seunumero > 20:
    print('digite um numero valido')
else:
    print(listanumeros[seunumero])