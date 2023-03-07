from Bio import SeqIO

file_type = 'fasta'
file_path_1 = 'aligned_fasta_files/B - NC_045512.2.fa'
file_path_2 = 'aligned_fasta_files/B.1.1.519 - OK341237.1.fa'

bio_seq_1 = SeqIO.read(file_path_1, file_type)
bio_seq_2 = SeqIO.read(file_path_2, file_type)

str1 = str(bio_seq_1.seq)
str2 = str(bio_seq_2.seq)

#Defines function find_mutations
def find_mutations(startPosition, endPosition, out):
  for x in range (0,len(str1)):
      reference = str1[x]
      target = str2[x]
      if str1[x] != str2[x] and startPosition <= x <= endPosition:
        out.append(x+1)
        out.append(reference)
        out.append(target)

#Sections out sections of base pairs. To add a new sequence, use the following template (without #):
#NAME = []
#find_mutations(startPosition, endPosition, NAME)
#print("whatever you want to show")
#print(NAME)

FIVEUTR = []
find_mutations(0, 264, FIVEUTR)
print("5 UTR")
print(FIVEUTR)

NSP1 = []
find_mutations(265, 804, NSP1)
print ("Leader protein; NSP1 produced by both pp1a and pp1ab")
print(NSP1)

NSP2 = []
find_mutations(805, 2718, NSP2)
print ("NSP2; produced by both pp1a and pp1ab")
print(NSP2)

NSP3 = []
find_mutations(2719, 8553, NSP3)
print ("NSP3; former nsp1; conserved domains are: Nterminal acidic (Ac), predicted phosphoesterase, papain-likeproteinase, Y-domain, transmembrane domain 1 (TM1),adenosine diphosphate-ribose 1''-phosphatase (ADRP);produced by both pp1a and pp1ab")
print(NSP3)

NSP4 = []
find_mutations(8554, 10053, NSP4)
print ("NSP4 contains transmembrane domain 2 (TM2) produced by both pp1a and pp1ab")
print(NSP4)

NSP5A = []
find_mutations(10054, 10971, NSP5A)
print ("3C-LIKE PROTEINASE; nsp5A_3CLpro and nsp5B_3CLpro; main proteinase (Mpro); mediates cleavages downstream of nsp4. 3D structure of the SARSr-CoV homolog has been determined produced by both pp1a and pp1ab")
print(NSP5A)

NSP6 = []
find_mutations(10972, 11841, NSP6)
print ("NSP6putative transmembrane domain; produced by both pp1a and pp1ab")
print(NSP6)

NSP7 = []
find_mutations(11482, 12090, NSP7)
print ("NSP7; produced by both pp1a and pp1ab")
print(NSP7)

NSP8 = []
find_mutations(12091, 12684, NSP8)
print ("NSP8; produced by both pp1a and pp1ab")
print(NSP8)

NSP9 = []
find_mutations(12685, 13024, NSP9)
print ("NSP9; ssRNA-binding protein; produced by both pp1a and pp1ab")
print(NSP9)

NSP10 = []
find_mutations(13024, 13440, NSP10)
print ("NSP10; CysHis; formerly known as growth-factor-like protein (GFL); produced by both pp1a and pp1ab")
print(NSP10)

NSP12 = []
find_mutations(13441, 16235, NSP12)
print ("RNA-dependent RNA polymerase; nsp12; NiRAN and RdRp; produced by pp1ab only")
print(NSP12)

NSP13 = []
find_mutations(16236, 18038, NSP13)
print ("BD, nsp13_TB, and nsp_HEL1core; helicase; zinc-binding domain (ZD), NTPase/helicase domain (HEL), RNA 5'-triphosphatase; produced by pp1ab only")
print(NSP13)

NSP14 = []
find_mutations(18039, 19619, NSP14)
print ("nsp14A2_ExoN and nsp14B_NMT; 3'-to-5' exonuclease; produced by pp1ab only")
print(NSP14)

NSP15 = []
find_mutations(19620, 20657, NSP15)
print ("nsp15-A1 and nsp15B-NendoU; endoRNAse; produced by pp1ab only")
print(NSP15)

NSP16 = []
find_mutations(20658, 21551, NSP16)
print ("nsp16_OMT; 2'-o-MT; 2'-O-ribose methyltransferase; produced by pp1ab only")
print(NSP16)

SPIKE = []
find_mutations(21563, 25384, SPIKE)
print ("Spike")
print(SPIKE)

ORF3A = []
find_mutations(25393, 26220, ORF3A)
print ("ORF3a")
print(ORF3A)

ENVELOPE = []
find_mutations(26245, 226472, ENVELOPE)
print ("Envelope")
print(ENVELOPE)

MEMBRANE = []
find_mutations(26523, 27191, MEMBRANE)
print ("Membrane glycoprotein")
print(MEMBRANE)

ORF6 = []
find_mutations(27202, 27387, ORF6)
print ("ORF6")
print(ORF6)

ORF7A = []
find_mutations(27394, 27759, ORF7A)
print ("ORF7a")
print(ORF7A)

ORF7B = []
find_mutations(27756, 27887, ORF7B)
print ("ORF7b")
print(ORF7B)

ORF8 = []
find_mutations(27894, 28259, ORF8)
print ("ORF8")
print(ORF8)

N = []
find_mutations(28274, 29533, N)
print ("nucleocapsid phosphoprotein")
print(N)

ORF10 = []
find_mutations(29558, 29674, ORF10)
print ("ORF10")
print(ORF10)

THREEUTR = []
find_mutations(29675, 29903, THREEUTR)
print ("3UTR")
print(THREEUTR)