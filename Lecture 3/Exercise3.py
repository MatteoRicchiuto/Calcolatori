'''
Esercizio per casa:
      Scrivere una funzione che prende in input due stringhe e restituisce il carattere della prima stringa che compare più volte nella seconda. Ad esempio se la prima stringa è ciao e la seconda è ramarro marrone, la funzione deve restituire a.
'''

'''
giovanni 
c = i
 
cannibbale

i 1
a 2
n 2
'''

def lettera_pp (s1, s2):

    lettera = "n"
    numero1 = 0
    numero2 = 0

    for c in s1:
        if c in s2:
            for d in s2:
                if c == d:
                    numero1 =+ 1
                if numero2 > numero1:
                    numero1 = numero2
                    lettera = c
    print(lettera)
    print(numero1)

a = "giovanni"
b = "cannibbale"

lettera_pp(a, b)



