
# ======================================================
d = {1: 'uno', 2: 'dos', 3: 'tres'}

print d

d[4] = 'cuatro'
d[1] = '1'
del d[2]

print d

"""
# ======================================================
#print d[100]
print d.get(100)
print d.get(100, 'cien')
print d

if 5 not in d:
    d[5] = '5'
else:
    d[5] = 'cinco'

d[6] = 'seis' if 6 in d else '6'

print d
"""

"""
# ======================================================
numeros = dict([(x, 1.0/x) for x in range(1, 11)])
print numeros

for llave in numeros.iterkeys():
    print '%i: %.3f' % (llave, numeros[llave])

for llave, valor in numeros.iteritems():
    print '%i: %.3f' % (llave, valor)
"""

"""
# ======================================================
from collections import defaultdict
dd = defaultdict(int)

for val in [1, 2, 3, 2, 3, 3, 1, 2, 3, 1, 1, 1]:
    dd[val] += 1

for llave, valor in dd.iteritems():
    print '%i esta %i veces' % (llave, valor)

print 'Ordenado por llave'
for llave in sorted(dd):
    print '%i esta %i veces' % (llave, dd[llave])

print 'Ordenado por valor'
for llave in sorted(dd, key=dd.get):
    print '%i esta %i veces' % (llave, dd[llave])
"""

"""
# ======================================================
llaves = range(10)
valores = 'abcdefghi'

d = dict([(k, v) for k, v in zip(llaves, valores)])
print d

d2 = dict([(k, range(v)) for k, v in zip(valores, llaves)])
print d2
"""

"""
# ======================================================
from collections import defaultdict
from string import letters
dd = defaultdict(list)
llaves = range(10)
llaves.extend([x for x in llaves if x % 2 == 0])
llaves.extend(range(5))

print llaves
print letters

for llave in llaves:
    dd[llave].append(letters[llave])

print dd

for llave in dd.iterkeys():
    print '%s: %s' % (str(llave), str(dd[llave]))
"""

