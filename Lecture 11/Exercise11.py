
# In[] Esercizzio Media incrementale v1
def media_incrementale(a):

    b = []
    for i in range(len(a)):
        b.append(sum(a[:i+1])/(i+1))
    return b

a = [1,2,3,4,5,6]
print( media_incrementale(a))

# In[] Esercizzio Media incrementale v2
      # Eviatre gli slicing
def my_sum(a,k):
    somma = 0
    for i in range(k):
        somma += a[i]
    return somma

def media_incrementale(a):

    b = []
    for i in range(len(a)):
        b.append(sum(a[:i+1])/(i+1))
    return b

a = [1,2,3,4,5,6]
print( media_incrementale(a))

# In[] Esercizzio Media incrementale v3
def my_sum(a,k):
    somma = 0
    for i in range(k):
        somma += a[i]
    return somma

def media_incrementale(a):

    b, somma = [], 0
    for i in range(len(a)):
        b.append((somma+a,[i])/(i+1))
    return b

a = [1,2,3,4,5,6]
print( media_incrementale(a))