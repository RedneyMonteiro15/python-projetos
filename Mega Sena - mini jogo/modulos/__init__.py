def LeiaInt(msg):
    while True:
        num = input(msg)
        if(num.isnumeric()):
            num = int(num)
            if(10 > num > 0):
                return num
            print('\033[1;31mERRO!!! Digite uma opção válido.\033[m')
        else:
            print('\033[1;31mERRO!!! Digite um número inteiro\033[m')
