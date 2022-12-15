
def rem_none(list):
    '''
    Input una lista ed elimini da questa tutti gli elementi a valore None.
    '''
    i = 0
    
    while i < len(list):
        if list[i] == None:
            del(list[i])
    
        else: 
            i += 1
    
    return list

print(rem_none([1,2,3,None,None,5,6,None,7,None,None,None]))