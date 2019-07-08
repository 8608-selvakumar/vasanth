char = 256
def max_distinct_char(str1, n): 
    count = [0] * char 
    for i in range(n): 
        count[ord(str1[i])] += 1
    max_distinct = 0
    for i in range(char): 
        if (count[i] != 0): 
            max_distinct += 1    
    return max_distinct 
  
def smallestest_Substr(str1): 
  
    n = len(str1)
    max_distinct = max_distinct_char(str1, n) 
    minl = n
    for i in range(n): 
        for j in range(n): 
            subs = str1[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = max_distinct_char(subs,subs_lenght)
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 

if __name__ == "__main__": 
    str1=input()
    l = smallestest_Substr(str1); 
    print( " maximum distinct", 
           "characters :", l) 
