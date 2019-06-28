#1.1 Get all the codons
mRNA = 'AUGUGCCGAGUGCAGUGA'

print(mRNA[0:3])
print(mRNA[3:6])
print(mRNA[6:9])
print(mRNA[9:12])
print(mRNA[12:15])
print(mRNA[15:18])


#1.2 Get all the codons... with a for loop
codon_len = int(len(mRNA)/3)
for x in range(codon_len):
   print(mRNA[3*x:3*x+3])


#1.3 Save the codons
codon_list = []
codon_len = int(len(mRNA)/3)
for x in range(codon_len):
    codon = (mRNA[3*x:3*x+3])
###    print codon
    codon_list+=[codon]
##print codon_list


#2.1 Translate a codon to an amino acid

genetic_code = {'ACC': 'T', 'GUC': 'V', 'ACA': 'T', 'ACG': 'T', 'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UAU': 'Y', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'GGU': 'G', 'GGG': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'UGA': 'X', 'UGG': 'W', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'UCC': 'S', 'UCA': 'S', 'GAA': 'E', 'UAA': 'X', 'GGA': 'G', 'UAC': 'Y', 'CGU': 'R', 'UAG': 'X', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAG': 'K', 'GAU': 'D', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'CGA': 'R', 'GCU': 'A', 'UGU': 'C', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

codon = "AUG"
print genetic_code[codon]
#OR:
if "AUG" in genetic_code:
   print genetic_code["AUG"]



#2.2 Translate a piece of mRNA
genetic_code_total = ""
for x in codon_list:
    genetic_code_total+=genetic_code[x]
print genetic_code_total


#2.3 Apply this to your mRNA!
