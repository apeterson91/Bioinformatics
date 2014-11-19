import collections
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC,generic_dna

#Reference: 
AAs=["G","A","S","P","V","T","C","I","L","N","D","K","Q","E","M","H","F","R","Y","W"]
AAs_mass=[57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]

def find_peptide(Text,Peptide):
    Text=Seq(Text,IUPAC.ambiguous_dna)
    textlength=len(str(Text))
    num_nucleotides=len(Peptide)*3
    sequencesofinterest=[]
    i=0
    while i<textlength-num_nucleotides:
        codonsofinterest=Text[i:i+num_nucleotides]
        complement=codonsofinterest.reverse_complement()
        i+=1
        try:
            if str(codonsofinterest.translate())==Peptide or str(complement.translate())==Peptide:
                sequencesofinterest.append(str(codonsofinterest))
        except:
            print i
    return sequencesofinterest
    
def num_subpeptides(n):
    return (n-1)*n 

def find_mass(Peptide):
    AAs={"G": 57,"A": 71,"S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186}
    mass=0
    for i in Peptide:
        mass+=AAs[i]
    return mass

def LinearSpectrum(Peptide,AminoAcid,AminoAcidMass):
    PrefixMasses=[0]
    for i in range(0,len(Peptide)):
        for j in range(0,20):
            if AminoAcid[j]==Peptide[i]:
                PrefixMasses.append(PrefixMasses[i]+AminoAcidMass[j])
    LinearSpec=[0]
    for i in range(0,len(Peptide)):
        for j in range(i+1,len(Peptide)+1):
            LinearSpec.append(PrefixMasses[j]-PrefixMasses[i])
    LinearSpec.sort()
    return LinearSpec
    
def CyclicSpectrum(Peptide,AminoAcid,AminoAcidMass):
    PrefixMasses=[0]
    for i in range(0,len(Peptide)):
        for j in range(0,20):
            if AminoAcid[j]==Peptide[i]:
                PrefixMasses.append(PrefixMasses[i]+AminoAcidMass[j])
    peptideMass= PrefixMasses[len(Peptide)]
    CyclicSpec=[0]
    for i in range(0,len(Peptide)):
        for j in range(i+1,len(Peptide)+1):
            CyclicSpec.append(PrefixMasses[j]-PrefixMasses[i])
            if i>0 and j<len(Peptide):
                CyclicSpec.append(peptideMass-(PrefixMasses[j]-PrefixMasses[i]))
    CyclicSpec.sort()
    return CyclicSpec
    
#returns unique list elements from input list
def findUnique(listofinterest):
    unique=[]
    for i in listofinterest:
        if i not in unique:
            unique.append(i)
    return unique
    
# determines all singular amino acids whose masses are found within experimental spectrum input 
#Input: Empty list of Peptides, Experimental Spectrum, Reference Lists
#Output: Emtpy 
def InitializePeptides(Peptides,ExperimentalSpectrum,AAs_mass,AAs):
    for i in range(len(ExperimentalSpectrum)):
        for j in range(20):
            if AAs_mass[j]==ExperimentalSpectrum[i]:
                Peptides.append(AAs[j])
    return Peptides
    

#Adds on each Amino Acid to a prexisting list "Peptides", returning that list, also removes initial peptides from input list
#Input:Peptides list, Reference Arrays
#Output: "Expanded" list of Peptides
def Expand(Peptides,AAs_mass,AAs):
    Expanders=list(Peptides)
    for AminoAcid in Expanders:
        for i in AAs:
            Peptides.append(str(AminoAcid+i))
    for AminoAcid in Expanders:
        if AminoAcid in Peptides:
            Peptides.remove(AminoAcid)
    return Peptides
    
#Input= two lists (Spectra)
#Output= Boolean denoting whether every value in ProposedPeptide Spec can be found in the Experimental
def Spectrum_Consistent(ProposedPeptideSpec,ExperimentalPeptideSpec):
    duplicates={};dups=[x for x, y in collections.Counter(ProposedPeptideSpec).items() if y > 1]
    for dup in dups:
        duplicates[dup]=dups.count(dup)
    for mass in ProposedPeptideSpec:
        if mass not in ExperimentalPeptideSpec:
            return False
        elif mass in dups:
            if ProposedPeptideSpec.count(mass)!=duplicates[mass]:
                return False
    return True

def readindata(filename):
    f=open(filename,"r")#read in quiz data
    QuizInput=f.read()
    QuizDataInput=[]
    Data=QuizInput.split(" ")
    for datum in Data:
        QuizDataInput.append(int(datum))
    f.close()
    return QuizDataInput
