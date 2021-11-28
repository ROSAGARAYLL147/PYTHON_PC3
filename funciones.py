# Declaración de una lista
lista = list()

# Cuenta el número de elementos de la lista
len(lista)

# Agrega un elemento (x) al final de la lista.
lista.append(x)

# Inserta un elemento (x) en una posición determinada (pos)
lista.insert(pos, x)

# Une dos listas (une la lista2 (la que se pasa como parámetro) a la lista)
lista.extend(lista2)

# Borra el primer elemento de la lista cuyo valor sea x. Sino existe devuelve un error
lista.remove(x)

# Borra el elemento en la posición dada de la lista, y lo devuelve.
lista.pop(pos)

# Borra todos los elementos de la lista (lista.clear())
del lista[:]

# Devuelve el índice en la lista del primer elemento cuyo valor sea x.
lista.index(x)

# Devuelve el número de veces que x aparece en la lista.
lista.count(x)

# Ordena los ítems de la lista
lista.sort(cmp=None, key=None, reverse=False)

# Invierte los elementos de la lista.
lista.reverse()

# Devuelve una copia de la lista (lista.copy())
listaCopia = lista[:]