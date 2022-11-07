# In[] Docstring e return multipli
def massima_intersezione( x, y ):
    '''
    Input: x ed y sono due stringhe
    Output: restituire il carattere in x che è il più frequente in y e la
        sua frequenza
    '''
    n_max, c_max = 0, None # unpacking
    for c in x:
        # conta il numero di volte in cui c compare in y
        n_c = 0
        for c_y in y:
            if c_y == c:
                n_c += 1
        if n_c > n_max:
            n_max, c_max = n_c, c
    return c_max, n_max
    
a, b = 'ciao', 'ramarro marrone'
c, n = massima_intersezione( a, b ) # unpacking
print(c, n)
    
# In[] Funzioni con numero variabile di argomenti

def f( *args ):
    for a in args:
        print(a)
        
f('ciao', 9, 'python', 3.14, True)

# In[] Astrazione e modularità

def radice_quadrata( x, eps=0.01 ):
    # prima ipotesi
    g = x/2
    
    while abs( g*g - x ) > eps: # questo e' un ciclo
        g = 0.5 * ( g + x/g )

    return g

# attenzione se si modifica una implementazione di una funzione, per garantire
# la compatibilià l'interfaccia non deve essere mutata

def radice_quadrata(x, eps=10):
    return x**0.5

print(radice_quadrata(20, 0.000001))
print(radice_quadrata(20))
print(radice_quadrata(eps=0.000001, x = 90))