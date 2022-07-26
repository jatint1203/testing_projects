l1 = [1,5,6,3,9,10,12,15,56,78]
l2 = [1,2,3,4,5,9,12,24,67]


def sort_arr(l1, l2, n1, n2):
    l3=[None] * (n1 + n2)
    j=0
    k=0
    i=0 
    print(n1, n2)
    
    while i<n1 and j<n2:
        
        if(l1[i] < l2[j]):
            l3[k] = l1[i]
            i=i+1
            k=k+1
            
        else:
            l3[k] = l2[j]
            j=j+1
            k=k+1
        
    while i < n1:
        l3[k] = l1[i]
        k=k+1
        i=i+1
        
        
        
    while j<n2:
        l3[k] = l2[j]
        k=k+1
        j=j+1
        
         
        
    print(l3)

print(sort_arr(l1,l2, len(l1), len(l2)))
