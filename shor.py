import numpy as np

def order(a, N):
    tmp = a
    for i in range(1, N):
        tmp = (tmp * a) % N
        if tmp == a: 
            return i
    
N = 456221
a1 = 123
a2 = 345

print(np.gcd(a1, N)) # gives 1
print(np.gcd(a2, N)) # gives 1

r1 = order(a1, N) 
r2 = order(a2, N) 
print('r1 =', r1) #=227406
print('r2 =', r2) #=75802

v1 = pow(a1, r1//2, N)  #results in overflow
v2 = pow(a2, r2//2, N)  #results in overflow

print(f'v1 = {v1}')
print(f'v2 = {v2}')

p1 = np.gcd(v1 - 1, N)
q1 = np.gcd(v1 + 1, N)
p2 = np.gcd(v2 - 1, N)
q2 = np.gcd(v2 + 1, N)

print('Factors 1:', p1, q1)
print('Factors 2:', p2, q2)
# both of the upper values give overflow







