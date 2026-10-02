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
'''num1 = float(input('Digite o número: '))

if num1 >0:
    sinal= "Positivo."
elif num1<0:
    sinal="Negativo."

if num1 % 2 == 0 and num1!=0:
    print("O numéro é par e", sinal)
elif num1==0:
    print("O número é zero.")
else:
    print("O número é impar e", sinal)'''

#TERCEIRO
'''print()
num1 , num2 , num3 = map(float, input('Digite três números separados por espaços:').split())
print()
if num1>num2 and num1>num3:
    print("O maior número é",num1)
elif num2>num1 and num2>num3:
    print("O maior número é",num2)
elif num3>num1 and num3>num2:
    print("O maior número é",num3)
print()
'''

#QUARTO
'''print()
ano = int(input("Digite o ano que se deseja verificar:"))
print()
if ano % 4 ==0 and ano %100!=0:
    print(ano,"é um ano bissexto.")
elif ano %400==0:
    print(ano,"é um ano bissexto.")
else:
    print(ano,"não é um ano bissexto.")
    print()'''


#QUINTA
'''num_1 , op , num_2 =(input('\n Digite a expressão entre espaços:').split())
num1 =float(num_1)
num2 =float(num_2)

if op == "+":
    result = num1 + num2
elif op =="-":
    result =num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2!=0:
        result = num1 / num2
    else:
        print('\n Não é possível dividir um número por zero.')
        result= None
        
else:
    print("Operador inválido")

if result is not None:
    print('\n O resultado é', result)
print()'''

#AULA 01/10
num1 = float(input('Digite o número: '))

if num1% 5 == 0:
    mult5=', múltiplo de 5'
else:
    mult5=''

if num1 >0:
    sinal= "Positivo."
    if num1 % 2 == 0 and num1!=0:
        
        print(f"O numéro é par{mult5} e {sinal}")
    else:
        print(f"O numéro é impar{mult5} e {sinal}")

elif num1<0:
    sinal="Negativo."
    print(f'O número é {sinal}.')

elif num1 ==0:
    print("O número é zero.")