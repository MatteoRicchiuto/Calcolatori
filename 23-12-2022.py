def fattoriale(n):

    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)

print(fattoriale(5))

# In[] Ex2 Funzione Unica
def Hailstone_sequence(n, l = [], i = 0):

    if n == 1 and i == 0:
        l = [1]
        return l 
    
    elif n != 1 and i == 0:
        i += 1
        l.append(n)
        return Hailstone_sequence(n,l,i) 

    elif n == 1 and i != 0:
        i += 1
        return l
   
    elif n % 2 == 0:
        i += 1
        n = int(n/2)
        l.append(n)
        return Hailstone_sequence(n,l,i) 

    elif n % 2 == 1:
        i += 1
        n = int(n*3+1)
        l.append(n)
        return Hailstone_sequence(n,l,i) 

print(Hailstone_sequence(6))

# In[] Ex2 Funzione Unica (correzione Prof)
def Hailstone_sequence(n, l = []):
    l.append(n)

    if n == 1:
        return l

    elif n % 2 == 0:
        n = int(n/2)
        return Hailstone_sequence(n,l) 

    elif n % 2 == 1:
        n = int(n*3+1)
        return Hailstone_sequence(n,l) 

print(Hailstone_sequence(1))

# In[] Ex3 controllo se una frase è palindroma
def palin(p):
    p = p.lower()
    p = p.replace(" ","")
    p = p.replace("'","")
    p = p.replace(".","")
    p = p.replace(",","")
    
    return palin1(p)

def palin1(p):
    
    if len(p) <= 1:
        return True

    elif p[0] == p[len(p)-1]:
        p = p[1:len(p)-1]
        return palin(p)
    
    else:
        return False

print(palin("Ai lati d'italia"))

# %%
