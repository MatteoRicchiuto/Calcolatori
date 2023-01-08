# In[] Funzione tuple
t = (1,2,3,4,5)
l = tuple(t)        # Trasforma una lista in una tupla
                    # Costo lineare (dipende dalla lunchezza dela tupla)

# In[] Ricerca binaria 
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
    
    lx, rx = 0, n
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2             
                # cx è il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx-1
        else:
            lx = cx+1
    
    return cx

print( bin_search(9, [6, 8, 10] ) )
# In[] Ricerca binaria V2

def bin_search(k, bin):
    n = len(bin)

    lx = 0
    rx = n
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
