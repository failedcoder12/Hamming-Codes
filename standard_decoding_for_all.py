# Standard Decoding algorithm 

def hamming_distance(A,B):
	return np.sum(A != B)

def error_generator_two_bit(H,G):
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
		lis = list(set(list(itertools.permutations([1,1,0,0,0,0,0]))))

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

def error_generator_three_bit(H,G):
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

def error_generator_four_bit(H,G):
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
		lis = list(set(list(itertools.permutations([1,1,1,1,0,0,0]))))

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
from matplotlib.ticker import FormatStrFormatter
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
GH2 = error_generator_two_bit(H,G)
GH21 = error_generator_two_bit(H,G1)

GH3 = error_generator_three_bit(H,G)
GH31 = error_generator_three_bit(H,G1)

GH4 = error_generator_four_bit(H,G)
GH41 = error_generator_four_bit(H,G1)

N = 3

GHH = (GH2,GH3,GH4)
GHH2 = (GH21,GH31,GH41)

fig,ax = plt.subplots()
ind = np.arange(N)
width = 0.20
p1 = ax.bar(ind,GHH,width)

p2 = ax.bar(ind+width/2,GHH2,width)
ax.set_title('Standard vs Optimal Standard Decoding')
ax.set_xticks(ind+width/2)
ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))
ax.yaxis.set_ticks(np.arange(0, 2.5, 0.1))
ax.set_xticklabels(('2 bit error','3 bit error','4 bit error'))
ax.legend((p1[0],p2[0]),('Standard Decoding','Optimal Standard Decoding'))
# ax.yaxis.set_units(inch)
ax.autoscale_view()
plt.grid()
print(GHH)
print(GHH2)
plt.show()

# import plotly
# import plotly.plotly as py
# import plotly.graph_objs as go

# trace1 = go.Bar(
# 	x = ['2 bit error','3 bit error','4 bit error'],
# 	y = [GH2,GH3,GH4],
# 	name = 'Standard Decoding'
# )

# trace2 = go.Bar(
# 	x = ['2 bit error','3 bit error','4 bit error'],
# 	y = [GH21,GH31,GH41],
# 	name = 'Standard Decoding with Optimization'
# )

# data = [trace1,trace2]
# layout = go.Layout(
# 	barmode='group'
# )

# fig = go.Figure(data = data,layout=layout)
# py.iplot(fig,filename='grouped-bar')