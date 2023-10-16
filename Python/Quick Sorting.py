def quick_sort(seq):
    length = len(seq)
    if length <=  1:
        return seq
    else:
        # lets define a pivot element now...
        pivot = seq.pop()

    # creating a lower and greater sequence list...
    items_greater = []
    items_lower = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    # now the algorithm is applied to each of the item again and again...
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,3,7,2,56,85,38,32,87]))