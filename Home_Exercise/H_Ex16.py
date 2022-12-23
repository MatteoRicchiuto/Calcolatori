# In[] Ex1

def find_in_file( filename, k):
    '''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)      # O(1)
    h = ()                  # O(1)
    r = 1                   # O(1)
    for line in f:          #? blocco ripetuto O(n)
        if k in line:           # se len(line) è O(1), O(1) operazini      
            h += (r, )          # 0(len(line))
        r += 1
    
    f.close()               # O(1)
    return h                # O(1)


print(find_in_file("H_Ex16.txt", "ciao"))

#! Costo
# O(1) = Costante
# n = numero righe file 
# nel caso peggiore costo della funzione = O(n^2)
# In[] Ex2
def find_in_file( filename, k):
    '''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
		righe e le colonne del file in cui compare k. Per colonna si intende la posizione
		all'interno della riga  
	'''
    f = open(filename)      # O(1)
    h = ()                  # O(1)
    r = 0                   # O(1)

    for line in f: 
        for c in range(len(line)-len(k)):
            
                if k == line[c:c+len(k)]:
                    h += ((r,c), )
                c =+ 1
        r += 1
    
    f.close()
    return h
	
print(find_in_file("H_Ex16.txt", "i"))
# %%
