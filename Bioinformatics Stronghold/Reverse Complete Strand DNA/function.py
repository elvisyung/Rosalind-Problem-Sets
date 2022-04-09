trans = ''                             
with open('rosalind_revc.txt') as f:      
    for line in f:                     
        for nt in line:                
            if nt == 'A':              
                trans+='T'             
            elif nt == 'C':            
                trans+='G'             
            elif nt == 'T':            
                trans+='A'             
            elif nt == 'G':            
                trans+='C'             
reverse = trans[::-1]                  
with open('compdna.txt','w') as answer:
    answer.write(reverse)      

# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print st

# from Bio.Seq import Seq

# file = open("rosalind2.txt", "r")
# s = file.read()
# seq = Seq(s)
# seq.reverse_complement()
# print seq.reverse_complement()