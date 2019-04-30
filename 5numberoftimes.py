def num_of_times(array,x):
    count=0
    for i in array:
        if i==x:
            count+=1
    return count
array=[5,5,8,8,9,9,9,6]
x=input("Enter the number")
print(num_of_times(array,x))
