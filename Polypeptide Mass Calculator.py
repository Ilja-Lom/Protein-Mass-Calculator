import csv

# necessary variables are initialised

# aa means 'amino acid'
aa_index = 0 # position of the aa in the 'amino_acids' list
amino_acids = [] # list including whole list of amino acids
aa_masses = [] # list of masses of the aa's in complementary order to 'amino_acids'
total_mass = 0 # total mass of the protein
n_aa = 0 # number of amino acids, starts at -1 because the number of water molecules is -1 amount of amino acids
repeat_loop = True # for the while loop to analyse the aa sequence


# classes for amino acid sequence processing

class Reading:
    """Reads the CSV file containing the amino acid residue masses"""
    
    def file(name_type):
        filename = 'Amino Acid Residue Masses.csv'
        
        with open(filename) as f:
            reader = csv.reader(f)
            
            for row in reader:
                amino_acid = str(row[name_type-1]) # selects row according to whether user wants to analyse full name aa, 3-letter name, or 1-letter name
                amino_acids.append(amino_acid.lower()) # adds the current amino_acid to the amino_acids list
                aa_mass = str(row[3]) # aa mass is in a constant row, no need to adjust according to a variable
                aa_masses.append(aa_mass) # aa mass is added into a list complementary to 'amino_acids'


class FullName:
    """Processes the user-given sequence if the sequence is written in full amino acid names"""
    
    def processing(aa_sequence, repeat_loop, total_mass, n_aa):
        while repeat_loop:
            try:
                comma = aa_sequence.index(",") # locates the index of the first comma
                aa = aa_sequence[0:comma] # the index of comma matches the last letter of the aa because reading begins at 0
                aa_index = amino_acids.index(aa) # locates index of the aa in the 'amino_acids' list, and stores value in a variable
                total_mass += float(aa_masses[aa_index]) # index of aa in 'amino_acids' is complementary to index of mass of aa in 'aa_masses'
                aa_sequence = aa_sequence[len(aa)+1:] # this calculates the start of the next amino acid by calculating the length of the current aa and adding 1 for the comma. That part of the string is then removed because of the : index
                n_aa += 1 # each loop means there is an additional amino acid
            except:
                repeat_loop = False # once an error is returned because there are no remaining aa, while loop stops repeating
                return(n_aa, total_mass)


class ThreeLetter:
    """Processes the user-given sequence if written in three-letter amino acid names"""
    def processing(aa_sequence, repeat_loop, total_mass, n_aa):
        while repeat_loop:
            try:
                aa = aa_sequence[:3]
                aa_index = amino_acids.index(aa)
                total_mass += float(aa_masses[aa_index])
                aa_sequence = aa_sequence[3:] # 3-letter names are used so the prefix of the sequence can be shortened by 3-units each loop repetition
                n_aa += 1
            except:
                repeat_loop = False
                return(n_aa, total_mass)


class OneLetter:
    """Processes the user-given sequence if written in one-letter amino acid names"""
    def processing(aa_sequence, repeat_loop, total_mass, n_aa):
        while repeat_loop:
            try:
                aa = aa_sequence[0]
                aa_index = amino_acids.index(aa)
                total_mass += float(aa_masses[aa_index])
                aa_sequence = aa_sequence[1:] # 1-letter names are used so the prefix of the sequence can be shortened by 1-unit each loop repetition
                n_aa += 1
            except:
                repeat_loop = False
                return(n_aa, total_mass)

# user inputs
aa_sequence = input("Enter the sequence:\n")
name_type = int(input("Select the name type of entry. 1 = full name. 2 = 3-letter name. 3 = 1-letter name:\n"))

# standardising the string sequence
aa_sequence = aa_sequence.lower()
aa_sequence = aa_sequence.replace(" ", "") # this will remove the whitespaces in the string
aa_sequence = aa_sequence + "," # adds a comma on the end of the sequence so that the full list of amino acids is read

# initialising analysis of the sequence
Reading.file(name_type) # loads amino acid csv file, and fills 'amino_acids', and 'aa_masses' lists
# selects correct class for the analysis of full-name, three-letter, or one-letter aa name sequence
if name_type == 1: # do not enter it as a string "1", it must be 1 by itself. Otherwise Python thinks it's a string not an integer value
    n_aa, total_mass = FullName.processing(aa_sequence, repeat_loop, total_mass, n_aa)
elif name_type == 2:
    n_aa, total_mass = ThreeLetter.processing(aa_sequence, repeat_loop, total_mass, n_aa)
elif name_type == 3:
    n_aa, total_mass = OneLetter.processing(aa_sequence, repeat_loop, total_mass, n_aa)


"""Water Mass Calculator"""
# use this if you are using the regular amino acid masses, not the residue mass
#water_mass = 18.01056*(n_aa - 1) # mass of water multiplied by how many molecules of water are produced
#print(f"""The mass of water produced: {water_mass}
#The mass of the protein: {total_mass - water_mass}
#""")

# printing results
print(f"""Number of amino acids in sequence: {n_aa}
The mass of the protein: {round(total_mass,5)}
""")


















