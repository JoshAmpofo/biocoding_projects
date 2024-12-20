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
    return sum(1 for i in range(len(str1)) if str1[i] != str2[i])

    # ham_dist = 0
    # for i in range(len(str1)):
    #     if str1[i] != str2[i]:
    #         ham_dist += 1
    # return ham_dist

# def neighborhood(pattern: str, d: int) -> str:
#     """
#     Find all neighbors of a pattern with at most d mismatches

#     Args:
#         pattern (str): Pattern to search for
#         d (int): Maximum number of mismatches allowed

#     Returns:
#         list: List of neighbors of pattern with at most d mismatches
#     """
#     if d == 0:
#         return {pattern}
#     if len(pattern) == 1:
#         return {"A", "G", "C", "T"}

#     neighbors = set()
#     suffix_neighbors = neighborhood(pattern[1:], d)

#     for text in suffix_neighbors:
#         if hamming_distance_strings(pattern[1:], text) < d:
#             for nucleotide in ["A", "G", "C", "T"]:
#                 neighbors.add(nucleotide + text)
#         else:
#             neighbors.add(pattern[0] + text)

#     # return neighbors with comma separator removed
#     neighbors = list(neighbors)
#     return sorted(neighbors)

def neighborhood(pattern: str, d: int) -> list:
    """
    Find all neighbors of a pattern with at most d mismatches using iterative approach

    Args:
        pattern (str): Pattern to search for
        d (int): Maximum number of mismatches allowed

    Returns:
        list: Sorted list of neighbors of pattern with at most d mismatches
    """
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = {pattern}
    
    # Iterate through each possible number of mismatches up to d
    for dist in range(1, d + 1):
        current_neighbors = set()
        # For each pattern we've found so far
        for pat in neighbors:
            # Try changing each position
            for i in range(len(pat)):
                # Convert string to list for efficient character replacement
                pat_list = list(pat)
                # Try each possible nucleotide at this position
                for nuc in nucleotides:
                    if pat_list[i] != nuc:
                        pat_list[i] = nuc
                        current_neighbors.add(''.join(pat_list))
        neighbors.update(current_neighbors)

    return sorted(list(neighbors))

if __name__ == "__main__":
    print(neighborhood("GCGGTAGGAGA", 3))