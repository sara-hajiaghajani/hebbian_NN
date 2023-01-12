# AND bipolar
x_and_bipolar = [([1, 1, 1], 1), ([1, -1, 1], -1), ([-1, 1, 1], -1), ([-1, -1, 1], -1)]
# OR bipolar
x_or_bipolar = [([1, 1, 1], 1), ([1, -1, 1], 1), ([-1, 1, 1], 1), ([-1, -1, 1], -1)]
# NAND bipolar
x_nand_bipolar = [([1, 1, 1], -1), ([1, -1, 1], 1), ([-1, 1, 1], 1), ([-1, -1, 1], 1)]
# NOR bipolar
x_nor_bipolar = [([1, 1, 1], -1), ([1, -1, 1], -1), ([-1, 1, 1], -1), ([-1, -1, 1], 1)]

# AND binary
x_and_binary = [([1, 1, 1], 1), ([1, 0, 1], 0), ([0, 1, 1], 0), ([0, 0, 1], 0)]
# OR binary
x_or_binary = [([1, 1, 1], 1), ([1, 0, 1], 1), ([0, 1, 1], 1), ([0, 0, 1], 0)]
# NAND binary
x_nand_binary = [([1, 1, 1], 0), ([1, 0, 1], 1), ([0, 1, 1], 1), ([0, 0, 1], 1)]
# NOR binary
x_nor_binary = [([1, 1, 1], 0), ([1, 0, 1], 0), ([0, 1, 1], 0), ([0, 0, 1], 1)]

"""
 #...#        .###.
 .#.#.        #...#
 ..#..        #...#
 .#.#.        #...#
 #...#        .###.
 
"""

xo = [
    ([1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1], 1),
    ([-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1], 1)
]


def hebb_learning(x):
    w = [0 for _ in x[0][0]]
    for i in range(len(x)):
        for j in range(len(w)):
            w[j] += x[i][0][j] * x[i][1]
    return w


def hebb_test_binary(x, w):
    for i in range(len(x)):
        yin = 0
        for j in range(len(x[i][0])):
            yin += x[i][0][j] * w[j]
        if yin >= 0:
            yout = 1
        else:
            yout = 0
        if yout != x[i][1]:
            return False
    return True


def hebb_test_bipolar(x, w):
    for i in range(len(x)):
        yin = 0
        for j in range(len(x[i][0])):
            yin += x[i][0][j] * w[j]
        if yin >= 0:
            yout = 1
        else:
            yout = -1
        if yout != x[i][1]:
            return False
    return True


print("learn AND Gate (binary):", end='\t\t')
weights = hebb_learning(x_and_binary)
print(hebb_test_binary(x_and_binary, weights))

print("learn OR Gate (binary):", end='\t\t\t')
weights = hebb_learning(x_or_binary)
print(hebb_test_binary(x_or_binary, weights))

print("learn NAND Gate (binary):", end='\t\t')
weights = hebb_learning(x_nand_binary)
print(hebb_test_binary(x_nand_binary, weights))

print("learn NOR Gate (binary):", end='\t\t')
weights = hebb_learning(x_nor_binary)
print(hebb_test_binary(x_nor_binary, weights))

print("learn AND Gate (bipolar):", end='\t\t')
weights = hebb_learning(x_and_bipolar)
print(hebb_test_bipolar(x_and_bipolar, weights))

print("learn OR Gate (bipolar):", end='\t\t')
weights = hebb_learning(x_or_bipolar)
print(hebb_test_bipolar(x_or_bipolar, weights))

print("learn NAND Gate (bipolar):", end='\t\t')
weights = hebb_learning(x_nand_bipolar)
print(hebb_test_bipolar(x_nand_bipolar, weights))

print("learn NOR Gate (bipolar):", end='\t\t')
weights = hebb_learning(x_nor_bipolar)
print(hebb_test_bipolar(x_nor_bipolar, weights))

print("learn XO (bipolar):", end='\t\t\t')
weights = hebb_learning(xo)
print(hebb_test_bipolar(xo, weights))
