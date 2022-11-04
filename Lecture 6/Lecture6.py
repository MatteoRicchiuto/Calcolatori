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

def ricerca_sottostringa(s1, s2):  # Creazione di una funzione
                                   # s1 e s2 Parametri formali
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

ricerca_sottostringa(a, b)           # Invocazione della funzione
# In[] Return
# Return associa comme risultato un valore alla funzione 
# Return termina la funzione (tipo break)

def ricerca_sottostringa(x, y):
    p, trovato = 0, False
    while p <= len(x)-len(y) and not trovato: 
        if y == x[p:p+len(y)]:
            trovato = True
            break  
        p += 1
        
    if not trovato:
        return -1  # Esce dalla funzione
    else:
        return p   # Esce dalla funzione

        
        
a = input("inserisci stringa1: ")
b = input("inserisci stringa2: ")

k = ricerca_sottostringa(a, b)    
fkt < 0:
    print('KO')
else:
    print('OK')  

# In[] Fattoriale Generalizzato

def fattoriale_generalizzato(a, b):
    m, p = 1, a
    
    while p <= b:
        m *= p # m = m*p
        p += 1
        
    return m

# In[] Fattoriale Generalizzato Con Range

def fattoriale_generalizzato(a, b):
    m = 1
    
    for p in range(a, b+1):
        m *= p
        
    return m

# In[Varianti Range]

for n in range(10): # da 0 a 10 salendo di 1 es: 0, 1, 2, 3, 4, 5, 6
    print(n)
    
for n in range(10, 20, 2): # da 10 a 20 salendo di 2 es: 10, 12, 14, 16, 18, 20
    print(n)
    
for n in range(20, 10, -1): # da 20 a 10 scendendo di 1 es: 20, 19, 18, 17, ...
    print(n)