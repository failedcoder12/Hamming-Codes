import numpy as np

G = np.array([[1,1,1,0,0,0,0],
			[1,0,0,1,1,0,0],
			[0,1,0,1,0,1,0],
			[0,0,1,1,0,0,1]])

H = np.array([[0,0,0,1,1,1,1],
			[0,1,1,0,0,1,1],
			[1,0,1,0,1,0,1]])

# print(G)
# print(H)

C = np.array([0,1,0,1])

# print(C)

GT = np.transpose(G)

# print(GT)

Codeword = np.dot(GT,C)%2
print(Codeword)

e = np.transpose(np.array([1,0,0,1,0,0,0]))

Transmitted = (e + Codeword)%2
print(Transmitted)

decode = np.dot(H,Transmitted)%2
print(decode)

val = 0
HT = np.transpose(H)
for i in range(HT.shape[0]):
	if (HT[i][0:] == decode).all():
		val = i
		break

Transmitted[val] = (Transmitted[val]+1)%2

print(Transmitted)

decode = np.dot(H,Transmitted)%2
print(decode)

