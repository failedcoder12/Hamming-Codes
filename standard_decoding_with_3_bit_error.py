# Standard Decoding algorithm 

def hamming_distance(A,B):
	return np.sum(A != B)

def error_generator(H,G):
	print("Correction Matrix", H)
	print("Generator Matrix ", G)

#Map which will be used to do mapping of each codeword woth dataword
	Map = {}

#Mapping all
	for i in range(16):

		#Converting decimal number to a binary list of size 4
		C = np.array([int(x) for x in list('{0:04b}'.format(i))])
		
		#Transposing matrix
		GT = np.transpose(G)

		#Dot product if two matrix
		Codeword = np.dot(GT,C)%2
		num = 0
		poww = 1
		for j in Codeword:
			num = num + j*poww
			poww = poww*2
		Map[num] = C

	#Setting number of errors to 0
	errors = 0

	#Iterating over the all possible codewords
	for i in range(16):
		print("-----------------------------------------------------------------------------------")

		print(i,"->")

		#Converting it to binary form
		C = np.array([int(x) for x in list('{0:04b}'.format(i))])
		print("Message : ",C)

		#Taking transpose
		GT = np.transpose(G)

		#codeworking by taking dot product of generator and dataword 
		Codeword = np.dot(GT,C)%2
		print("Codeword : ",Codeword)

		#Python tool for getting permutation
		import itertools

		#Setting number of permutation to 0 and then counting
		perm = 0

		#putting all possible permutation in lis
		lis = list(set(list(itertools.permutations([1,1,1,0,0,0,0]))))

		#looping over complete lis
		for listt in lis:
			e = np.array([int(x) for x in listt])
			perm = perm + 1
			# e = np.transpose(np.array([0,0,0,1,0,0,1]))

			#Adding error
			Transmitted = (e + Codeword)%2
			print(Transmitted)

			#decoding it	
			decode = np.dot(H,Transmitted)%2
			print(decode)

			#Detecting error and correcting
			for k in range(3):
				val = -1
				HT = np.transpose(H)
				for i in range(HT.shape[0]):
					if (HT[i][0:] == decode).all():
						val = i
						break

			#correcting it
				if(val != -1):
					Transmitted[val] = (Transmitted[val]+1)%2

				print(Transmitted)

			#Getting word to be decoded
			decode = np.dot(H,Transmitted)%2
			print(decode)

			num = 0
			poww = 1

			#Calculating number of errors
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
				mini_ans = next(iter(Map))
				mini_hamm = hamming_distance(num,mini_ans)
				for key,valu in Map.items():
					if(hamming_distance(num,key)<=mini_hamm):
						mini_hamm = hamming_distance(num,key)
						mini_ans = key
				print(np.sum(C != Map[mini_ans]))
				errors += np.sum(C != Map[mini_ans])
				print("No possible")

			print("-----------------------------------------------------------------")

	print(perm)
	print("Errors ", errors/(16*perm))

	return errors/(16*perm)

#Importing libraries required for plotting and calculating
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


#  We get the following matrix after replacing the second row with the modulo-2 sum of the first two rows
G1 = np.array([[1,1,1,0,0,0,0],
			[0,1,1,1,1,0,0],
			[0,1,0,1,0,1,0],
			[0,0,1,1,0,0,1]])
			
#  Standard generator matrix 
G = np.array([[1,1,1,0,0,0,0],
			[1,0,0,1,1,0,0],
			[0,1,0,1,0,1,0],
			[0,0,1,1,0,0,1]])

# Parity check Matrix 
H = np.array([[0,0,0,1,1,1,1],
			[0,1,1,0,0,1,1],
			[1,0,1,0,1,0,1]])


#Giving name to graph plot
objects = ('Standard Decoding', 'Optimized Standard Decoding')
y_pos = np.arange(len(objects))

# Calculating errors percentage
GH = error_generator(H,G)
GH1 = error_generator(H,G1)

#Printing them (Percentage error)
print(GH,GH1)

#Converting it to a array
performance = [GH,GH1]
 
#Plotting it
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Average Error')
plt.title('Comparison for three bit error')
 
plt.show()

