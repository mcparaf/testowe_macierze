import numpy as np
import sys

dim_a = int(sys.argv[1])
dim_b = int(sys.argv[2])

lhs = np.random.randint(-100, 100, size=(dim_a, dim_b))
rhs = np.random.randint(-100, 100, size=(dim_b, dim_a))
result = np.matmul(lhs, rhs)

def print_matrix(filename, matrix):
    res = "{} {}\n".format(matrix.shape[0], matrix.shape[1])
    for i in matrix:
        for j in i:
            res += "{} ".format(j)
        res = res.strip()
        res += "\n"
    with open(filename, "w") as f:
        f.write(res)

print_matrix("lhs.txt", lhs)
print_matrix("rhs.txt", rhs)
print_matrix("result.txt", result)
