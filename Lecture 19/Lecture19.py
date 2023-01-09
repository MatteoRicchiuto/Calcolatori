# In[] 455554
d = {'c':'ciao', 'h':'hello'}

v1 = d.get('c')    # prende il valore associato alla chiave 'c'
print(v1)

v3 = d.get('z')    #? se la chiave non esiste restistituisce None
#v3 = d['z']        #! se la chiave non esiste restituisce un errore
print(v3)

v4 = d.get('a', 'alo') # secondo parametro,
print(v4)              # permette di personalizzare l'output se chiave non esiste

# In[] utilizzare
def dizionario_iniziali( a ):

    d = {}              
    for x in a:         
        if x == '':    
            continue 
        k = x[0]   

#       if k in d:     
#           d[k].append(x) 
#      else:
#         d[k] = [x]  

        a = d.get(k,[])           #! metodo semplificato
        a.append(x)                     # se k esiste: 1) prendiamo la lista collegata alla chiave k e la associamo ad a
                                        #              2) aggiungia alla lista a il valore x
                                        #              3) sostituiamo la vecchia lista colegata a k con la nuova(a)
        d[k] = a                        # se k NON esiste:  1) creimao una nuova lista vuaota e la associamo ad a 
                                        #                   2) aggiungiamo alla lista vuota il valore x  
    return d                            #                   3) sostituiamo la vecchia lista colegata a k con la nuova(a)                             

print(dizionario_iniziali(['python', 'for', 'codice', 'programma', '', 'input', 'while', 'for', 'in']))
# %%
