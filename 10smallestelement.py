def smallest_num_in_array(x):
    min=x[0]
    for i in x:
        if i<min:
            min=i
    return min
x=[5,8,1,9]
print(smallest_num_in_array(x))