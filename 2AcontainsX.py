def arrayint(n,x):
    flag=False
    for i in n:
        if(i==x):
            flag=True
    return flag    
n=[5,8,2,1]
x=input("Enter the number")
print(arrayint(n,x))