
s1 = input("inserisci la stringa 1: ")
s2 = input("inserisci la stringa 2: ")
k = input("inserisci lvalore buleano: ")

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
'''
if not trovato:
    print('non esiste corrispondenza')
else:
    print(s2 + ' compare in posizione ' + str(i2) + ' di ' + s1)
'''
Print("non esiste corrispondenza") if not trovato elif trovato and k = true print(s2 + ' compare in posizione ' + str(i2) + ' di ' + s1)