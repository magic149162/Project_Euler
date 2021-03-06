#https://projecteuler.net/problem=2
'''Two differnent ways to calculate the sum of even memebers in Fibonacci series with the last member not exceeds 4 million.

    The first approach deduces the members from the definition of the series as a[n] = a[n-1] +a[n-2]
    While the second one acquires the members from an interesting truth that the ratio between two adjacent even members approaches Phi**3, \n
    where Phi = Golden ratio(approximately 1.61803398)'''
def fib():
    sum = 2
    a,b=1,2
    while True:
        if(b<4000000):
            a,b = b,a+b            
            #fib_seq.append(b)
            if(not b%2):
                print b
                sum+=b
        else:
            break    
    return sum
print fib()

#print sum(filter(lambda i:i%2 == 0,fib()))
#print sum([i for i in fib() if not i%2])


Phi=(5**0.5+1)/2.0 #get the golden ratio
def fib_even():
    a=2
    sum=2
    while True:
        a=round(a*Phi**3)
        if(a<4000000):            
            print int(a)
            sum=sum+a
        else:break
    return sum
print int(fib_even())

