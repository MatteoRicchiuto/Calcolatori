# In[]
def contaBirreRic(Birre_vuote, Birre, k):
    
    if Birre_vuote >=  k:
        
         Birre_omaggio = Birre_vuote // k
         Birre_vuote = Birre_vuote % k + Birre_omaggio
         Birre += Birre_omaggio
         
         
         return contaBirreRic(Birre_vuote, Birre, k)
    else:
       return Birre

def contaBirreMax(d,p,k):
    
    Birre = d // p
    Birre_vuote = Birre
    
    return contaBirreRic(Birre_vuote, Birre, k)

print(contaBirreMax(15,1,3))

# In[]
def contaBirreRic(Birre,k):
    
    if Birre >=  k:
      Birre_omaggio = Birre // k
      Birre= Birre % k + Birre_omaggio
      
      return Birre_omaggio + contaBirreRic(Birre,k)

    else:
        return 0
         

def contaBirreMax(d,p,k):
    
    Birre = d // p

    return Birre + contaBirreRic(Birre,k)

print(contaBirreMax(1000000,1000,10))



# %%    
