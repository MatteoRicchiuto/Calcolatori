
# In[] Retudr di una funzione
def g(x, y):
    return 0 if x < y else 1

def f(k):
    n = k**2
    return g(n, k)

print(f(9))

# In[] Funzione Ricorsiva
def f(n):
    if n == 0:
        return 0
    else:
        return 1+f(n-1)
   
k = 2
print(f(k))
# In Esercizio Funzione ricorsiva
def max_list(a):
	'''
		Input: lista di numeri
		Output: il numero piu grande
			La funzione deve essere ricorsiva
        	non si deve usare la funzione max
	'''
	n = len(a)
	if n == 1:
		return a[0]
	else:
		x = max_list(a[1:])
		if a[0] > x:
			return a[0]
		else:
			return x

print(max_list([1,2,3,4,5,6,7,8,9]))