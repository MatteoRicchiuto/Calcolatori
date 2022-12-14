''' 
    Un dizionario è una raccolta di elementi che sono identificati da:
        - un valore e una chiave.
'''

d0 = {}                                     # Dizionario vuoto
d0 = {"chiave" : "valore"}                  # Strutura

d0 = {"k1": 6, True : "due" , ("ciao", 2) : 3.12}   # Esempio
# d1 = {[1,2] : False, {1,2} : False}       #! Errore: non si possono usare liste e dizionari come chiavi

# In[] Lettura
d0 = {"k1": 6, True : "due"}

print(d0)           # Stampa tutto il dizionario 
print(d0["k1"])     # Stampa il valore associato alla chiave (k1)
#print(d0["k9"])    #! Errore: "k9" non è una ciave del dizionar0


# In[] Scrittura
student = {"name" : "Matteo", "age" : 18 }

student["age"] = 19         # Sovrascrittura 
student["year"] = 2022      # Aggiunta          
                            # Questi metodi permettono di modificare o aggiunfere un valore alla volta)

student.update({"age" : 20, "year" : 2023, "id" : 34323 })  
                            # Sovrascrittura e aggiunta multipla
print(student)


# In[] Cancellazione
student = {"name" : "Matteo", "age" : 18 }

del(student["age"])
#del(student["Matteo"])  #! Errore: "Matteo" non è una delle chiavi

print(student)

# In[] Altre funzioni
student = {"name" : "Matteo", "age" : 18 } 

print(len(student))         # Stampa numero di chiavi

print(student.keys)         # Stampa soltanto le chiavi
print(student.values)       # Stampa soltanto i valori

print(student.items)        # Stampa i valori e le loro chiavi (pair o coppie)

# In[] Loop
student = {"name" : "Matteo", "age" : 18 } 

for key in student:         
    print(key)              # Loop nelle chiavi

for values in student.values():
    print(values)           # Loop nei valori

for keys, values in student.items():
  print(keys, values)       # Loop nelle chiavi e valoro
    

# In[] Tip
#todo Scrittura Legibile di un dizionario

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# %%
