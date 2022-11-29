# In[]Apertura di un file 

a = "/Users/matteo/Documents/GitHub/Calcolatori/Lecture 8/Lecture8.py"

f = open(a) # Apertura file in modalita di lettura (default)

f = open('prova scittura.py', 'w') # Apertura file in modalita di scrittura.
f.write('print("ciao")')
f.close()


# In[] Esercizio di Prova
for line in f:
    print(line) if "str" in line else None
# %%
