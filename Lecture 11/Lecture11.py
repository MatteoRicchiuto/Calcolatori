
# In[] Operatore in

print(2 in (4, 2, "ciao"))  # 2 è nella tupla?
print(2 in [4, 2, "ciao"])  # 2 è nella lista?
        # Se vero = True
        # Se falso = False

# In[] Operatori max, min e sum
#!Liste e tuple
a = [1,5,4,3,0]   # Funzionano con tuple, liste e stringhe
b = ["python", "zorro", "casa"] 

print( max(a), max(b))  # Numero più grande o stringa con valore alfabetico maggiore
print( min(a), min(b))  # Numero più piccolo o stringa con valore alfabetico minore
print( sum(a))          # Somma di tutti i numeri
                        # Non si può fare somma tra stringhe
    
    # Questi operatori funzionano soltanto se sono utilizati tra valori comparabili tra di loro

# In[] Aliasing e clonazione liste
a = [10,10,5,5]

b = a[:]  # clonazione Intera Lista

# Aliacing
c = a            # = associa un secondo nome alla lista
c[1] = "casa"    # Funziona soltanto per le liste

print(b) # a = 10,10,5,5
print(a) # c = 10,casa,5,5
print(c) # a = 10,casa,5,5

