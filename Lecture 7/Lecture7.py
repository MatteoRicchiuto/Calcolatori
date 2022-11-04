# In[] Stringe formattate 

name = "Matteo"
age = "19"

print("Il tuo nome è " + name + "e hai " + str(age) + "anni.")
print(f"Il tuo nome è {name} e hai {str(age)} anni.")  
# Stringa formattata è possibile aggiungere variabli alle stringe mettendole tra parentesi graffe
# più breve ed immediata da scrivere

# In[] \ prima del carattere 
'''
Come aggiungere caratteri come ", ', / che normalente non possono essre scritti in stringhe.
'''
print("Il tuo nome è \"matteo\" e hai 19 anni.") 
# Scrivere \ prima del carattere 

# In[] Andare a capo in un print
print("Il tuo nome è matteo n\ Hai 19 anni.") 

# In[] Valore di default

def radice_quadrata(x, esp=0.01) # Se esp non viene dichiarato, verra preso come valore di default o.o1
    
    g = x/2

    while abs(g * g - x) > esp: # esp aprossimazione della radice
                                # abs il risultato è sempre positivo, abs(-20) = 20 
        g = 0.5 * (g + x / g)

    return g

print(radice_quadrata(20, 0.0000001))  # esp dichiarato = 0.0000001
print(radice_quadrata(20))             # esp NON dichiarato = 0.01

''' Scrivere valore parametri formali dichiarandole'''

print(radice_quadrata(esp=0.0000001, x=20  ))  # Molto utile per funzioni con molte variabili
# %%
