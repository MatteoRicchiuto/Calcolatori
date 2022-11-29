
# In[] Correzione Esercizio x Casa

'''
1) Modificare browse_dir nel seguente modo: aggiungere un secondo parametro ext opzionale di tipo str che, 
   se specificato, stampi solo i file che hanno per estensione ext. Se non indicato, 
   la funzione si comporti nel modo originale.

 2) Modificare la precedente funzione in modo tale che, invece di stampare i nomi dei file, li ritorni in una lista.
'''
import os

def browse_dir(d, ext=None):
    '''
    imput: d è il nome di una cartella {un str}, ext è una str che indica un' estensione di file.
    output: stampa tutti i filein de in tutte le sue sottocartelle che terminano in .ext.
            se ext == None stampa tutti i file
    '''
    cartella = (os.listdir(d))
    b = []

    for x in cartella:
        full_path = os.path.join(d, x)
        
        if os.path.isfile(full_path):
            if ext == None or full_path.split(" ")[-1] == ext:
                print(f"FILE:{full_path}")
                
        elif os.path.isdir(full_path):
            c = browse_dir(full_path, ext=ext)
            b.extend(c) #! Equivalente a...
            
            #! for x in c:
                #! b.append()
        
    return b

b = browse_dir(os.getcwd(), "py")
print(b)
# In[]
a = "/Users/matteo/Documents/GitHub/Calcolatori/Lecture 15/Exercise14.py"

f = open(a)

for line in f:
    print(line)
    

# %%
