class dsu:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.size=[1]*n

    def find(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,x,y):
        ulp_x=self.find(x)
        ulp_y=self.find(y)

        if ulp_x==ulp_y:
            return #since they are in the same component
        
        if self.size[ulp_x]<self.size[ulp_y]:
            self.parent[ulp_x]=ulp_y
            self.size[ulp_y]+=self.size[ulp_x]
        else:
            self.parent[ulp_y]=ulp_x
            self.size[ulp_x]+=self.size[ulp_y]

obj = dsu(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
if obj.find(4) == obj.find(0):
    print('Yes')
else:
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else:
    print('No')
