
def prefix_sum(array):

    for i in range(1,len(array)):
        array[i]+=array[i-1]
    
    return array

array=list(map(int,input().split()))
print(prefix_sum(array))