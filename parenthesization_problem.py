# dp1

import sys

given_list = [1, 6, 4, 5, 7, 2, 9, 8]

# assume sequence starts with addition i.e 1 + 6 * 4 + 2 * 8 + 3
# That means there is always in '+' infront of an element in an odd index and '*' infront of an element in an even index

adict = {}

def cal(alist, length):
	n = length
	if n == 1:
		return alist[0]
	elif n == 2:
		return alist[0]+alist[1]

	elif n % 2 == 0:
		if not str(n-1) in adict:
			adict[str(n-1)] = cal(alist, n-1)
		penultimate_in = adict[str(n-1)]+alist[n-1]

		if not str(n-2) in adict:
			adict[str(n-2)] = cal(alist, n-2)
		penultimate_out = adict[str(n-2)]*(alist[n-2]+alist[n-1])

		return max(penultimate_in, penultimate_out)

	else:
		if not str(n-1) in adict:
			adict[str(n-1)] = cal(alist, n-1)
		penultimate_in = adict[str(n-1)]*alist[n-1]

		if not str(n-2) in adict:
			adict[str(n-2)] = cal(alist, n-2)
		penultimate_out = adict[str(n-2)]+(alist[n-2]*alist[n-1])

		return max(penultimate_in, penultimate_out)

print cal(given_list, len(given_list))
print adict