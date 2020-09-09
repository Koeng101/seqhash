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

def reverse_complement(seq:str) -> str:
    return seq.translate(str.maketrans("ATUGCYRSWKMBDHVNX","TAACGRYSWMKVHDBNY"))[::-1]

def seqhash_protein(seq:str) -> str:
    return seqhash(seq,circular=False, double_stranded=False, dna_type='protein')

def seqhash(seq:str,circular:bool=False,double_stranded=False,dna_type='DNA') -> str:
    seq = seq.upper()
    dna_types = {
            "DNA": "D",
            "RNA": "R",
            "PROTEIN": "P"}
    if circular==True:
        if double_stranded==True:
            rotated_sequence = rotate_sequence(seq)
            seqhash = blake3.blake3(min(rotated_sequence, reverse_complement(rotated_sequence)).encode('utf8'))
        else:
            seqhash = blake3.blake3(rotate_sequence(seq).encode('utf8'))
    else:
        if double_stranded==True:
            seqhash=blake3.blake3(min(seq,reverse_complement(seq)).encode('utf8'))
        else:
            seqhash=blake3.blake3(seq.encode('utf-8'))

    return "v1_{}{}{}_{}".format((dna_types[dna_type]),("C" if circular else "L"),("D" if double_stranded else "S"), seqhash.hexdigest())

