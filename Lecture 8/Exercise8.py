# In[] Esercizzio in classe: stampa verticale
def print_v( *strings ):
    '''
    Input: un numero variabile di stringhe
    Stampa le stringhe in verticale, uno di fianco l'altra
    Restituisce: None
    
    Esempio print_v('ciao', 'python')
    
    cp
    iy
    at
    oh
     o
     n
    '''    
    
    r = 0 # numero di riga
    terminato = False
    while not terminato:
        terminato = True
        # definiamo la riga r
        riga_r = ''
        for a in strings:
            if len(a) > r:
                riga_r += a[r]
                terminato = False
            else:
                riga_r += ' '
        if not terminato:
            print(riga_r)
        r += 1
        
print_v('ciao', 'python', 'programmazione', 'java', 'c++')


# In[] Esercizio per casa: Quantità di numeri in determinati insiemi
'''
     Dati 3 segmenti adiacenti ed n float si vuole calcolare quanti degli n float ricadono in ogni segmento. 
     I segmenti sono rappresentati da 2 float h0 e h1 che definiscono i segmenti: (-∞, h0), [h0, h1), [h1, ∞]. 
     Si progetti una funzione che prenda in input la descrizione di 3 segmenti (h0 e h1) e un numero variabile di float e restituisca 
     una terna di interi che rappresenta il numero di float che ricade in   ciascuno dei 3 segmenti.

               Ad esempio se l'input della funzione fosse -7, 5, 3, 10, -4, 5, -12, 6, 0, 
               i segmenti sono: i numeri minori di -7; i numeri compresi tra -7 e 5 (escluso); i numeri maggiori-uguali a 5. 
               
               I valori -12 e -7 fanno parte del primo segmento; 
               
               3 e 0 fanno parte del secondo segmento; 
               
               10, 5 e 6 fanno parte del terzo segmento. 
               
               Quindi la funzione dovrebbe restituire la terna: 2, 2, 3

               Suggerimento La funzione abbia la seguente intestazione

               def hist(h0, h1, *numbers)

               dove numbers rappresenta il numero variabile di float
'''

def hist(h0, h1, *numbers):
   
    s1, s2, s3 = "", "", ""
    
    numbers_x = ""
    
    for c in numbers:
        i = 0
        for k in numbers:
        
            if c == k:
                i += 1
            
        if i <= 1 :
               
            if c < h0:
                s1 += str(c) + ", "
                
            if h0 <= c and c < h1:
                s2 += str(c) + ", " 
                    
            if c >= h1:
                s3 +=str(c) + ", " 

        else:
            if str(c) not in numbers_x:
                numbers_x += str(c)

    for c in numbers_x:
    
        if int(c) <= h0:
            s1 += str(c) + ", "
                
        if h0 <= int(c) and int(c) < h1:
            s2 += str(c) + ", " 
                    
        if int(c) >= h1:
            s3 +=str(c) + ", "       
    
    print(f"{s1} sono minori di {h0}.")
    print()
    print(f"{s2} sono compresi tra {str(h0)} e {str(h1)}.")
    print()
    print(f"{s3} sono maggiori di {h1}.")
    

hist(-7, 5, -7, 5, 3, 10, -4, 5, -12, 6, 0)

# In[] versione del prof
def hist(h0, h1, *numbers):
    seg0, seg1, seg2 = 0, 0, 0
    for x in numbers:
        if x < h0:
            seg0 += 1
        elif x < h1:
            seg1 += 1
        else:
            seg2 += 1
    return seg0, seg1, seg2