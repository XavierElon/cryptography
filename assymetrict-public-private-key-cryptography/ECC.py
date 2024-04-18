

class Point:
    
    def __init__(self, x, y):
        self.x  = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + " - " + str(self.y)
    

class EllipticCurveCryptography:
    def __init__(self, a, b):
        self.a  = a
        self.b = b
        
    def point_addition(self, P, Q):
        x1, y1 = P.x, P.y
        x2, y2 = Q.x, Q.y
        
        if x1 == x2 and y1 == y2:
            m = (3 * x1 * x1 + self.a) / (2 * y1)
        else:
            m = (y2 - y1) / (x2 - x1)
        
        x3 = m*m - x1
        y3 = m*(x1 - x3) - y1
        
        return Point(x3, y3)
    
if __name__ == '__main__':
    ecc = EllipticCurveCryptography(0, 7)
    p = Point(1, 1)
    print(ecc.point_addition(p, p))