def sort_array(l1):
    size = len(l1)
    
    l3 = [None] * size
    
    small = l1[0]
        
    for i in range(size):  
        if (small>=l1[i]):
            
            small = l1[i]
            
    print(f"smallest number in array is {small}")               
    return 0

print(sort_array([24,32,6,23,7,98,12,21,23,7,8,1,5,9,32]))