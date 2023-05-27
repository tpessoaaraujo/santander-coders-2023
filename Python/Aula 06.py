# Estrutura de repetição com for

for i in range(5):
    print(i)

print('------------------------------')

for i in range(1, 10):
    print(i)
    
print('------------------------------')

for i in range(1, 12, 3):
    print(i)

print('------------------------------')

soma = 0

for i in range(4):
    nota = float(input(f'Informe a nota {i}: '))
    soma = soma + nota
media = soma / 4    
print ('A média é igual a ', media)