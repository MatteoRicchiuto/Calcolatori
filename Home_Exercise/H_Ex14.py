'''
Esercizi per casa

    Modificare browse_dir nel seguente modo: aggiungere un secondo parametro ext opzionale di tipo str che, se specificato, stampi solo i file che hanno per estensione ext. Se non indicato, la funzione si comporti nel modo originale.

    Modificare la precedente funzione in modo tale che, invece di stampare i nomi dei file, li ritorni in una lista.
'''

import os

def browse_dir( d ):
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            print(f'FILE: {full_path}')
        elif os.path.isdir(full_path):
            browse_dir( full_path )
            
browse_dir( os.getcwd("/Users/matteo/Documents/GitHub/Calcolatori/Home_Exercise") )