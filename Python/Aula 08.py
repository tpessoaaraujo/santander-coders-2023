# Métodos e Funções de Listas

# Adicionando elementos

lista = [1, 3, 12, 8, 2]

print ('Antes do append: ', lista)

lista.append(5)

print('Depois do append: ', lista)

lista.insert(2, 10)

print('Depois do insert: ', lista)

nova_lista = [1, 2, 3]

lista.extend(nova_lista)

print('Depois do extend: ', lista)

# Removendo elementos

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0) # Remove o elemento na posição 0

print('Lista após o pop: ', lista)

lista.remove(3) # Remove o elemento com valor 3

print('Lista após o remove: ', lista)

# Outros métodos

print('Quantidade de números 5 na lista: ', lista.count(5))

print('Qual é o índice do elemento 12: ', lista.index(12))

lista.sort() # Organiza os elementos em ordem crescente
print(lista)

lista.sort(reverse=True) # Organiza os elementos em ordem decrescente
print(lista)


# Funções

print(len(lista)) # Imprime quantos elementos tem na lista

print(sum(lista)) # Imprime a soma de todos os elementos da lista

print(min(lista)) # Retorna o menor elemento da lista

print(max(lista)) # Retorna o maior elemento da lista