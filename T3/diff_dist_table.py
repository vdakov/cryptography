import numpy as np

def sbox(i):
    arr = [6, 2, 3, 10, 0, 14, 4, 7, 8, 15, 12, 11, 1, 5, 9, 13]
    return arr[i]

m = 4
n = 4
difference_dist_table = np.zeros((2**m, 2**n))


for plaintext_1 in range(2**m):
    for plaintext_2 in range(2**m):
        delta_u = plaintext_1 ^ plaintext_2
        delta_v = sbox(plaintext_1) ^ sbox(plaintext_2)
        difference_dist_table[delta_u][delta_v] += 1

print(difference_dist_table)
difference_dist_table[0][0] = -1 #does not count because this is the 0 XOR input (meaning two same plaintexts and two same ciphertexts) and not a pair of inputs

print('The maximum differential probability of the table is {}/{}'.format(int(np.max(difference_dist_table)), np.max([2**m,2**n])))


