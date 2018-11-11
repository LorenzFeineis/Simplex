class Matrix(object):
    """docstring for Matrix."""
    def __init__(self, arg):
        self.arg = arg
    def rows(self):
        return len(self.arg)
    def columns(self):
        return len(self.arg[0])
    def show(self):
        for i in range(self.rows()):
            print(self.arg[i])
    def item(self, r,c):
        return(self.arg[r-1][c-1])
    def submatrix(self,r,c):
        sub = []
        for i in range(self.rows()):
            sub.append(self.arg[i].copy())
        del(sub[r-1])
        for i in range(len(sub)):
            del(sub[i][c-1])
        return Matrix(sub)
    def deter(self):
        if self.rows() is not self.columns():
            print("No determinant defined for not quadratic matrices.")
        else:
            if self.rows() == 2:
                return self.item(1,1)*self.item(2,2)-self.item(1,2)*self.item(2,1)
            elif self.rows() == 1:
                return self.item(1,1)
            else:
                sum = 0
                for i in range(self.rows()):
                    pot = -1
                    for j in range(1+i):
                        pot = -1*pot
                    sum += pot*self.item(1,i+1)* self.submatrix(1,i+1).deter()
                return sum
    def times(self, second):
        if self.columns() == second.rows():
            product = []
            for i in range(self.rows()):
                row = []
                for j in range(second.columns()):
                    sum = 0
                    for k in range(self.columns()):
                        sum += self.item(i+1,k)*second.item(k,j+1)
                    row.append(sum)
                product.append(row)
            return Matrix(product)
        else: print("These two matrices cannot be multiplicated")


x = Matrix([[1,2],[3,4]])
y = Matrix([[5,-1],[6,-4]])


A = Matrix([[1,2,3,4],[4,5,6,4],[7,8,9,4]])

B = Matrix([[1,2,3,4],[5,123,7,8],[9,10,11,12],[13,14,15,134]])

C = A.times(B)

C.show()
