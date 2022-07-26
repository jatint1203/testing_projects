def sort_array(l1):
    size = len(l1)

    small = l1[0]
    temp=0
        
    for i in range(size):   
        for j in range(i+1,size):  
            if (l1[i]>=l1[j]):
                
                temp = l1[i]
                l1[i] = l1[j]
                l1[j]=temp
                
                
                small = l1[j]
    print(l1)

    return 0

print(sort_array([24,32,6,23,7,98,12,21,23,7,8,1,5,9,32]))