def shortest_steps_to_num(num):
    cur = 1
    count = 0
    while 2 * cur < num:
        cur *= 2
        count += 1
        print('Duplicating, new number is ', cur)
    while cur < num:
        cur += 1
        count += 1
        print('Adding, new number is ', cur)
    print (count)
    return count

shortest_steps_to_num(12)    