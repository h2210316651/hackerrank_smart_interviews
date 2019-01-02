import math 
  

def Log2(x): 
    return (math.log10(x) / 
            math.log10(2)); 
  

def check_power(n): 
    return (math.ceil(Log2(n)) == 
            math.floor(Log2(n))); 
  
t=int(input())
a=[]
for i in range(t):
    x=int(input())
    if(x==0):
        break
    else:
        a.append(check_power(x))
for i in range(t):
    if(a[i]):
        print('True')
    else:
        print('False')
