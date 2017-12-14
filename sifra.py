#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:49:14 2017

@author: lov35174
"""

posun=int(input("O kolik se má abeceda posunout?>>> "))

a=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

b=a[posun:] + a[:posun]

slovo=input("Jaký text chceš šifrovat?>>> ")

slovo=slovo.upper()

for znak in slovo:
    x=b[a.index(znak)]
    print(x,end='')
