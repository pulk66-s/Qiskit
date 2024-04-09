def row_reduce(matrix):
    for i in range(len(matrix)):
        index, firstNonZero = list(filter(lambda x: x[1] != 0, enumerate(matrix[i])))[0]
        for j in range(len(matrix)):
            if i == j:
                continue
            sameIndex = matrix[j][index]
            rapport = -sameIndex / firstNonZero
            matrix[j] = list(map(lambda x: x[1] + rapport * matrix[i][x[0]], enumerate(matrix[j])))
    for i in range(len(matrix)):
        index, firstNonZero = list(filter(lambda x: x[1] != 0, enumerate(matrix[i])))[0]
        if firstNonZero != 1:
            matrix[i] = list(map(lambda x: x / firstNonZero, matrix[i]))
    return matrix

def find_invert(matrix):
    blockMatrix = matrix
    for i in range(len(blockMatrix)):
        blockMatrix[i] += [0] * i + [1] + [0] * (len(blockMatrix) - i - 1)
    rowReduce = row_reduce(blockMatrix)
    invert = list(map(lambda x: x[len(matrix):], rowReduce))
    return invert

def main():
    m = [
        [1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 2]
    ]
    invert = find_invert([i.copy() for i in m])
    print("m")
    for i in m:
        print(i)
    print("i")
    for a in invert:
        print(a)

if __name__ == "__main__":
    main()