#!/usr/bin/env python3


def hamming_distance(g1: str, g2: str) -> int:
    """
    Calculate the hamming distance between two sequence strings

    Args:
        g1 (str): first sequence
        g2 (str): second sequence

    Returns:
        int: difference/mismatches between both sequences
    """
    count = 0

    if len(g1) != len(g2):
        return -1

    return sum(1 for i in range(len(g1)) if g1[i] != g2[i])


def get_kmers(sequence: str, k: int) -> list:
    """
    Gets all possible kmers from a DNA string

    Args:
        sequence (str): DNA sequence to get kmers from
        k (int): length of kmer

    Return:
        list: all kmers from the string
    """
    kmers = []

    # loop through sequence to get all k-length substrings
    seq_len = len(sequence)
    for i in range(seq_len - k + 1):
        # get substring of k
        kmers.append(sequence[i : i + k])
    return kmers


def neighbors(pattern: str, d: int) -> set:
    """
    Generate all possible patterns that differ from the input pattern by at most d mismatches

    Args:
        pattern (str): target k-mer pattern
        d (int): maximum num er of allowed mismatches

    Return:
        set: all possible patterns with up to d mismatches
    """
    nucleotides = {'A', 'C', 'G', 'T'}
    neighborhood = set()

    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    # get suffix neighbors
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in list(nucleotides): #['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    
    # add patterns that differ at the first position
    suffix_neighbors = neighbors(pattern[1:], d-1)
    for text in suffix_neighbors:
        for nucleotide in list(nucleotides): #['A', 'C', 'G', 'T']:
            if nucleotide != pattern[0]:
                neighborhood.add(nucleotide + text)
    
    return neighborhood


def MotifEnumeration(dna: list, k: int, d: int) -> str:
    """
    Find all the hidden k-mer motifs within a DNA sequence with specified mismatches

    Args:
        dna (list): target DNA sequences
        k (int): k-mer length
        d (int): number of mismatches

    Returns:
        set: all k-mer motifs matching the specified mismatch length
    """
    # set pattern set
    patterns = set()

    # get all k-mers from the first DNA string
    first_dna = dna[0]
    first_kmer = get_kmers(first_dna, k)

    # iterate over each kmer in the first dna string
    for pattern in first_kmer:
        # generate all mismatch kmers neighbors
        pattern_neighbors = neighbors(pattern, d)
        # check if each nieghbor appears in every DNA string with at most "d" mismatches
        for neighbor in pattern_neighbors:
            appears_in_all = True  # assume neighbor appears in all DNA string
            # check each DNA string
            for dna_string in dna:
                # get all k-mers in current dna string
                dna_kmers = get_kmers(dna_string, k)
                # check if any kmer in DNA string matches 'neighbor' with at most d mismatches
                found = False
                for dna_kmer in dna_kmers:
                    if hamming_distance(neighbor, dna_kmer) <= d:
                        found = True
                        break
                # if the neighbor does not appear in all DNA strings, not a valid motif
                if not found:
                    appears_in_all = False
                    break
            # if neighbor appears in all DNA strings, valid motif
            if appears_in_all:
                patterns.add(neighbor)

    return patterns


if __name__ == "__main__":
    # with open("datasets/motif_dataset.txt", "r") as file:
    #     k, d = map(int, file.readline().split())
    #     dna = file.readline().strip()
        
    dna = ["AAGGCCGCATCATGTGTTGCTTTTC", "ACTTGTCCACTAACTTGTTCTGCGC", "TCACATGTTCAGGACGACCGCTGCA", "ATTCCTGGCTTGTTCATTGTGCTCT", "GACGGACTTTTAACGTCTTCCCACC", "ATTTCTTTTCTATCTCATTCGCCGC"]    
    k = 5
    d = 1
   

    result = MotifEnumeration(dna, k, d)
    print(result)
