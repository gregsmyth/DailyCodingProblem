# Given an array of integers, return a new array such that 
# each element at index i of the new array is the product of 
# all the numbers in the original array except the one at i.

# For example, 
# if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?



def product_exclude_current_easy(num_lst):
    product = 1
    new_num_lst = []

    if len(num_lst) > 1:
        for i in num_lst:
            product = product * i

        for j in num_lst:
            if j != 0:
                new_num = product / j
            else:
                new_num = float("nan")
            new_num_lst.append(new_num)

    return new_num_lst



def product_exclude_current_hard(num_lst):
    new_num_lst = []

    if len(num_lst) > 1:
        for i in range(len(num_lst)):
            skip_lst = []
            skip_lst = num_lst[0:i]
            if i < len(num_lst)-1:
                skip_lst = skip_lst + num_lst[i+1:len(num_lst)]
            product = 1
            for j in skip_lst:
                product = product * j
            new_num_lst.append(product)

    return new_num_lst
        