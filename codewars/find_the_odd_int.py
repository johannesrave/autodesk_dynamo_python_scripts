def find_it(seq):
    int_dict = {}
    for num in seq:
        if num in int_dict:
            int_dict[num] += 1
        else:
            int_dict[num] = 1

    for k, v in int_dict.items():
        if v % 2 == 1:
            result = k
            break
    return result

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])