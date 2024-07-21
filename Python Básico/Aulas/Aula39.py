"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, *
create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)

"""
lista = [10, 20, 30, 40]

# lista[2] = 300
# del lista[2]

lista.append(50)
lista.append(60)
lista.append(70)
print(lista)
#omprime [10, 20, 30, 40, 50]

#podemos remover através de indices

ultimo_valor = lista.pop(3)
print('Removido:', ultimo_valor)
print(lista)







