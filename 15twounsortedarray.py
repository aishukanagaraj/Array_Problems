def two_unsorted_array(array1,array2):
    if (len(array1)==len(array2)):
        return True
    for i in array1:
        for j in array2:
            if not(array1[i]==array2[j]):
                return False

    return False
array1=[2,1,0,5,8]
array2=[2,1,0,5,8]
print(two_unsorted_array(array1,array2))
    
