TxAA = 13.90

Vi = float(input("Digite o valor do investimento: "))
CDI = float(input("Digite quantos porcento do CDI: "))
Período = int(input("Digite o número de meses da aplicação: "))

DU= Período*21
TxD = (1+TxAA/100)**(1/252) -1
TxSD = TxD*CDI
VF = Vi*(1+TxSD/100)**DU
print(f'O valor finaldo investimento é: {VF:.2f}')