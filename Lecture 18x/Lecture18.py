# Un dizionario è una rcaccolta di elementoi che sono identi ficati:
# da un valore e da una chiave.
# In[] Dizionario
d0 = {} # Dizionario vuoto
d1 = {"k0": 6, "k1":"python", 6:3.12} 


## Lettura

print(d1)           # Stampa tutto il dizionario 
print(d1["k1"])     # Stampa il valore associato alla chiave (k1)
#print(d1["k9"])    #! Errore non è una ciave del dizionario

## Scrittura

d1["k0"] = True     # Sovrascrittura 
d1["L"] = False

print(d1)

## Cancellazione

del(d1["k0"])
#del(d1["python"]) . #! Errore: python non è una delle chiavi

print(d1)

# %%
