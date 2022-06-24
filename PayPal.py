def Paypal(st,n):

   
    if n == 1:
        return(st)
    
    result = ""
   
    step = 2 * n - 2
    
    for i in range(0, n):
       
        for j in range(i, len(st), step):
            result += st[j]
            if i != 0 and i != n - 1 and (j + step - 2 * i) < len(s):
                result += st[j + step - 2 * i]
    return(result)