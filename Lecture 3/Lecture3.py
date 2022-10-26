# In[] Funzioni

'''
# hanno sempre le parentesi, dento la parentesi può esserci uno o più argomento
# print type int float str len ...
# esistono molte altre funzioni e sono accessibili atraverso le librie esterne.
'''
import random #per importare un modulo esterno (libreria)

print(random.random()) #numero a caso tra 0 e 1
    #nome libreia  nome funzione.

print(random.randint(10, 20)) #numero a caso tra intervallo dato

from math import cos #importa una sola funzone da un libreria 

from math import cos, sin # è possibili importare più funzioni insieme

import time as t # importa una libreia ma cambia nome

print(t.time()) #è come se avessimo scritto time.time

# In[] Creare la propria funzione

def ricerca_sottostringa(s1, s2):  #creazione di una funzione
#s1 e s2 sono ...
    i, trovato = 0, False
    while i <= len(s1)-len(s2):
        if s1[i:len(s2) + i] == s2:
            trovato = True
            break
        i += 1
    if trovato:
        print("la stringa 2 è presente nella stringa una in posizione " + str(i) + ".")
    else:
        print("Non c'è corrispondenza.")

a = input("inserisci stringa1: ")
b = input("inserisci stringa2: ")

ricerca_sottostringa(a, b)
# %%
