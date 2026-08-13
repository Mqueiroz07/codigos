A = int(input("Digite o valor de A: "))
resultado= A
restos= []

while resultado > 0:
    quociente = resultado // 2
    resto = resultado % 2

    restos.append(resto)

    resultado = quociente


restos.reverse() 

binario = ''.join(str(bit) for bit in restos)

print(f'O número {A} em binário é: {binario}')