#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:52:27 2020
"""

print('Escribe un número de más de 2 digitos:')

p = input()
sd = False
c = 1
while not sd:
    nn = int(str(p)[0])
    lp = len(str(p))
    for i in range(1,lp):
        nn = nn*int(str(p)[i])
    print('\n'+str(c)+':\t'+str(nn))
    c = c + 1
    p = nn
    if len(str(nn)) == 1:
        sd = True
    