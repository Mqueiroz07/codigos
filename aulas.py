#CALCULADORA
'''num1 = float(input('Digite o primeiro número: '))
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

print('Resultado é:', resultado)'''


#IMPAR OU PAR
'''num1 = float(input('Digite o número: '))
if num1 % 2 == 0:
    print("O numéro é par!")
else:
    print("O número é impar!")'''
#PT.2
num1 = float(input('Digite o número: '))

if num1 >0:
    sinal= "Positivo."
elif num1<0:
    sinal="Negativo."

if num1 % 2 == 0 and num1!=0:
    print("O numéro é par e", sinal)
elif num1==0:
    print("O número é zero.")
else:
    print("O número é impar e", sinal)