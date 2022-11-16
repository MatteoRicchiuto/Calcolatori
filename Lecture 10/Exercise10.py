
# In[] Esercizio per casa
'''
Si progetti una funzione denominata init_tuple che prenda in input un intero positivo n e, opzionalmente, una funzione v. 
La funzione restituisca una tupla di lunghezza n che in posizione i contenga v(i). 
Qualora il parametro v non fosse specificato, la funzione restituirebbe una tupla composta da n zeri.

Suggerimento. Potrebbe essere utile partire da una tupla vuota - si indica così () - e poi procedere per concatenazioni successive. 
A tal proposito si provi ad usare l'operatore + come si fa con le stringhe. 
Una tupla composta da un unico elemento e si definisce in questo modo (e, ).

Utilizzare la funzione init_tuple per creare una tupla contenente i primi 10 numeri dispari

Utilizzare la funzione init_tuple per creare una tupla contenente 10 stringhe non vuote di lunghezza crescente

Utilizzare la funzione init_tuple per creare una tupla contenente 10 tuple tali che la tupla in posizione i sia lunga 10 e contenga i in ogni posizione. 
Suggerimento: come per le stringhe, * sulle tuple è l'operatore di ripetizione.
'''

def init_tuple(n, v=0):
    tupla = ()
    i = 0
    while i < n:
        tupla += (v, )
        i += 1

    return(tupla)

init_tuple(12,5)

# In[] Esercizio per casa 2
def init_tuple(i=0):
    tupla = ()
    while len(tupla) < 10:
        if i % 2 == 1:
            tupla += (i, )
        i += 1
        
    return(tupla)
init_tuple(10)

# In[] Esercizio per casa 3
def init_tuple():
    tupla = ()
    while len(tupla) < 10:
        if i % 2 == 1:
            tupla += (i, )
        i += 1
        
    return(tupla)
init_tuple(10)