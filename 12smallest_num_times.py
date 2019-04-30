def smallest_num_in_array(x):
    min1=x[0]
    count=0
    for i in x:
        if i<min1:
            i=min1
            count+=1
    return count
x=[5,8,1,9,1,1,1,1,1]
print(smallest_num_in_array(x))