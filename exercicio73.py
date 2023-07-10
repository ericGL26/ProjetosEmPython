times = (
    'América-MG',
    'Athletico Paranaense',
    'Atlético-GO',
    'Atlético-MG',
    'Bahia',
    'Bragantino',
    'Ceará',
    'Chapecoense',
    'Corinthians',
    'Cuiabá',
    'Flamengo',
    'Fluminense',
    'Fortaleza',
    'Grêmio',
    'Internacional',
    'Juventude',
    'Palmeiras',
    'Santos',
    'São Paulo',
    'Sport Recife'
)
#parte das prints
posicaofla = times.index('Flamengo')
print(f'A posicao do flamengo é {posicaofla}')
print(f'A lista do brasileirao é {times}')
print(f'Os 5 primeiros colocados foram {times[0: 6]}')
print(f'Os 4 ultimos colocados foram {times[-4:]}')
print(f'Em ordem alfabetica ficaria {sorted(times)}')