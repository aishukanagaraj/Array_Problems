def largest_num_in_array(x):
    max=x[0]
    for i in x:
        if i>max:
            max=i
    return max
x=[5,8,1,9]
print(largest_num_in_array(x))