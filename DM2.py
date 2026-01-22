class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1:
                    for k in range(self.n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def check_relation(self):
        r = self.is_reflexive()
        s = self.is_symmetric()
        a = self.is_antisymmetric()
        t = self.is_transitive()

        print("Reflexive:", r)
        print("Symmetric:", s)
        print("Anti-symmetric:", a)
        print("Transitive:", t)

        if r and s and t:
            print("Relation is an Equivalence Relation")
        elif r and a and t:
            print("Relation is a Partial Order")
        else:
            print("Relation is None")


# Example
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

rel = RELATION(matrix)
rel.check_relation()
