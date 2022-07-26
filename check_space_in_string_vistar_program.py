ipt = "Enter your name your name your name y     n n yyyyy n n n n n"

def string_check(ipt):
    
    count =0
    for i in range(len(ipt)):
        
        if (ipt[i]=='y'):
            j=i
            
            while j <len(ipt):
                 
                if(ipt[j]=='n'):
                    if((j-i)==5):
                        count=count+1
                j=j+1
    
    if (count == 0):
        return False

    else:
        print(count)
        return True
    
print(string_check(ipt))