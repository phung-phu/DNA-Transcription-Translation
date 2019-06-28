sequence = "ACTTGTCGAATCGGTGCCTGAAGTCGTGCGTAGC"
total = len(sequence)*1.0
print "hello",sequence
print total
print len(sequence)


for x in sequence:
   print x

if "-" in sequence:
   print "Missing bases detected"
else:
   print "No missing bases detected!"


counterA = 0
for x in sequence:
   if "A"in x:
       counterA += 1
print "It contains " + str(counterA) + " adenines."


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
print "It cointains " + str(counterC) + " cytosines."
print "It cointains " + str(counterG) + " guanines."
print "It cointains " + str(counterT) + " thymines."


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



counterC = 0
counterG = 0
for x in sequence:
   if "C" in x:
       counterC += 1
   if "G" in x:
       counterG +=1
print "It is", str((counterC + counterG)/total), "% GC content."




green_signal = [20, 150, 35, 100, 120, 50, 180]
print "The sequence length is", len(green_signal)
print "The minimum green signal value is", min(green_signal), "and the maximum is", max(green_signal)
