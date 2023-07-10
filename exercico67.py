c = 0
while True:
    n = int(input('digite seu numero'))
    for r in range(1, 11):
        c += 1
        print(f'{n} x {c} = {n * c}')
