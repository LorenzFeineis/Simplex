from fractions import Fraction

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
            return False
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
    def lkippung(self, column, plus, factor):
        zeros = [0 for i in range(self.rows()-1)]
        identity = []
        for i in range(self.rows()):
            row = zeros.copy()
            row.insert(i,1)
            identity.append(row)
        identity[column-1][plus-1] = factor
        kippung = Matrix(identity)
        return kippung.times(self)
    def change(self, one, two): # tauscht zwei Zeilen
        new = self.lkippung(one,two,1)
        new = new.lkippung(two,one,-1)
        new = new.lkippung(one,two,1)
        new = new.lkippung(two,two,-1)
        return new
    def inverse(self):
        if self.deter() == False:
            return False
        elif self.deter() == 0:
            return False
        else:
            zeros = [0 for i in range(self.rows()-1)]
            identity = []
            for i in range(self.rows()):
                row = zeros.copy()
                row.insert(i,1)
                identity.append(row)
            Inv = Matrix(identity)
            neu = []
            for i in range(self.rows()):
                neu.append(self.arg[i].copy())
            new = Matrix(neu)
            for i in range(self.columns()): # iteriert über die Spalten
                j=i
                while new.item(j+1,i+1) == 0:
                    j+=1
                new = new.change(i+1,j+1) # Stellt sicher, dass der i-te Diagonaleintrag nicht verschwindet
                Inv = Inv.change(i+1,j+1)
                Inv = Inv.lkippung(i+1,i+1,Fraction(1,new.item(i+1,i+1)))
                new = new.lkippung(i+1,i+1,Fraction(1,new.item(i+1,i+1))) # normiert den i-ten Diagonaleintrag
                j=1
                while j <= self.rows(): # vernichtet alle Einträge der i-ten Spalte
                    if new.item(j,i+1)==0:
                        j+=1
                    elif j==i+1:
                        j+=1
                    else:
                        Inv = Inv.lkippung(j,i+1,-new.item(j,i+1))
                        new = new.lkippung(j,i+1,-new.item(j,i+1))
                        j+=1
            return(Inv)



x = Matrix([[1,2],[3,4]])
y = Matrix([[5,-1],[6,-4]])
A = Matrix([[1,2,3,4],[4,5,6,4],[7,8,9,4]])
B = Matrix([[1,2,3,4],[5,123,7,8],[9,10,11,12],[13,14,15,134]])


B.times(B.inverse()).show()
