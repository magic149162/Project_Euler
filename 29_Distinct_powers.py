#https://projecteuler.net/problem=29
print len(set(i**j for i in xrange(2,101) for j in xrange(2,101)))

'''
c=[]
p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def primefact(n,p,e):
    a={}
    for i in p:
        a[i]=0
        while n%i==0:
            n=n/i
            a[i]+=e
    return a
            
for i in range(2,101):
    for j in range(2,101):
        k=primefact(i,p,j)
        if k in c:
            continue
        c+=[k]

print len(c)'''