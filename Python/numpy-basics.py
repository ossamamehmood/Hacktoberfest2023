import numpy as np
# law for indexing think of it as outer array, inner, inner
variable = np.array([1,2,3])
mulitdim_variable = np.array([[1,2,3,4], 
                              [9,8,7,6],
                              [2,4,6,8]])

print(variable)
print(mulitdim_variable)

# basic functions 
# 1. getting info about the variable
print('size of the item in np array ', variable.itemsize) #  
print('size of the item in np array ', mulitdim_variable.itemsize)
print()
print('data type of the element in np array ', variable.dtype)
print('data type of the element in np array ', mulitdim_variable.dtype)
print()
# total number of elements in the array
print('size of the np arrary ', variable.size)
print('size of the np arrary ', mulitdim_variable.size)
# dimension of the array
print('dimension of the array ', variable.ndim)
print('dimension of the array ', mulitdim_variable.ndim)
print()
print('shape of the array ', variable.shape)
print('shape of the array ', mulitdim_variable.shape)

print()
# 2. changing the shape and dimensions
variable_reshaped = variable.reshape(1,3)
mulitdim_variable_reshaped = mulitdim_variable.reshape(4, 3)
print('reshaped shape of the array ', variable_reshaped.shape, 'the diff is : ', variable_reshaped)
print('reshaped shape of the array ', mulitdim_variable_reshaped.shape)
print()

# multidimension to 1-D
mulitdim_variable_one_d = mulitdim_variable.ravel()
print('reshaped shape of the array ', mulitdim_variable_one_d.shape, 'the diff : ', mulitdim_variable_one_d)
print()

# test for any
bool_array = np.array([[True,True,False],
            [True, False, False],
            [True, True, False]])
num_array = np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
# you can pass boolean values to the array and print the desired values
print("test of any: ", bool_array.any(axis=1, keepdims=True)) # 0 - or operation between rows, 1 - or operation between columns
print(num_array[~(bool_array)])

# np.where ( condition, arry_value_when_condition_is_true, value to replace other )
arr = np.array([1,2,3,4,5,1,2,3,4,5])
print('where in action: ', np.where(arr <=2, arr, 0))