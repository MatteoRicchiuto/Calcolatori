
def count_int(l):
    '''
    Input: lista che può contenere liste annidate 
    output: il numero di 'int' nella lista e in tutte le sottoliste annidate.
    '''

    c = 0
    for x in l:
        if type(x) is int:
            c += 1
            
        elif type(x) is list:
            c += count_int(x)
    return c


print(count_int([3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3]]))


def deep_count(l):
    '''
    Input: una lista o una tupla
    Output: il numero di 'int', 'float', 'str', 'bool' e 'None' in a ed in tutte
        le sue sottoliste o sottotuple annidate
    '''

    c = 0
    for x in l:
        if type(x) in (int, float, str, bool, bool, type(None)):
            c += 1
            
        elif type(x) in (list, tuple):
            c += deep_count(x)
    return c

print(deep_count([2,[True,[1,2.1],None],'94',(12,[None,['tre',[4,['1']],[False,[4,5]]]]),0]))