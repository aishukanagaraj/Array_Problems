def loc_of_array_value(array,x):
    index=0
    count=0
    for i in array:
        if i==x:
            index=count
        count+=1
    return index
array=[5,8,6,4,7]
x=input("Enter the value")
print(loc_of_array_value(array,x))