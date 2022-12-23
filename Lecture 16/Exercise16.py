# In[] Correzione esercizio per casa L15

def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''

    n = len(bins) + 1       # aggiung 1 perche bins = a n-1
    h = [0] * n             # creo lista h con lunghezza n 

    for x in a:
        i = 0
        
        while i < n-1 and x >= bins[i]:             
            i += 1                                  
       
        h[i] += 1
  
    return h

print(hist([90, 90, 90, 90], [1,2,3,4,5]))