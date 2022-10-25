# In[] Slicing
x = input("inserisci una stringa: ")

x0 = x[1:4] # le lettere dalla 1 alla 4
x1 = x[:4] # lettere dalla prima alla 4
x2 = x[3:] #lettere dalla 3 all'ultima 
x3 = x[:] #tutte le letterere
x4 = x[3:8:2] #le lettere tra 3 e 8 ma con intervalli di due
x5 = x[6:1:-1] #le letter dalla 6 alla 1 ma in ordine inverso
x6 = x[::-1] #inverte tutta la stringa


print(x0)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)