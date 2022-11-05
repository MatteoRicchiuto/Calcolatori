'''
Esercizio per casa:
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