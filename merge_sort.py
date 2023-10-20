def merge_sort(arr):
    brr = []
    if( len(arr) == 1):
        return arr;
    half  = len(arr) / 2
    lower = merge_sort(arr[:half])
    upper = merge_sort(arr[half:])
    lower_len = len(lower)
    upper_len = len(upper)
    i = 0
    j = 0
    while i != lower_len or j != upper_len:
        if( i != lower_len and (j == upper_len or lower[i] < upper[j])):
            brr.append(lower[i])
            i += 1
        else:
            brr.append(upper[j])
            j += 1

    return brr;

arr = [4, 2, 3, 8, 8, 43, 6,1, 0]
ar = merge_sort(arr)
print " ".join(str(x) for x in ar)
