class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list1)):

            for j in range(len(self.list2[i])):
                matr[i][j] = self.list1[i][j] + self.list2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

mymatrix = Matrix([[11, 3, 24],
                    [7, 19, 1],
                    [1, 51, 0]],
                   [[34, 2, 2],
                    [7, 8, 11],
                    [13, 15, 7]])

print(mymatrix.__add__())
