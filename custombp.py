from time import sleep

file=open('tracehw3.trace','r')
index=0
index1=0

pht=[0] * 1024	
pht1=[0] * 4096							#LIST IS USED TO SIMULATE THE PATTERN HISTORY TABLE BEHAVIOUR
#pht[10]=pht[10]+1 				use later to increment the counter
mispredictpht=0
mispredictpht1=0
linectr=0
bitwidth=0
centerval=0

print("Enter the bitwidth")
bitwidth=int(raw_input())
centerval=(((2**bitwidth)-1)/2)
# print centerval

sleep(1)
for line in file:
	line=line.rstrip()
	words=line.split()
	index=int(words[0])%1024
	index1=int(words[0])%4096

	if words[1]=='N':
		if pht[index]<=centerval and pht[index]>0:
			pht[index]=pht[index]-1
		elif pht[index]>centerval:
			pht[index]=pht[index]-1
			mispredictpht=mispredictpht+1

		if pht1[index1]<=centerval and pht1[index1]>0:
			pht1[index1]=pht1[index1]-1
		elif pht1[index1]>centerval:
			pht1[index1]=pht1[index1]-1
			mispredictpht1=mispredictpht1+1

	elif words[1]=='T':
		if pht[index]<=centerval:
			pht[index]=pht[index]+1
			mispredictpht=mispredictpht+1
		elif pht[index]>centerval and pht[index]<((2**bitwidth)-1):
			pht[index]=pht[index]+1

		if pht1[index1]<=centerval:
			pht1[index1]=pht1[index1]+1
			mispredictpht1=mispredictpht1+1
		elif pht1[index1]>centerval and pht1[index1]<((2**bitwidth)-1):
			pht1[index1]=pht1[index1]+1
	linectr=linectr+1
print "The misprediction for 1024 and 4096 respectively is:\n",mispredictpht,"\n",mispredictpht1 
#pred=format(100-(100*(mispredict/(linectr*1.0))),'0.02f')
#print "prediction rate is:", pred, "%"