import sys
'''
ScoreCalculor.py is a python script that takes in a text file
containing the 3 sequence alignment with no headers and returns
the score and length of the alignment.
'''

'''
Calculates the score of the alignment of three sequences.
A value of 1 is added to the score if the character at the
index of the 3 sequences is the same. 
'''
def CalculateScore(s1, s2, s3):
    if len(s1) != len(s2) and len(s3):
        raise ValueError("All sequences must have the same length")
    
    score = 0
    for s1, s2, s3 in zip(s1, s2, s3):
        if s1 == s2 == s3:
            score += 1

    return score

# Get the FASTA file path from the command-line argument
file_path = sys.argv[1]

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("python ScoreCalculator.py [alignments file]")
    sys.exit(1)

sequences = []
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('>'):
            continue
        sequences.append(line.strip())

# Prints the alignment score and alignment length of an alignment
print('Alignment score: ' + str(CalculateScore(sequences[0], sequences[1], sequences[2])))
print('Aligntment length: ' + str(len(sequences[0])))

