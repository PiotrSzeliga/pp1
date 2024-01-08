class C():
    def __init__(self,coordinates):
        self.coordinates = coordinates
    def m(self,n):
        n2 = 0
        for i in self.coordinates:
            n3 = 0
            for k in i: 
                if k <= 0:
                    continue
                else:
                    n3 += 1     
                if n3 == 2:
                    n2 += 1
        if n2 >= n:
            return True
        else:
            return False
        
c = C([[2,3],[1,8],[-6,4],[3,-7]])
print(c.m(2))
print(c.m(3))

