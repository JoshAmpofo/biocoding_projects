#!/usr/bin/env python3


def hamming_distance(g1: str, g2: str) -> int:
    """
    Compute the Hamming Distance (difference in nucleotides) between two genomes

    Args:
        g1 (str): First genome
        g2 (str): Second genome

    Returns:
        int: Hamming Distance
    """
    with open(g1, "r") as file1, open(g2, "r") as file2:
        g1 = file1.read().strip()
        g2 = file2.read().strip()
        
    # check if len of g1 and g2 are the same
    if len(g1) != len(g2):
        return f"Error. Genomes must be of the same length."
    # initialize hamming distance
    ham_dist = 0
    # interate through both genomes
    for nucleotide in range(len(g1)):
        # compare each character in g1 with g2
        if g1[nucleotide] != g2[nucleotide]:
            # if they are not the same, add 1 to hamming distance
            ham_dist += 1
    # return hamming distance
    return ham_dist


if __name__ == "__main__":
    g1 = "datasets/ham_dist_d1.txt" 
    g2 = "datasets/ham_dist_d2.txt"
    print(hamming_distance(g1, g2))

