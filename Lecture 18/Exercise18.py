# In[] Ricerca binaria correzione V1
def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = max(1, (lx+rx)//2)    #! cx viene scelto tra il massimo tra 1 e (lx+rx)//2
                                   #? quindi se (lx+rx)//2 è < di 1 cx sarè = a 1           
                # cx è il segmento mediano tra lx e rx

        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx-1
        else:
            lx = cx+1
    
    return cx

print( bin_search(1, [6, 8, 10] ) )
# In[] Ricerca binaria correzione V2
def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2           
                # cx è il segmento mediano tra lx e rx

        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k >= bins[cx]:
            # a sx del segmento cx
            lx = cx+1
        else:
            rx = cx-1
    
    return cx

print( bin_search(10, [6, 8, 10, 20] ) )
# In[] Implementazione ricerca binaria in esercizio L16
def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2           
                # cx è il segmento mediano tra lx e rx

        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k >= bins[cx]:
            # a sx del segmento cx
            lx = cx+1
        else:
            rx = cx-1
    
    return cx
def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in v < bins[0]
        - h[n-1] = numero di elementi in v >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    
    n = len(bins)+1 # un numero costante (rispetto a n e m) di operazioni
    h = [0]*n       # circa n operazioni
    
    for k in a:
        i = bin_search(k, bins) # O(log n)
        h[i] += 1
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([1, 3, -8, 10, 12, 9], [0, 10, 20, 30]) )

# Costo computazionale
#
# O(m*log n) caso peggiore o è fisso?


# %%
