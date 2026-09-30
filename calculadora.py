num1 = float(input('Digite o primeiro número: '))
sinal = input('Digite o operador matemático ( +, -, *, / ): ')
num2 = float(input( 'Digite o segundo número: '))

if sinal == '+':
    resultado = num1 + num2
elif sinal == '-':
    resultado = num1-num2
elif sinal == '*':
    resultado = num1*num2
elif sinal == '/':
    resultado = num1/num2
else:
    print('operador inválido')

print('Resultado é:', resultado)