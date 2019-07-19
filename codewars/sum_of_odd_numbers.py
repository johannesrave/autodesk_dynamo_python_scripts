import cProfile

def row_sum_odd_numbers(n):
    first = n + (n-1)**2
    last = first + n*2
    return sum(range(first, last, 2))
    
cProfile.run('row_sum_odd_numbers(3)', None, 1)
print(row_sum_odd_numbers(2))
