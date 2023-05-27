# Estruturas Condicionais

print('------------------------------')
print('Sistema de cálculo de média')
print('------------------------------')

aluno = str(input('Digite o nome completo do aluno: '))

print('------------------------------')
print('Aluno: ', aluno)
nota_de_matematica = float(input('Digite o valor da nota de matemática: '))
nota_de_portugues = float(input('Digite o valor da nota de português: '))
nota_de_historia = float(input('Digite o valor da nota de história: '))

media = (nota_de_matematica + nota_de_portugues + nota_de_historia) / 3

if media >= 7:
    print('A média do aluno', aluno, 'é igual a', media)
    print('Aluno aprovado!')
elif media >= 5:
    print('A média do aluno', aluno, 'é igual a', media)
    print('Aluno de recuperação!')
else:
    print('A média do aluno', aluno, 'é igual a', media)
    print('Aluno reprovado!')
    
print('Os dados foram registrados.')
print ('Encerrando sistema de cálculo de média.')
print('------------------------------')