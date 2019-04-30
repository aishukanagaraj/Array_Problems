def more_than_once(array,x):
    flag=False
    count=0
    for i in array:
        if i==x:
            count+=1
            if count>1:
                flag=True
    return flag
array=[5,2,2,7,8,5,6]
x=input("Enter the value:")
print(more_than_once(array,x))


