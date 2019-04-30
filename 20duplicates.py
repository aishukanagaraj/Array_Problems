def duplicate_rmv_array(array):
    x=[]
    duplicate_removed=[]
    for x in array:
        if not(duplicate_removed==x):
            print duplicate_removed
    
array=[6,6,2,1,1,4,5,5]
print(duplicate_rmv_array(array))