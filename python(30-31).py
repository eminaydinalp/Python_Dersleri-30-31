# Modüller (30.Ders)

import random
import math

for i in range(10):
    
    print(random.random())
    
    
random.randint(1, 50)

for i in range(50):
    
    print(random.randint(1, 50))
    
liste = [1,2,34,5,325,5,23,5]

random.choice(liste)

math.factorial(5)

# Ödev Çözüm (31.Ders)
def faktoriyel(x):
    
    sayi = 1
    
    if x == 1 or x == 0:
        
        print("Faktoriyeli : ", sayi)
        
    else:
        
        while(x >= 1):
            
            sayi *= x
            x -= 1
            
        print("Faktoriyeli : ", sayi)
        
faktoriyel(5)
faktoriyel(6)



































        
        
    
    
    
    
    






        










































# 1. Ödev
# 2. Kendi Modülümüzü Yapma    
# 3. Sayi Tahmin Oyunu












































