# Dicionários

# Criando dicionários

dicionario = {} # Criando dicionario vazio
dicionario = dict() # Criando dicionario vazio

dicionario = {'nome': 'Thiago', 'idade': 22, 'altura': 1.74} # Criando dicionário com elementos

print(dicionario['nome'])
print(dicionario['idade'])

print('------------------------------')

# Adicionando elementos no dicionário

dicionario['profissao'] = 'Programador'
print(dicionario)

print('------------------------------')

# Iterando sobre um dicionário

for i in dicionario:
    print(i) # Percorre as chaves do dicionário

print('------------------------------')

for i in dicionario:
    print(dicionario[i]) # Percorre os conteúdos das chaves

print('------------------------------')

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)