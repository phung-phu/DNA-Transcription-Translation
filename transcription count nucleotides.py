sequence = "ACTTGTCGAATCGGTGCCTGAAGTCGTGCGTAGC"
total = len(sequence)*1.0
print "hello", sequence
print total
print len(sequence)

#1.3: Looping Through Bases
for x in sequence:
   print x


#1.4: Evaluating Missing Bases
if "-" in sequence:
   print "Missing bases detected"
else:
   print "No missing bases detected!"


#1.5: Counting DNA Nucleotides by Base
counterA = 0
for x in sequence:
   if "A"in x:
       counterA += 1
print "It contains " + str(counterA) + " adenines."


#1.6: Counting DNA Nucleotides by Base
counterC = 0
counterG = 0
counterT = 0
for x in sequence:
   if "C" in x:
       counterC += 1
   if "G" in x:
       counterG +=1
   if "T" in x:
       counterT +=1
print "It contains " + str(counterC) + " cytosines."
print "It contains " + str(counterG) + " guanines."
print "It contains " + str(counterT) + " thymines."


#1.7: Counting DNA Nucleotides by Base REMIX
counterA = 0
counterC = 0
counterG = 0
counterT = 0
for x in sequence:
   if "A"in x:
      counterA += 1
   if "C" in x:
       counterC += 1
   if "G" in x:
       counterG +=1
   if "T" in x:
       counterT +=1
print "It is", str(counterA/total), "% adenine."
print "It is", str(counterC/total), "% cytosine."
print "It is", str(counterG/total), "% guanine."
print "It is", str(counterT/total), "% thymine."


#1.8: Transcribing from DNA to mRNA
forward_mRNA = ""
for x in sequence:
   if "A" in x:
       forward_mRNA += "U"
   if "C" in x:
       forward_mRNA += "G"
   if "T" in x:
       forward_mRNA += "A"
   if "G" in x:
       forward_mRNA += "C"
print "The complementary mRNA for the DNA sequence ACTTGTCGAATCGGTGCCTGAAGTCGTGC is", forward_mRNA


#1.9: Designing Primers for GC content
counterC = 0
counterG = 0
for x in sequence:
   if "C" in x:
       counterC += 1
   if "G" in x:
       counterG +=1
print "It is", str((counterC + counterG)/total), "% GC content."



#Section 2: Lists and Dictionaries
#2.1: Finding the Range of Signal

green_sig = [20, 150, 35, 100, 120, 50, 180]
red_sig = [45, 65, 160, 160, 98, 142, 123]
blue_sig = [101, 120, 98, 67, 56, 200, 65]
yellow_sig = [160, 15, 39, 66, 70, 56, 100]

len_green_sig=len(green_sig)
print "The sequence length is", len_green_sig
print "The minimum green signal value is", min(green_sig), "and the maximum is", max(green_sig)



#2.2: Iterating Through a List
for x in range (len_green_sig):
   print green_sig[x]


#2.3: Finding the Index with Maximum Signal
index = 0
count = 0
for x in range(len_green_sig):
   if green_sig[x]>count:
       count = green_sig[x]
       index = x
print "The sequence index with the maximum value is", index


#2.4: Iterating Through Two Signal Channels Simultaneously
count = 0
for x in range(len_green_sig):
   if green_sig[x]>red_sig[x]:
       print "At position", x, "green signal is higher than red signal."
   else:
       print "At position", x, "red signal is higher than green signal."


#2.5: Concatenating Signal Results from Two Lists
list= []
for x in range(len_green_sig):
   if green_sig[x]>red_sig[x]:
       list.extend(['green'])
   else:
       list.extend(['red'])
print list



#2.6: Concatenating Four Signal Lists into One List
list= []
for x in range(len_green_sig):
   if green_sig[x]>red_sig[x] and green_sig[x]>yellow_sig[x] and green_sig[x]>blue_sig[x]:
       list.extend(['green'])
   if red_sig[x]>green_sig[x] and red_sig[x]>yellow_sig[x] and red_sig[x]>blue_sig[x]:
       list.extend(['red'])
   if yellow_sig[x]>green_sig[x] and yellow_sig[x]>red_sig[x] and yellow_sig[x]>blue_sig[x]:
       list.extend(['yellow'])
   if blue_sig[x]>green_sig[x] and blue_sig[x]>red_sig[x] and blue_sig[x]>yellow_sig[x]:
       list.extend(['blue'])
print list


#2.7: Converting Signal to Bases
list= []
for x in range(len_green_sig):
    if green_sig[x]>red_sig[x] and green_sig[x]>yellow_sig[x] and green_sig[x]>blue_sig[x]:
        list.extend(['A'])
    if red_sig[x]>green_sig[x] and red_sig[x]>yellow_sig[x] and red_sig[x]>blue_sig[x]:
        list.extend(['T'])
    if yellow_sig[x]>green_sig[x] and yellow_sig[x]>red_sig[x] and yellow_sig[x]>blue_sig[x]:
        list.extend(['G'])
    if blue_sig[x]>green_sig[x] and blue_sig[x]>red_sig[x] and blue_sig[x]>yellow_sig[x]:
        list.extend(['C'])

print "The DNA sequence is", "".join(list)
#print "The DNA sequence is", list
