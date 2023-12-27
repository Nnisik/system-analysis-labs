import numpy

def fill_elems_matrix(matrix, matrix_size):
    for index_1 in range(1, matrix_size + 1):
        for index_2 in range(1, matrix_size + 1):
            matrix[sum(index_1, index_2)][index_1 * index_2] += 1
    return matrix

def calculate_Ha(p):
    h = [[0 if pij == 0 else -pij * numpy.log2(pij) for pij in row] for row in p]
    return sum(map(sum, h))

def calculate_Hb(matrix, n):
    matrix = numpy.transpose(matrix)
    p = [[x / (n * n) for x in row] for row in matrix]
    h = [0 if sum(row) == 0 else -sum(row) * numpy.log2(sum(row)) for row in p]
    return sum(h)

def task():
    n = 6
    elems_matrix = [[0 for x in range(n**2 + 1)] for y in range(2 * n + 1)]
    elems_matrix = fill_elems_matrix(elems_matrix, n)

    p = [[x / n**2 for x in row] for row in elems_matrix]
    Hab = calculate_Ha(p)

    p2 = [[0 if sum(row) == 0 else mij / sum(row) for mij in row] for row in elems_matrix]
    h2 = [[0 if pij == 0 else -pij * numpy.log2(pij) for pij in row] for row in p2]

    HaB = 0.0
    for i in range(len(p2)):
        HaB += sum(h2[i]) * sum(p[i])

    Ha = Hab - HaB
    Hb = calculate_Hb(elems_matrix, n)

    return [Hab, Ha, Hb, HaB, Hb - HaB]

if __name__ == "__main__":
    # example_data = [4.34, 3.27, 4.04, 1.06, 2.98]
    print(task())