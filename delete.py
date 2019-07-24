import math
num=int(input(""))
n=int(input("")) 
def deleteno(num, n): 
    d = (math.log10(num) + 1) 
    rev_new_num = 0 
    i = 0 
    while (num != 0): 
  
        digit = num % 10 
        num = int(num / 10) 
  
        if (i != (int(d) - n)): 
            rev_new_num = ((rev_new_num * 10) +
                                        digit) 
        i += 1 
    new_num = 0
    i = 0 
    while (rev_new_num != 0): 
  
        new_num = ((new_num * 10) + 
                   (rev_new_num % 10)) 
        rev_new_num = int(rev_new_num / 10)
        i += 1 
  
    return new_num 
  

print(deleteno(num, n)) 
  
