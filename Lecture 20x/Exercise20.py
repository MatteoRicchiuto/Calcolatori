# In[]# In[Soluzione con metodo get]

import os

def analizza_test(cartella):
    d={}

    for filename in os.listdir(cartella):
        if filename.split(".")[-1] == "csv":    # split divide una stringa in due parti prima del punto e dpo il punto con -1 selezioniamo l'ultima parte ovvero l'estenzione
            print(filename)                     # analiziamo file name

            filepath = os.path.join(cartella, filename)     # creiamo nuova variabile che è composta dall'unione del percorso di cartella e di filename
            f = open(filepath)
            
            for line in f:
                k, v = line.split(';')  # dividiamo la stringa in due parti la prima (ovvero l'email l'associamo k)
                v = int(v)                              # la prima (ovvero l'email l'associamo k)
                                                        # la seconda (ovvero il voto lo associamo a v)
                if k in d:
                    d[k].append(v)
                else:
                    d[k] = [v]
            f.close
    return d
cartella = '/Users/matteo/Documents/GitHub/Calcolatori/Lecture 19'
print(analizza_test(cartella))