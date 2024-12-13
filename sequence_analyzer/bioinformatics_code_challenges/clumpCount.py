#!/usr/bin/env python3

from collections import defaultdict

def DistinctClumpCount(file_path: str, k: int, L: int, t: int) -> int:
    """
    Finds the number of distinct k-mers forming (L, t)-clumps in a genome.

    Args:
        file_path (str): Path to the file containing the genome sequence.
        k (int): Length of k-mers.
        L (int): Length of the window to search within.
        t (int): Minimum number of occurrences for a k-mer to form a clump.

    Returns:
        int: Number of distinct k-mers forming clumps.
    """
    try:
        # Read the genome from the file
        with open(file_path, "r") as file:
            genome = file.read().strip().upper()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

    n = len(genome)
    clump_kmers = set()
    freq = defaultdict(int)

    # Initialize the first window
    for i in range(L - k + 1):
        kmer = genome[i:i + k]
        freq[kmer] += 1

    # Add k-mers forming clumps in the first window
    for kmer, count in freq.items():
        if count >= t:
            clump_kmers.add(kmer)

    # Slide the window across the genome
    for i in range(1, n - L + 1):
        # Remove the k-mer going out of the window
        outgoing_kmer = genome[i - 1:i - 1 + k]
        freq[outgoing_kmer] -= 1
        if freq[outgoing_kmer] == 0:
            del freq[outgoing_kmer]  # Clean up to save space

        # Add the k-mer coming into the window
        incoming_kmer = genome[i + L - k:i + L]
        freq[incoming_kmer] += 1

        # Check if the new k-mer forms a clump
        if freq[incoming_kmer] >= t:
            clump_kmers.add(incoming_kmer)

    # Return the number of distinct clump-forming k-mers
    return len(clump_kmers)


file_path = "E_coli.txt"
k = 9
L = 500
t = 3

result = DistinctClumpCount(file_path, k, L, t)
print(result)