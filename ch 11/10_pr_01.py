class C2dVac():
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    
    def __str__(self):
        return (f"{self.icap}i+{self.jcap}j")
        
class C3dVac(C2dVac):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return (f"{self.icap}i+{self.jcap}j+{self.kcap}k")
v2=C2dVac(1,8)
v3=C3dVac(2,9,6)
print(v2)
print(v3)