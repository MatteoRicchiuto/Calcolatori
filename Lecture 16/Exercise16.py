# In[] Correzione Esercizio x Casa
def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    n = len(bins)+1     #! circa 3 operazioni elementari (costanti non auentono in base alla variabile)
    h =[0]*n            #! circa n operazioni

    for v in a:         #! tutte le operazioni del ciclo for si ripetono n volte
        # cerco il segmento v
        i = 0           #! numero costantre di operazioni(dipende da n ovvero da quante volte si ripete il ciclo for)
        
        while i < n-1 and v >= bins[i]:    #! nel caso peggiore n operazioni 
            i += 1      #! numero costantre (dipende da n ovvero da quante volte si ripete il ciclo for)
        h[i] += 1       #! numero costantre (dipende da n ovvero da quante volte si ripete il ciclo for)
        
    return h 
'''
# Costo computazionale:
    Il numero di operazioni eseguite è dato dal numero di volte in cui si esegue il
    ciclo for esterno (m volte) moltiplicato per il costo del blocco (n operazioni
    nel caso peggiore). In definitiva O(nm).
'''

print(hist([10,], [0, 10 , 2])) 

# %%

# all' esame ti verra chiesto il costo di una funzione qualsisi
