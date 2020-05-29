import blake3

# Booth's algorithm https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation#Booth's_Algorithm
def least_rotation(S: str) -> int:
    """Booth's algorithm."""
    S += S  # Concatenate string to it self to avoid modular arithmetic
    f = [-1] * len(S)  # Failure function
    k = 0  # Least rotation of string found so far
    for j in range(1, len(S)):
        sj = S[j]
        i = f[j - k - 1]
        while i != -1 and sj != S[k + i + 1]:
            if sj < S[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != S[k + i + 1]:  # if sj != S[k+i+1], then i == -1
            if sj < S[k]:  # k+i+1 = k
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k

def rotate_sequence(seq:str) -> str:
    r = least_rotation(seq)
    return "{}{}".format(seq,seq)[r:r+len(seq)]

def seqhash(seq:str,circular:bool=False) -> str:
    seq = seq.upper()
    if circular==True:
        seqhash=blake3.blake3(rotate_sequence(seq).encode('utf8'))
    else:
        seqhash=blake3.blake3(seq.encode('utf-8'))
    return seqhash.hexdigest()

