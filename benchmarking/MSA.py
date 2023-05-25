import sys

def mlcs(s1, s2, s3):
    m, n, o = len(s1), len(s2), len(s3)
    dp = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, o+1):
                dp[i][j][k] = max(
                    dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1],
                    dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1],
                    dp[i-1][j-1][k-1] + (1 if s1[i-1] == s2[j-1] == s3[k-1] else 0)
                )
                    
                dp[i][j][k] = max(
                    dp[i-1][j][k],
                    dp[i][j-1][k], 
                    dp[i][j][k-1],
                    dp[i-1][j-1][k],
                    dp[i-1][j][k-1],
                    dp[i][j-1][k-1],
                    dp[i-1][j-1][k-1] + (+1 if (s1[i-1] == s2[j-1] == s3[k-1]) else +0),
                )

    # backtracking
    i, j, k = m, n, o
    align_s1, align_s2, align_s3 = [], [], []

    while i > 0 and j > 0 and k > 0:
 
        
        ##the if false to help moving all the elif below 
        if False:
            ""
            
        elif dp[i][j][k] == dp[i-1][j-1][k-1] + (1 if s1[i-1] == s2[j-1] == s3[k-1] else 0):
            align_s1.append(s1[i-1])
            align_s2.append(s2[j-1])
            align_s3.append(s3[k-1])
            i -= 1
            j -= 1
            k -= 1        
        
        elif dp[i][j][k] == dp[i-1][j][k]:
            align_s1.append(s1[i-1])
            align_s2.append('-')
            align_s3.append('-')
            i -= 1
        elif dp[i][j][k] == dp[i][j-1][k]:
            align_s1.append("-")
            align_s2.append(s2[j-1])
            align_s3.append("-")
            j -= 1
        elif dp[i][j][k] == dp[i][j][k-1]:
            align_s1.append("-")
            align_s2.append("-")
            align_s3.append(s3[k-1])
            k -= 1
        
        elif dp[i][j][k] == dp[i-1][j-1][k] +1:
            align_s1.append(s1[i-1])
            align_s2.append(s2[j-1])
            align_s3.append('-')
            i -= 1
            j -= 1
        
        elif dp[i][j][k] == dp[i-1][j][k-1] +1:
            align_s1.append(s1[i-1])
            align_s2.append('-')
            align_s3.append(s3[k-1])
            i -= 1
            k -= 1
        elif dp[i][j][k] == dp[i][j-1][k-1] +1:
            align_s1.append('-')
            align_s2.append(s2[j-1])
            align_s3.append(s3[k-1])
            j -= 1
            k -= 1
            
    # fill left
    while i > 0 and j > 0:
        align_s1.append(s1[i-1])
        align_s2.append(s2[j-1])
        align_s3.append('-')
        i -= 1
        j -= 1
    while i > 0 and k > 0:
        align_s1.append(s1[i-1])
        align_s2.append('-')
        align_s3.append(s3[j-1])
        i -= 1
        k -= 1
    while j > 0 and k > 0:
        align_s1.append('-')
        align_s2.append(s2[i-1])
        align_s3.append(s3[k-1])
        j -= 1
        k -= 1
        
    while i > 0:
        align_s1.append(s1[i-1])
        align_s2.append('-')
        align_s3.append('-')
        i -= 1
    while j > 0:
        align_s1.append('-')
        align_s2.append(s2[j-1])
        align_s3.append('-')
        j -= 1
    while k > 0:
        align_s1.append('-')
        align_s2.append('-')
        align_s3.append(s3[k-1])
        k -= 1    
            
    return dp[m][n][o], "".join(align_s1[::-1]), "".join(align_s2[::-1]), "".join(align_s3[::-1])


# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("python mlcs.py [fasta_file]")
    sys.exit(1)

# Get the FASTA file path from the command-line argument
fasta_file = sys.argv[1]

# Read the sequences from the FASTA file
sequences = []
sequence_names = []  # Initialize the sequence_names list
with open(fasta_file, 'r') as file:
    sequence = ""
    for line in file:
        if line.startswith('>'):
            if sequence:
                sequences.append(sequence)
                sequence = ""
            sequence_names.append(line.strip()[1:])
        else:
            sequence += line.strip()
    sequences.append(sequence)

# Check if at least 3 sequences are present
if len(sequences) < 3:
    print("Error: The FASTA file should contain at least 3 sequences.")
    sys.exit(1)

# Extract the first 3 sequences from the list
s1 = sequences[0]
s2 = sequences[1]
s3 = sequences[2]

# Call the function with the provided sequences
result = mlcs(s1, s2, s3)

# Print the alignment result with sequence names
alignment_score, aligned_s1, aligned_s2, aligned_s3 = result
print("Alignment Score:", alignment_score)
print(sequence_names[0] + ":", aligned_s1)
print(sequence_names[1] + ":", aligned_s2)
print(sequence_names[2] + ":", aligned_s3)


