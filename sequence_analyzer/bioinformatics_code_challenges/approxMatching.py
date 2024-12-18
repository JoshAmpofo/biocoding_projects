#!/usr/bin/env python3


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


# if __name__ == "__main__":
#     with open("datasets/ApproxMatching_dataset.txt", "r") as file:
#         lines = file.readlines()

#     pattern = lines[0].strip()
#     genome = lines[1].strip()
#     d = int(lines[2].strip())
#     print(
#         ApproxPatternMatching(
#             pattern,
#             genome,
#             d,
#         )
#     )
    


def ApproxPatternCount(pattern: str, genome: str, d: int) -> int:
    """
    Find the total count of patterns with mismatches
    
    Args:
        pattern (str): Pattern to search for
        genome (str): Path to genome file to search in
        d (int): Maximum number of mismatches allowed
        
    Return:
        int: Number of patterns with mismatches 
    """
    positions = ApproxPatternMatching(pattern, genome, d)
    total_occurrences = len(positions)
    return f"Positions: {positions}\nOccurrences: {total_occurrences}"


if __name__ == "__main__":
    with open("datasets/approxCount_dataset.txt", "r") as file:
        lines = file.readlines()

    pattern = lines[0].strip()
    genome = lines[1].strip()
    d = int(lines[2].strip())
    print(
        ApproxPatternCount(
            pattern,
            genome,
            d,
        )
    )