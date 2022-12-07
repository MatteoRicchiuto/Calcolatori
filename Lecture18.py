def list_to_str(word):
    for i in word:
        print(i,end=" ")
    print("\n")    
    
print("Gioco dell' impiccato")

secret_word = input("Digita la parola segreta: ")  # Successivamente prendere la parola in modo randomico da un file 

semi_word = ["_"] * len(secret_word) # La parola che verra stampata di volta in volta
 
                    # solo con le lettere indovinate ( al posto giusto )
                    
list_to_str(semi_word) # controllo

vite = 6 # Testa Corpo x2_Braccio x2_Gambe

while vite > 0 and semi_word.count("_") != 0:
    
    lettera = input("Inserisci una lettera: ")
    
    
        
        
    if lettera in secret_word:
        
        for i in range(len(secret_word)):
            if lettera == secret_word[i]:
                
                semi_word[i] = lettera
        list_to_str(semi_word)
    else:
        print("Lettera sbagliata")
        vite -= 1
        print("vite rimanenti: ", vite)
            
if vite:
    print("Bravo hai vinto :)")
else:
    print("Hai perso :(")
    

