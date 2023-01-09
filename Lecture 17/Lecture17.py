# In[] Funzione tuple
t = (1,2,3,4,5)
l = tuple(t)        # Trasforma una lista in una tupla
                    # Costo lineare (dipende dalla lunchezza dela tupla)

# In[] Ricerca binaria 

#? L'algoritmo cerca un elemento all'interno di un array che deve necessariamente essere ordinato in ordine crescente
#? Non usa mai più di ⌈ log 2 ⁡ N ⌉
#? Impiega sempre lo stesso tempo su uno stesso array per cercare elementi anche in posizioni diverse
#? Almeno che l'elemento non si trovi al centro dell'array o agli estremi

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
        cx = lx+rx//2          
                # cx è il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx-1
        else:
            lx = cx+1
    
    return cx

print( bin_search(6, [6, 8, 10] ) )
#! non funziona con istanze molto piccole
#! contralla lecture 18, exercise per vedere la soluzione

# In[] Ricerca binaria V2

def bin_search(k, bin):
    n = len(bin)

    lx = 0
    rx = n-1
    trovato = False

    while not trovato:
        cx = (lx+rx)//2
        
        if k > cx:
            lx = cx

        elif k < cx:
            rx = cx 

        else:
            return cx

print(bin_search(8,(1,2,3,4,5,6,7,8,9,10)))
# %%
