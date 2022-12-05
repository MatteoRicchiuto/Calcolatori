# In[] Ricerca binaria 

def bin_search(k, bins)
    '''
    sia n-1 la lunghezza di bins, 
    ritorna: 
            0 se k < bins[0],
            n se k >= bin[n-2]
            i se bins[i-1] <= k < bin[i]
    '''
    lx, rx = 0, n-1
    n = len(bins)+1
    
    while True:            # Ciclo teoricamente infinito
        cx = (lx + rx)//2
        # cx è il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            return cx
        
        elif k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx -1

        else: 
            lx = cx + 1''''0'0'''' 