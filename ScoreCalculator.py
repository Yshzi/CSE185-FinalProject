'''
Calculates the score of the output sequences of a MAFFT alignment.
A value of 1 is added to the score if the character at the current
index of the 3 sequences are equal. 

returns score
'''

def CalculateScore(s1, s2, s3):
    if len(s1) != len(s2) and len(s3):
        raise ValueError("All sequences must have the same length")
    
    score = 0
    for s1, s2, s3 in zip(s1, s2, s3):
        if s1 == s2 == s3:
            score += 1

    return score


