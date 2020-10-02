class Matrix:
    def __init__(self, a, b):
        # matrix can be used for finding fibonacci numbers (thanks linear algebra)
        # also matrix is the natural representation of N^2 -> N^2
        self.matrix = [[a, a], [a, b]]

#    def pow(self, n):
#        if n = 2: