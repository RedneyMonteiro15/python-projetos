from random import shuffle


print('-'*20)
print('Mega Sena'.center(20))
print('-'*20)
valores = [0, 0, 50, 250, 0, 50, 500, 750, 150]
shuffle(valores)
for c in range(1, 10):
    print(f'[ {c} ]', end=' ')
    if c == 3 or c == 6 or c == 9:
        print()
print('-'*20)
op = int(input('Sua opção: '))

if valores[op-1] > 0:
    print(f'\033[1;32mVocê ganhou {valores[op-1]}€\033[m')
else:
    print(f'\033[1;31mVocê não ganhou nada.\033[m')
print('-'*20)
print('\033[1;34mResultado da Mega Sena\033[m')
for i in range(0, 9):
    print(f'[{valores[i]:^3}]', end=' ')
    if i == 2 or i == 5 or i == 8:
        print()
