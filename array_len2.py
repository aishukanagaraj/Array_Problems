#refactoring 2 - code for array integer
def arr_len(a):
    count=0
    while(a[count:]):
        count+=1
    return count
a=[2,45,85,6]
print(arr_len(a))