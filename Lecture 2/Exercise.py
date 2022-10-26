# In[] stringa in stinga Variabili buleane

string1 = input("inserisci la stringa 1: ")
string2 = input("inserisci la stringa 2: ")


i2, trovato = 0, False
while i2 <= len(string1)-len(string2) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(string2) and string1[i2+i1] == string2[i1]:
        i1 += 1
    if not (i1 < len(string2) ):
        print(string2 + ' compare in posizione ' + str(i2) + ' di ' + string1)
        trovato = True
        
    i2 += 1
    
if not trovato:
    print('non esiste corrispondenza')
    

# In[] Stringa in stringa Break v1

string1 = input("inserisci la stringa 1: ")
string2 = input("inserisci la stringa 2: ")


i2, trovato = 0, False
while i2 <= len(string1)-len(string2) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(string2) and string1[i2+i1] == string2[i1]:
        i1 += 1
    if not (i1 < len(string2) ):
        trovato = True
        break # esce dal ciclo più interno
    i2 += 1
    
if not trovato:
    print('non esiste corrispondenza')
else:
    print(string2 + ' compare in posizione ' + str(i2) + ' di ' + string1)
    
    
# In[] Stringa in stringa Break v2

string1 = input("inserisci la stringa 1: ")
string2 = input("inserisci la stringa 2: ")


i2 = 0
while i2 <= len(string1)-len(string2): # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(string2) and string1[i2+i1] == string2[i1]:
        i1 += 1
    if not (i1 < len(string2) ):
        break # esce dal ciclo più interno
    i2 += 1
    
if not (i2 <= len(string1)-len(string2)):
    print('non esiste corrispondenza')
else:
    print(string2 + ' compare in posizione ' + str(i2) + ' di ' + string1)


# In[] stringa in stringa Slicing
string1 = input("inserisci la stringa 1: ")
string2 = input("inserisci la stringa 2: ")

i, trovato = 0, False
k = len(string2)

while i <= len(string1)-len(string2):
    if string1[i:k] == string2:
        trovato = True
        break
    else:
        i += 1
        k = len(string2) + i

if trovato == True:
    print("la stringa 2 è presente nella stringa una in posizione " + str(i) + ".")
else:
    print("Non c'è corrispondenza.")

# %%
