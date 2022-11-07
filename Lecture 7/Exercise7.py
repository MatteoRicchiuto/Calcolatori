'''
Esercizio per casa:
    Scrivere una funzione che riceva in input un intero `n` e
    restituisca un `float` (pseudo)-casuale compreso tra 0 ed 1 composto da `n` cifre decimali dopo la virgola. 
'''
import random as rn

def r_float( n ):
 
    str_f = '0.'
    for c in range(n-1):
        # n-1 caratteri in 0...9
        str_f += str(rn.randint(0, 9))
    # l'ultimo carattere non deve essere 0
    str_f += str(rn.randint(1, 9))
    return float(str_f)

print(r_float(20))
    

    
    