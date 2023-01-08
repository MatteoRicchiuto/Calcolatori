# In[] Correzione Esercizio 1 x Casa
def find_in_file(filename, k):
    '''
    Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)
    lines = ()              # 0(1) overo costo costante
    r = 1                   # 0(1) 

    for line in f:          # eseguito 0(n)
        if k in line:       # len(line è) 0(1), 0(1) operazioni
            line += (r, )   # è 0(len(lines))+1
                            #! Visto che lines è una tupla non è possibili utilizzare append,
                            #! Quindi il costo è quadratico
        r += 1
    
    f.close()               # 0(1)
    return lines            # 0(1)

t = find_in_file("Exercise 17.py", "lines")
print(t)

#! COSTO COMPUTAZIONALE
# O(1) = Costante
# n = numero righe file 
# Nel caso peggiore , k in ogni riga, il costo è 0(n^2)   (quadratico)


# In[] Correzione Esercizio 1 x Casa V2
def find_in_file(filename, k):
    '''
    Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)
    lines = []              # 0(1) 
    r = 1                   # 0(1) 

    for line in f:          # Blocco ripetuto 0(n)
        if k in line:       # len(line è) 0(1), 0(1) operazioni
            lines.append(r) # O(1)
                            #? Visto che lines è una lista è possibili utilizzare append
        r += 1
    
    f.close()               # 0(1)
    return tuple(lines)     # nel caso peggiore 0(n)
         #? tuples traforma una lista in una tupla.

t = find_in_file("Exercise17.py", "lines")
print(t)

#! COSTO COMPUTAZIONALE
# len(line) è 0(1)
#
# Il costo della funzione è 0(n) 

# In[] Correzione Esercizio 2 x Casa
def find_in_file( filename, k):
    '''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
		    righe e le colonne del file in cui compare k. Per colonna si intende la posizione
		    all'interno della riga  
	'''
    f = open(filename)
    lines = []              # 0(1) overo costo costante
    r = 1                   # 0(1) 

    for line in f: 
        for c in range( len(line) - len(k) + 1 ): # per evitare errore out of range  
            # verifica se k è il line a partire dalla posizione 
            
            if k == line[c:c+len(k)]:
                lines.append( (r,c)) # O(1)
        r += 1
    
    f.close()               # 0(1)
    return tuple(lines)     # nel caso peggiore 0(n)
    
t = find_in_file("Exercise17.py", "lines")
print(t)
# %%
