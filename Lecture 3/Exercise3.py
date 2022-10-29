'''
Esercizio per casa:
      Scrivere una funzione che prende in input due stringhe e restituisce il carattere della prima stringa che compare più volte nella seconda. 
      Ad esempio se la prima stringa è ciao e la seconda è ramarro marrone, la funzione deve restituire a.
'''

def lettera_pp (s1, s2):

    lettera = "*"
    numero_test = 0
    numero_mem = 0


    for c in s1:
        numero_test = 0
        if c in s2:
            for d in s2:
                if c == d:
                    numero_test += 1
                if numero_test > numero_mem:
                    numero_mem = numero_test
                    lettera = c
    
    if lettera == "*":
        print("Nessun carattere di " + s1 + " si ripetecazzo in " + s2 + ".")
    else:
        if numero_mem > 1:
            print("Il carattere di " + s1 + " che compare più volte in " + s2 + " è " + lettera + ", si ripete " + str(numero_mem) + " volte.")
        else:
            print("Il carattere di " + s1 + " che compare più volte in " + s2 + " è " + lettera + ", si ripete " + str(numero_mem) + " volta.")




a = input("Inserisci la prima parola: ")
b = input("Inserisci la seconda parola: ")


lettera_pp(a, b)



