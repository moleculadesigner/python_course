from utils import hamming_distance

s1 = 'ATGTAAAATATATATTGCGTCGTGAA'
s2 = 'AATTAGGGTATATATTGCGTCGTGTT'
sub = ''
for c1, c2 in zip(s1, s2):
    if c1 == c2:
        sub += ' '
    else:
        sub += ':'
print(s1)
print(sub)
print(s2)
print("Distance = {}".format(hamming_distance(s1, s2)))