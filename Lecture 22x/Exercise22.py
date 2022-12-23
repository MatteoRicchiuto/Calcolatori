# In[]Corezzione esercizio per casa lezione 20
'''
Si progetti ed implementi una funzione che prenda in input due liste di numeri ordinati 
in modo crescente e restituisca una nuova lista contenente tutti gli elementi delle liste 
in input ordinati dal più piccolo al più grande.
'''
def merge(a, b):
    '''a,b : liste di interi ordinati secondo la relazione <=
    
    Rerurns: una lista c contenete gli elementi di a e b ordinati se condo la realazionr <=
    '''
    c = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else: 
            c.append(b[j])
            j += 1

    if i == len(a):
        c.extend(b[j:])
    else:   
        c.extend(a[i:])
    return c

L0 = [1,5,9,10,11,20,23]
L1 = [0,1,2,10,12,20,21,23,24,29]

M = merge(L0, L1)
print(M)
# In[] v2

#! rimuoviamo lo slicing (che è costoso dal punto di vista della memoria utlizzata)
#! al costo della legibilità
def merge(a, b):

    c = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else: 
            c.append(b[j])
            j += 1
    
    if i == len(a):
        t, k = a, i
    else:
        t, k = a, i
    while k < len(t):
        c.append(t[k])
        k += 1
    return c

L0 = [1,5,9,10,11,20,23]
L1 = [0,1,2,10,12,20,21,23,24,29]

M = merge(L0, L1)
print(M)
# %%
