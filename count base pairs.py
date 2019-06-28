
sequence='ACTTGTCGAATCGGTGCCTGAAGTCGTGCGTAGC'
#Loop through all of the bases in a sequence
for base in sequence:
    #Print every base
    print(base)

#Sometimes it is useful to have print statements explain what you are seeing
#on the screen. For example:

print('This is the sequence we are interested in:',sequence)
    
#Find how many A's are in this sequence
countA=0
for base in sequence:
    if base=='A':
        countA=countA+1
#Find how many C's are in this sequence
countC=0
for base in sequence:
    if base=='C':
        countC=countC+1
#Find how many G's are in this sequence
countG=0
for base in sequence:
    if base=='G':
        countG=countG+1
#Find how many T's are in this sequence
countT=0
for base in sequence:
    if base=='T':
        countT=countT+1

#Is there a more efficient way to do this? Using else if statements?
countA=0
countC=0
countG=0
countT=0

for base in sequence:
    if base=='A':
        countA=countA+1
    elif base=='C':
        countC=countC+1
    elif base=='G':
        countG=countG+1
    elif base=='T':
        countT=countT+1
