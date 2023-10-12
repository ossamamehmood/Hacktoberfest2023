# Python code to remove duplicate elements
def rem(list1):
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list

list1=[1,2,3,4,5,2,3]
print(rem(list1))


'''
# Python code to remove duplicate elements other way
list1=[1,2,3,4,5,2,3]
list1=list(set(list1))
print(list1)
'''
