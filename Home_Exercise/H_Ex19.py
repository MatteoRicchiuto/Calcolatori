# In[] ex1
'''
Modificare la precedente funzione in modo che il dizionario associ indirizzi email 
al voto finale derivante da tutte le prove a cui hanno partecipato gli studenti.
Per il voto finale ogni prova intermedia contribuisce nel seguente modo: 
da 0 a 5 punti il contributo è 0, con 6 il contributo è 0.3, 
con 7 il contributo è 0.4, con 8 il contributo è 0.6, 
con 9 punti il contributo è 1 e con 10 punti il contributo è 1.5.
'''
import os

def analizza_test(cartella):
    d={}
    d1={}

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

                for keys, values in d.items():
                    voto = 0
                    for r in values:
                        if r == 6:
                            voto = voto + 0.3
                        elif r == 7:
                            voto = voto + 0.4
                        elif r == 8:
                            voto = voto + 0.6
                        elif r == 9:
                            voto = voto + 1
                        elif r == 10:
                            voto = voto + 1.5
                        else:
                            voto = voto + 0
                    d1[keys] = voto
                        

            f.close
    return d1

cartella = '/Users/matteo/Documents/GitHub/Calcolatori/Lecture 19x'
print(analizza_test(cartella))

# %%