def mode_arrray(array):
    mode=0
    count=0
    maxcount=0
    for i in array:
        count=0
        for j in array:
            if i==j:
                count+=1
            
        if count>maxcount:
            maxcount=count
            mode=i

    return mode
array=[5,8,6,8,8,6,9]
print(mode_arrray(array))