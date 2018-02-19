"""
# Name:			Pratik kulkarni
# ID:			801020567
# Assignment: 	Write a program that reads in the trace and simulates
#				different branch prediction schemes.
# Course:		Computer Architecture
# Homework:		HW3
"""

"""
THIS IS A 2 LEVEL LOCAL BRANCH PREDICTOR
"""

file=open('tracehw3.trace','r')
ghr=0
indexlht=0
indexpht=0

pht=[0] * 1024								#List used to simulate the behaviour of pattern history table
lht=[0] * 128

mispredict=0 								#Used for the misprediction counter
linectr=0    								#Counts the number of lines present in the trace file
bitwidth=0 									#Used to take the bitwidth for the saturating counter, from the user
centerval=0 								#Calculates the center value for a particular bit counter size(eg: 1 for a 2 bit counter)

print("Enter the counter size as 2,4,6,8 or 10 (bits)")
bitwidth=int(raw_input())
print ("Calculating the prediction rate....")
centerval=(((2**bitwidth)-1)/2)

for line in file:
	line=line.rstrip() 						#Used to strip the newline character at the end
	words=line.split() 						#Used to split the addressess and 'T' or 'N' tag
	indexlht=int(words[0])%128
	indexpht=lht[indexlht]
	if words[1]=='N':	
		if pht[indexpht]<=centerval and pht[indexpht]>0:
			pht[indexpht]=pht[indexpht]-1
		elif pht[indexpht]>centerval:
			pht[indexpht]=pht[indexpht]-1
			mispredict=mispredict+1
		indexpht=((indexpht<<1) & 0x000003ff)
		lht[indexlht]=indexpht            #The Local history table's value is used as an index to index the pattern/branch history table
	elif words[1]=='T':
		if pht[indexpht]<=centerval:
			pht[indexpht]=pht[indexpht]+1
			mispredict=mispredict+1
		elif pht[indexpht]>centerval and pht[indexpht]<((2**bitwidth)-1):
			pht[indexpht]=pht[indexpht]+1		
		indexpht=(((indexpht<<1) | 0x01) & 0x000003ff)	
		lht[indexlht]=indexpht
	linectr=linectr+1
pred=format(100-(100*(mispredict/(linectr*1.0))),'0.05f')
print "The prediction rate for a ",bitwidth," bit counter is:", pred, "%"
print "The misprediction rate for a ",bitwidth," bit counter is:", (100-float(pred)), "%"