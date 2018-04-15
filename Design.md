*DESIGN OF HAMMING CODE AS ERROR-REDUCING  CODE*

**PROJECT GOAL :**

*  Our main contribution is to show a lower bound on the average number of errors remaining in the decoded message with standard decoding  while two errors are introduced by an adversary.

*  We also show that this lower bound is achievable for Hamming codes.

*  Standard decoding is not the best decoding method for the purpose of error reduction. We explore several other potential decoding methods for Hamming codes, and experimentally show that it is possible to beat the standard decoding lower bound on average number of errors. 

*  This demonstration will be followed by several algorithms that attempt to maximize the reduction in errors along with an analysis of the performance and scalability of each algorithm.


**OUTCOMES AND OBJECTIVES :**

* In this implementation we initiate the study of the error-reducing property for classical families of error-correcting codes. 

* It was found that the error reduction capabilities of Hamming codes are limited when standard decoding is used, inviting the study of other decoding methods. Several other decoding algorithms were implemented for Hamming codes and found to be more effective for reducing errors than standard decoding. 

* It is also of interest to explore other decoding methods to provide a greater level of error reduction with low complexity.

* Future work should address the best possible reduction that can be achieved as no lower bound is known in general. 

* Finally, it will be of interest to compute the error-reducing properties of other well-known families of codes such as BCH codes. 

* Finally, it will be of interest to compute the error-reducing properties of other well-known families of codes such as BCH codes. 


** CONSTRAINS :**

* When multiple errors are introduced into a codeword, there is no guarantee of correct recovery of messages. 

* We show that in that situation as well, it can be possible for a Hamming code to reduce the number of errors contained in that codeword in the decoded message.

** ABOUT IMPLEMENTATION :**

* We proved that the matrix we found is the optimal generator matrix for the [7,4,3]-Hamming code with standard decoding in terms of the mean number of errors in the received message for every possible error vector. 

** RESULTS : **

* Though Hamming codes with standard decoding,, other decoding methods have shown more favorable results.

* Several decoding algorithms were experimentally tested, giving a best-case result of having 9 7 or 1.2857 errors in the received message.

* However, there is an increased computational cost of employing such algorithms, substituting a matrix multiplication for several search operations within larger sets. Furthermore, these algorithms do not guarantee independence of the residual errors on the transmitted codeword (i.e., proposition 2 is not valid). 

* For all of these algorithms, it should be assumed that the encoding procedure is unchanged and that the generator matrix in (1) was used for the encoding process. In all of the decoders , the ﬁrst step consists of determining all codewords that are a distance of less than or equal to the number of errors introduced from the erroneous vector. The messages corresponding to these codewords were collected into a list L. 