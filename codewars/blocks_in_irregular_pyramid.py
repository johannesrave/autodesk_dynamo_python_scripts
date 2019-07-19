import cProfile

def num_blocks(w, l, h):
    blocks_per_layer = 0
    for i in range(h):
        blocks_per_layer = blocks_per_layer + (w*l)
        w = w+1
        l = l+1
    return blocks_per_layer

def num_blocks4(w, l, h):
    return sum([(w+i)*(l+i) for i in range(h)])

def num_blocks5(w, l, h):
    return sum(map(lambda x: (w+x)*(l+x), range(h)))


cProfile.run('num_blocks(10000000, 10000000, 10000000)', None, 1)
cProfile.run('num_blocks4(10000000, 10000000, 10000000)', None, 1)
cProfile.run('num_blocks5(10000000, 10000000, 10000000)', None, 1)

print(num_blocks(10000000, 10000000, 10000000))
print(num_blocks5(10000000, 10000000, 10000000))

'''
Test.it("Example cases")
Test.assert_equals(num_blocks(1, 1, 2), 5)
Test.assert_equals(num_blocks(2, 4, 3), 47)
Test.assert_equals(num_blocks(1, 10, 10), 880)
Test.assert_equals(num_blocks(20, 30, 40), 83540)

def num_blocks2(w, l, h):
    return functools.reduce(operator.add, [(w+i)*(l+i) for i in range(h)])

cProfile.run('num_blocks2(10000000, 10000000, 10000000)', None, 1)
print(num_blocks2(10000000, 10000000, 10000000))

def num_blocks3(w, l, h):
    height = range(h)
    return sum([(w+i)*(l+i) for i in height])

'''