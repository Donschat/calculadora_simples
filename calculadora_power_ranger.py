def soma(a, b):
    s = a + b
    print(f'o resultado da soma é {s}')


def mult(a, b):
    s = (a * b)
    print(f'o resultado da multiplicação é {s}')


def div(a, b):
    s = (a / b)
    print(f'o resultado da divisão é{s:.4f}')


def sub(a, b):
    s = (a - b)
    print(f'o resultado da subtração é {s}')


print('*'*30, '\n', 'MegaCalculator Power Ranger')
print('*'*30)
while True:
    while True:
        try:
            a = int(input('Primeiro valor: '))
            break
        except ValueError:
            print('Digite apenas números.')
    while True:
        try:
            b = int(input('Segundo valor: '))
            break
        except ValueError:
            print('digite apenas números.')
    while True:
        try:
            op = input('Qual a operação? digite penas um operador (+, - , / , *): ')
            if op in '+,-,/,*':
                break
        except ValueError:
            print('digite apenas um operador [+, -, /, *')
    if op == '+':
        soma(a, b)
    elif op == '-':
        sub(a, b)
    elif op == '/':
        div(a, b)
    elif op == '*':
        mult(a, b)
    else:
        print('Você fez um operação inválida. Reinicie o programa')
    if op in '+, -, /, *':
        teste2 = str(input('Deseja continuar? [s/n]'))
        if teste2 == 's':
            continue
        else:
            break
print('*'*30, 'Obrigado por utilizar a MegaCalculator Power Ranger'.format(), '*'*30)