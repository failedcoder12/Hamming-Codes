# % Standard Decoding algorithm %
def error_generator(H,G):
	print("Generator Matrix ", G)
	print("Correction Matrix", H)

	Map = {}

	for i in range(16):
		C = np.array([int(x) for x in list('{0:04b}'.format(i))])
		GT = np.transpose(G)
		Codeword = np.dot(GT,C)%2
		num = 0
		poww = 1
		for j in Codeword:
			num = num + j*poww
			poww = poww*2
		Map[num] = C

	errors = 0

	for i in range(16):
		print("-----------------------------------------------------------------------------------")

		print(i,"->")

		C = np.array([int(x) for x in list('{0:04b}'.format(i))])
		print("Message : ",C)

		GT = np.transpose(G)

		Codeword = np.dot(GT,C)%2
		print("Codeword : ",Codeword)


		import itertools
		perm = 0
		lis = list(set(list(itertools.permutations([1,0,1,0,0,0,0]))))
		for listt in lis:
			e = np.array([int(x) for x in listt])
			perm = perm + 1
			# e = np.transpose(np.array([0,0,0,1,0,0,1]))

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

			num = 0
			poww = 1
			for j in Transmitted:
				num = num + j*poww
				poww = poww*2
			if num in Map:
				print(Map[num])
				if (Map[num] == C).all():
					errors = errors
				else:
					print(np.sum(C != Map[num]))
					errors += np.sum(C != Map[num])
			else:
				Map[num] = np.array([1,1,1,1])
				print(np.sum(C!=Map[num]))
				errors += np.sum(C!=Map[num])
				print("No possible")

			print("-----------------------------------------------------------------")

	print(perm)
	print("Errors ", errors/(16*perm))

	return errors/(16*perm)

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# % We get the following matrix after replacing the second row with the modulo-2 sum of the first two rows%
G1 = np.array([[1,1,1,0,0,0,0],
			[0,1,1,1,1,0,0],
			[0,1,0,1,0,1,0],
			[0,0,1,1,0,0,1]])
			
# % Standard generator matrix %
G = np.array([[1,1,1,0,0,0,0],
			[1,0,0,1,1,0,0],
			[0,1,0,1,0,1,0],
			[0,0,1,1,0,0,1]])

# % Parity check Matrix %
H = np.array([[0,0,0,1,1,1,1],
			[0,1,1,0,0,1,1],
			[1,0,1,0,1,0,1]])

objects = ('Standard Decoding', 'Optimized Standard Decoding')
y_pos = np.arange(len(objects))

GH = error_generator(H,G)
GH1 = error_generator(H,G1)

print(GH,GH1)

performance = [GH,GH1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Average Error')
plt.title('Hamming Codes')
 
plt.show()

