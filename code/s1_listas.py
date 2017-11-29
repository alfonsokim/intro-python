
# ======================================================
lista = [0, (2, 'x'), ['otra', 'lista'], 6, 'A', 0.000001, 'dentro de la lista', False]

print  lista
print len(lista)

lista.append(10)

print lista

lista[0] = True

print lista
print len(lista)

"""
# ======================================================
print 'Solo los elementos pares'
pares = []
for i in range(len(lista)):
    if i % 2 == 0:
        pares.append(lista[i])

print pares
"""

"""
# ======================================================
lista.insert(4, 'insertado')
print lista
"""

"""
# ======================================================
print 'Solo pares con comprension de listas'
pares = [element for i, element in enumerate(lista) if i % 2 == 0]
print pares
"""

"""
# ======================================================
print 'Comprension de listas'
lista = range(10)
print lista

cuadrados = [e**2 for e in lista if e % 2 == 0]
print cuadrados

pares2 = [e**2 if e % 2 == 0 else ':)' for e in lista]
print pares2
"""

"""
print 'Comprension de listas 2'
numeros = range(0, 5)
print numeros
"""

"""
print '--- anidadas'
anidadas = [range(x) for x in numeros]
print anidadas
"""

"""
print '--- cuadrados'
cuadrados = [e**2 for interna in anidadas for e in interna]
print cuadrados
"""

"""
print '--- doble anidadas'
doble_anidadas = [[range(e)] for interna in anidadas for e in interna]
print doble_anidadas
print len(doble_anidadas)
"""

"""
print '--- doble anidadas 2'
doble_anidadas_2 = [[range(e) for e in interna] for interna in anidadas]
print doble_anidadas_2
print len(doble_anidadas_2)
"""
