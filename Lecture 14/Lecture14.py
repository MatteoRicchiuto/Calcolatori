
# In[] Correzione Esercizio x Casa
def deep_count(a):
    '''
    InPut: Una lista che può contenere liste annidate.
    OutPut: Il numero di Int nella lista e in tutte le sottoliste annidate che questa contiene.
    '''
    c = 0
    for x in a:
        if type(x) == int:
            c += 1 
        elif type(x) == list:
            c += deep_count(x)
    return c

a = [3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3]]
print(deep_count(a))
    
# In[] 
def deep_count(a):
    '''
    InPut: Una lista che può contenere liste annidate.
    OutPut: Il numero di Int, Float, Str, Bool nella lista e in tutte le sottoliste annidate che questa contiene.
    '''
    c = 0
    for x in a:
        if type(x) == int, float, str, bool, type(None):
            c += 1 
        
        elif type(x) == list:
            c += deep_count(x)
    
    return c

a = [3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3]]
print(deep_count(a))

# In[] 
def deep_count_clone(a):
    b = []
    for x in a:
        if type(x) == list:
            b.append(deep_count_clone(x))
        else:
            b.append(x)
        return b

a = [3, [9.13, ["ciao",5], 2], 10, [None, [4,], [1,2], 3]]
print(deep_count_clone(a))

# In[]
import os

cartella = (os.listdir())

for x in cartella:
    if os.path.isdir(x):
        print(f"DIR:{x}")
    elif os.path.isfile(x):
        print(f"FILE:{x}")
# In[]
import os
def browse_dir(d):
    
    cartella = (os.listdir(d))

    for x in cartella:
        if os.path.isfile(x):
            print(f"FILE:{x}")
        elif os.path.isdir(x):
            browse_dir(x)

browse_dir(os.getcwd())

# %% 