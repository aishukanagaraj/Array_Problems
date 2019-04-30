def largest_num_in_array(x):
    max=x[0]
    for i in x:
        if i>max:
            max=i
    return max


def largest_num_in_times(x):
    count=0
    for i in x:
        if (largest_num_in_array(x)==i):
            count+=1
    return count
x=[5,9,9,9,1]
print(largest_num_in_times(x))