# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import random
participantes = ['Meli','Santi','Cris', 'Ivan', 'Chiqui','Caro']

print('Participantes: ', end = '' )

[print(x, end = ' ' ) for x in participantes]


random.shuffle(participantes)

print('\nSorteo:')

for i,j in enumerate(participantes):    
    print( str(i+1) + "- " + j )
