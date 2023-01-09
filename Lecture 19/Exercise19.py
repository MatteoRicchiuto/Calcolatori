# In[] Correzine H_Ex18, ex1
def dizionario_iniziali( a ):
    '''
    Input: una lista di n stringhe
    Output: un dizionario d che mappa caratteri in liste di stringhe tale che
        se d[k] = b, b contiene tutte le stringhe in a che iniziano per k 
    '''
    d = {}              # O(1)
    for x in a:         # per n volte
        if x == '':     # O(1)
            continue # torno a testare la condizione del ciclo saltando
                    # la  parte restante del blocco
        k = x[0]        # O(1)
        if k in d:      # O(1)
            d[k].append(x) # O(1) lettura del dizionario + O(1) per append
        else:
            d[k] = [x]  # O(1) costo per creare la lista + O(1) per scrittura
                        # nel dizionario
    return d


print(dizionario_iniziali(['python', 'for', 'codice', 'programma', '', 'input', 'while', 'for', 'in']))


# In[] Correzine H_Ex18, ex2
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

#! Costo Computazionale
# Assumiamo che n sia la dimensione complessiva di tutti li file
#
#n*O(1) = O(n) 

# %%
