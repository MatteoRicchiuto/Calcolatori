'''
Esercizio per casa:
      Scrivere una funzione che prende in input due stringhe e restituisce il carattere della prima stringa che compare più volte nella seconda. 
      Ad esempio se la prima stringa è ciao e la seconda è ramarro marrone, la funzione deve restituire a.
'''

def lettera_pp (s1, s2):

    c_max = None
    n_max = 0
    n_test = 0

    for c1 in s1:
        n_test = 0
        if c1 in s2:
            for c2 in s2:
                if c1 == c2:
                    n_test += 1
            if n_test > n_max:
                n_max = n_test
                c_max = c1
    
    if c_max == None:
        print(f"Nessun carattere di {s1} si ripete in {s2}.")
    else:
        if n_max > 1:
            print(f"Il carattere di {s1} che si ripete più volte in {s2} è {c_max}, si ripete {str(n_max)} volte.")  # Stringa formattata è possibile aggiungere variabli alle stringe mettendole tra parentesi graffe
        else:
            print("Il carattere di " + s1 + " che compare più volte in " + s2 + " è " + c_max + ", si ripete " + str(n_max) + " volta.")




a = input("Inserisci la prima parola: ")
b = input("Inserisci la seconda parola: ")


lettera_pp(a, b)



