#!/usr/bin/env python3

from reverseComplement import ReverseComplement


def hamming_distance_strings(str1: str, str2: str) -> int:
    """
    Calculate hamming distance between two strings of equal length

    Args:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        int: Hamming distance between the strings
    """
    if len(str1) != len(str2):
        return -1

    ham_dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            ham_dist += 1
    return ham_dist


def ApproxPatternMatching(pattern: str, genome: str, d: int) -> list:
    """
    Find all approximate occurrences of a pattern in a genome with at most d mismatches

    Args:
        pattern (str): Pattern to search for
        genome (str): Path to genome file to search in
        d (int): Maximum number of mismatches allowed

    Returns:
        list: List of starting positions where pattern appears with at most d mismatches
    """
    positions = []

    # Scan through genome
    for i in range(len(genome) - len(pattern) + 1):
        sliding_window = genome[i : i + len(pattern)]
        # Check if hamming distance between pattern and window is <= d
        if hamming_distance_strings(pattern, sliding_window) <= d:
            positions.append(i)

    # return " ".join(str(pos) for pos in positions)
    return positions


def neighborhood(pattern: str, d: int) -> str:
    """
    Find all neighbors of a pattern with at most d mismatches

    Args:
        pattern (str): Pattern to search for
        d (int): Maximum number of mismatches allowed

    Returns:
        list: List of neighbors of pattern with at most d mismatches
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "G", "C", "T"}

    neighbors = set()
    suffix_neighbors = neighborhood(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance_strings(pattern[1:], text) < d:
            for nucleotide in ["A", "G", "C", "T"]:
                neighbors.add(nucleotide + text)
        else:
            neighbors.add(pattern[0] + text)

    return neighbors


def frequentWordsWithMismatches(genome: str, k: int, d: int) -> list:
    """
    Find all frequent words with mismatches

    Args:
        genome (str): Path to genome file to search in
        k (int): String set size
        d (int): Maximum number of mismatches allowed

    Returns:
        list: List of frequent words with mismatches
    """
    frequent_words = {}

    for i in range(len(genome) - k + 1):
        pattern = genome[i : i + k]
        neighbors = list(neighborhood(pattern, d))
        for neighbor in neighbors:
            if neighbor in frequent_words:
                frequent_words[neighbor] += 1
            else:
                frequent_words[neighbor] = 1
  
    # find the most frequent word mismatches
    max_count = max(frequent_words.values())
    
    
    # return the most frequent word mismatches
    return [pattern for pattern, count in frequent_words.items() if count == max_count]


if __name__ == "__main__":
    with open("datasets/frequentMismatch_dataset.txt", "r") as file:

        genome = file.readline().strip()
        k, d = map(int, file.readline().split())
        print(f"k: {k}\nd: {d}")
    print(frequentWordsWithMismatches(genome, k, d))
   