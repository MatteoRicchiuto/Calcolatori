
# In[] Correzione Esercizio x Casa

'''
1) Modificare browse_dir nel seguente modo: aggiungere un secondo parametro ext opzionale di tipo str che, 
   se specificato, stampi solo i file che hanno per estensione ext. Se non indicato, 
   la funzione si comporti nel modo originale.

 2) Modificare la precedente funzione in modo tale che, invece di stampare i nomi dei file, li ritorni in una lista.
'''
import os

def browse_dir( d, ext=None ):
    '''
    Input: d è il nome di una cartella (un str), ext è una str che indica
        una estensione di file
    Output: ritorna la lista di tutti i file in d e in tutte le sue sottocartelle che
        terminanano in .ext. Se ext==None, stampa tutti i file
    '''
    
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            if ext == None or x.split('.')[-1] == ext:
                b.append(full_path)
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, ext=ext )
            b.extend(c)
            # equivalente a...
            #for x in c:
            #    b.append(x)
    return b
  
b = browse_dir( os.getcwd(), ext = 'py')
print(b)

# In[]Ricerca di file in base al contenuto

def browse_dir( d, txt ):
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path) and full_path.split('.')[-1] == 'py':
            f = open(full_path)
            for line in f:
                if txt in line:
                    b.append(full_path)
                    break
            f.close()
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, txt=txt )
            b.extend(c)
    return b
  
b = browse_dir( os.getcwd(), 'len' )
print(b)


# %%
