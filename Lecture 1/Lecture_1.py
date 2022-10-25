# In[] Conta Vocali Pare V1
parola = input("Inserisci una parola: ")
L_parola = len(parola)

i = 1
N_vocali = 0
vocali = "aeiouyAEIOUY"

print("La parola " + parola + " è lunga " + str(L_parola) + " lettere")

while i < L_parola:
    if i % 2 == 0:                      # %
       if parola[i] in vocali:
         N_vocali += 1
    i +=1

print("La parola " + parola + " è composta da " + str(N_vocali) + " vocali.")




# In[] Conta Vocali Pare V2
parola = input("Inserisci una parola: ")
L_parola = len(parola)

i = 1
N_vocali = 0
vocali = "aeiouyAEIOUY"

print("La parola " + parola + " è lunga " + str(L_parola) + " lettere")

while i < L_parola:
    if i % 2 == 0 and parola[i] in vocali:
         N_vocali += 1
    i = i + 1

print("La parola " + parola + " è composta da " + str(N_vocali) + " vocali.")




# In[] Conta Vocali Pare V3 (ciclo for)
parola = input("Inserisci una parola: ")
L_parola = len(parola)

N_vocali = 0

print("La parola " + parola + " è lunga " + str(L_parola) + " lettere")

for c in parola:
    if c in "AEIOUYaeiouy":
        N_vocali += 1

print("La parola " + parola + " è composta da " + str(N_vocali) + " vocali.")




# In[] Sottolinea Vocali
parola = input("Inserisci una parola: ")
L_parola = len(parola)

N_vocali = 0
sottolineatura = ""
    

print("La parola " + parola + " è lunga " + str(L_parola) + " lettere")

for c in parola:
    if c in "aeiouyAEIOUY":
        N_vocali += 1
        sottolineatura += "*"
    else: 
        sottolineatura += " "

print("La parola " + parola + " è composta da " + str(N_vocali) + " vocali.")
print(parola)
print(sottolineatura)


