def multiply(a,b):
    n=len(a)
    mult=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
    
            for k in range(n):
                mult[i][j]+=a[i][k]*b[k][j]

    return mult

def exponentiation(a,n):
    if n==1:
        return a
    resultby2=exponentiation(a,n//2)
    result=multiply(resultby2,resultby2)
    if n&1:
        result=multiply(result,resultby2)
    return result

print(exponentiation([[1,1],[1,1]],2))