'''
Esercizo per casa:
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
'''

def hist( a, bins ):
    n = len(bins) + 1             #! Costante (non cambia al variare delle varianìbili)
    h = [0] * n                   #! Circa n 

    for x in a:                             #? Blocco ripetuto m volte
        i = 0                               #! Costante
        
        while i < n-1 and x >= bins[i]:             #? Blocco ripetuto n volte (nel caso peggiore)
            i += 1                                  #! Costante
       
        h[i] += 1                           #! Costante
  
    return h                      #! Costante

print(hist([90, 90, 90, 90], [1,2,3,4,5]))

#  c = costante 
#! Costi:
#       c + c + m(c + n(c)+ c) + c   #* Si rinuovono tutte le costanti
#       m(c + nc + c)
#       mc + mnc + mc   
#       m + mn +  c                  #* Si rimuovono tutte le costanti moltiplicative 
#       mn                           #* Scegliamo soltato l'elemento di ordine di grandezza superiore  
#!      O(nm)

