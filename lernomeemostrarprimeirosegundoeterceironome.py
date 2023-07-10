 #programa para ler o nome completo de uma pessoa e mostrar o primeiro segundo e terceiro nome

seunome = input('degite seu nome')
separador = seunome.split()
indicacao = ["o primeiro nome é {}", "o segundo nome é {}", "o terceiro nome é {}", "o quarto nome é {}"]
for seunome, indicacao in zip(separador, indicacao):
     print(indicacao.format(seunome))