import collections
class TreeNode:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None

def bfs(root):
    if root is None:
        return
    
    res=[]
    q=collections.deque()
    q.append(root)
    while q:
        n=len(q)
        temp=[]
        while n:
            cur=q.popleft()
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
            temp.append(cur.val)
            n-=1
        res.append(temp)
    return res

mynode=TreeNode(5)
mynode.left=TreeNode(10)
mynode.right=TreeNode(12)
res=bfs(mynode)
print(*res)
