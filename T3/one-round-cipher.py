import numpy as np

def sbox(i):
    arr = [6, 2, 3, 10, 0, 14, 4, 7, 8, 15, 12, 11, 1, 5, 9, 13]
    return arr[i]
m0 = 11
m1 = 4
c0 = 8
c1 = 7

possible_k1 = []

delta_v = c0 ^ c1

for k1 in range(16):
    v_candidate = sbox(m0 ^ k1) ^ sbox(m1 ^ k1)
    if(v_candidate == delta_v):
        possible_k1.append(k1)


possible_k1 = set(possible_k1)
print("The possible keys k1 are {}".format(possible_k1))

possible_k2 = set()

for k1 in possible_k1:
    k2 =  sbox(m0 ^ k1) ^ c0
    possible_k2.add(k2)

print("The possible keys k2 are {}".format(possible_k2))

        

