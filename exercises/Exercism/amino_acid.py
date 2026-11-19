
def proteins(rna):

    #Is a little too time complex, O(n^2), reworked to make it O(n)
    #     "Methionine": ["AUG"],
    #     "Phenylalanine": ["UUU", "UUC"],
    #     "Leucine": ["UUA", "UUG"],
    #     "Serine": ["UCU", "UCC", "UCA", "UCG"],
    #     "Tyrosine": ["UAU", "UAC"],
    #     "Cysteine": ["UGU", "UGC"],
    #     "Tryptophan": ["UGG"],
    #     "STOP": ["UAA", "UAG", "UGA"]

    rna_dict = {
        'AUG': 'Methionine',
        'UUC': 'Phenylalanine',
        'UUU': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAC': 'Tyrosine',
        'UAU': 'Tyrosine',
        'UGC': 'Cysteine',
        'UGU': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': "STOP",
        'UAG': "STOP",
        'UGA': "STOP"
        }

    codons = []

    for x in range(0,len(rna), 3):
        sliced_codon = rna[x:x+3]
        amino = rna_dict.get(sliced_codon)
        if amino == "STOP":
            return codons
        else:
            codons.append(amino)

    return codons

print(proteins("AUGUUUUCUUAAAUG"))