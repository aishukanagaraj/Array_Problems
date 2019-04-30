def indexarray(n,x):
    index=-1
    count=0
    for i in n:
        if(i==x):
            index=count
            break
        count+=1
    return index
n=[2,8,4,6,5]
x=input("Enter the number")
print(indexarray(n,x))
        