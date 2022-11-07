# In[] stringa in stinga Variabili buleane

s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")


i2, trovato = 0, False
while i2 <= len(s1)-len(s2) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(s2) and s1[i2+i1] == s2[i1]:
        i1 += 1
    if not (i1 < len(s2) ):
        print(s2 + ' compare in posizione ' + str(i2) + ' di ' + s1)
        trovato = True
        
    i2 += 1
    
if not trovato:
    print('non esiste corrispondenza')
    

# In[] Stringa in stringa Break v1

s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")


i2, trovato = 0, False
while i2 <= len(s1)-len(s2) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(s2) and s1[i2+i1] == s2[i1]:
        i1 += 1
    if not (i1 < len(s2) ):
        trovato = True
        break # esce dal ciclo più interno
    i2 += 1
    
if not trovato:
    print('non esiste corrispondenza')
else:
    print(s2 + ' compare in posizione ' + str(i2) + ' di ' + s1)
    
    
# In[] Stringa in stringa Break v2

s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")


i2 = 0
while i2 <= len(s1)-len(s2): # modificato tenendo conto che possa aver successo...
    # verifico se string2 è in string1 a partire da i1
    i1 = 0
    while i1 < len(s2) and s1[i2+i1] == s2[i1]:
        i1 += 1
    if not (i1 < len(s2) ):
        break # esce dal ciclo più interno
    i2 += 1
    
if not (i2 <= len(s1)-len(s2)):
    print('non esiste corrispondenza')
else:
    print(s2 + ' compare in posizione ' + str(i2) + ' di ' + s1)


# In[] stringa in stringa Slicing
s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")

i, trovato = 0, False
k = len(s2)

while i <= len(s1)-len(s2):
    if s1[i:k] == s2:
        trovato = True
        break
    else:
        i += 1
        k = len(s2) + i

if trovato == True:
    print("la stringa 2 è presente nella stringa una in posizione " + str(i) + ".")
else:
    print("Non c'è corrispondenza.")

# In[] stringa in stringa Slicing con semplificazione del prof
s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")

i, trovato = 0, False

while i <= len(s1)-len(s2):
    if s1[i:len(s2) + i] == s2:
        trovato = True
        break
    i += 1

if trovato:
    print("la stringa 2 è presente nella stringa una in posizione " + str(i) + ".")
else:
    print("Non c'è corrispondenza.")