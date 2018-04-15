#  Hamming Codes as Error Reducing Codes
```

```
## About
* Hamming codes are the first of it's kind for error correcting codes which can correct error in a block of binary strings. 
* In this we try to analyze error reducing capabilities of the hamming codes. 
* We are focused on binary linear codes. 
 Messages are coded into some strings called as codeword.They have some limit upon the number of errors to be corrected.
* The [7; 4; 3]-Hamming code is the first Hamming code, where m = 3.
* Number of maximum error corrected - floor((d-1)/2)
* One bit of error can be corrected for length - (2^m -m -1)
* Codeword produced for one length correction - (2^m - 1)
* Hamming distance between the two words x; y^2 Fn2, d(x; y).


## Standard Hamming code decoding

* The [7,4,3]-Hamming code has generator matrix G and parity check matrix H, given below respectively:.
 * G = 
      * 1 1 1 0 0 0 0 
      * 1 0 0 1 1 0 0 
      * 0 1 0 1 0 1 0
      * 0 0 1 1 0 0 1
 * H = 
      * 0 0 0 1 1 1 1
      * 0 1 1 0 0 1 1 
      * 1 0 1 0 1 0 1
      

## Lower Bound on Hamming code decoding

* The [7,4,3]-Hamming code has generator matrix G and parity check matrix H, given below respectively:.
 * G1 = 
      * 1 1 1 0 0 0 0 
      * 0 1 1 1 1 0 0 
      * 0 1 0 1 0 1 0
      * 0 0 1 1 0 0 1
 * H1 = 
      * 0 0 0 1 1 1 1
      * 0 1 1 0 0 1 1 
      * 1 0 1 0 1 0 1
      

```
Figure Output shows the comparison in Hamming codding decoding with standard decoding and what we get as a lower bound on it.
```

## Explaination



* If we replace the second row with the modulo-2 sum of the ﬁrst two rows, we get the following generator matrix. 
 * G' = 
      * 1 1 1 0 0 0 0
      * 0 1 1 1 1 0 0 
      * 0 1 0 1 0 1 0
      * 0 0 1 1 0 0 1 
* When generator matrix G' is used along with the parity check matrix, the average number of errors found in the decoded message for all error vectors becomes 12/7 or about 1.714. While this improvement is relatively small, this Hamming code reaches the maximum level of error reduction that is theoretically possible for the
[7,4,3]-Hamming code with standard decoding. 

* Now using the lower-bound technique the ratio has been increased

**For 2 Bit error**

![Output of 2 bit error correction](2bit.png)

*For  2 bit error correction we were able to reduce the error in the set of the codewords to an average of 1.8571 by standard decoding method, but by optimizing the standard decoding method the count of average number of error is reduced to 1.7143.

**For 3 Bit error**

![Output of 3 bit error correction](3bit.png)

*For  3 bit error  correction we were able to reduce the error in the set of the codewords to an average of 2.200 by standard decoding method, but by optimizing the standard decoding method the count of average number of error is reduced to 2.1714.

**For 4 bit error**

![Output of 4 bit error correxction](4bit.png)

*For  34 bit error correction we were able to reduce the error in the set of the codewords to an average of 1.9429 by standard decoding method, but by optimizing the standard decoding method the count of average number of error is reduced to 1.8286.


