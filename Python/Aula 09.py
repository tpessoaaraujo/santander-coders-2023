# Funções

# Função inicial

def saudacao():
    print('Seja bem vindo!')
    
saudacao()

# Função com parâmetros

def saudacao(nome):
    print(f'Seja bem vindo {nome}!')
    
saudacao('Thiago')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo {nome} ao curso de {curso}!')
    
saudacao('Thiago')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    else:
        return num1 * num2

resultado = calculadora(10, 20, '-')
print(resultado)