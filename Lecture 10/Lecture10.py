# In[] Liste

a0 = [] # lista vuota
a1 = ["ciao", 9, 'python', (1,2), [], 3.14]
a2 = ['ciao']
# supporta: indicizzazione, slicing, concatenazione, ripetizione, funzione len

# Concatenazione e ripetizione
a3 = a1 + a2  # Nuova lista richiede len(a1)+len(a2) operazioni elementari
a4 = a1*2     # Nuova lista richiede 2*len(a1) operazioni elementari
              # Richiede molte risorse
print(a1, a2, a3, a4) 

a1.append('ciao') # Richiedeuna sola operazione elementare
                  # sereve per aggiungere alla fine della lista nuovi elementi
print(a1)

# In[] Indicizzazione e Del
a1 = ["ciao", 9, 'python', (1,2), [], 3.14]

a1[0] = None  # Sostituisce il valore presente nell indice 0 con None
print(a1)

del(a1[0])    #  Cancella il valore

# In[] Insert
a1 = ["ciao", 9, 'python', (1,2), [], 3.14]

a1.insert(0, None) # (Indice, Valore) 
                   # Aggiunge un valore in un idice specificato
                   # Non cancella il valore precedente ma spostta gli indici di tutti i valori succcesivi di 1
print(a1)
# %%
