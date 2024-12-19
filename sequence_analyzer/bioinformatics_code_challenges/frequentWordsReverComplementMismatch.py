def reverse_complement(pattern: str) -> str:
    """
    Find the reverse complement of a DNA string

    Args:
        pattern (str): DNA string

    Returns:
        str: Reverse complement of the DNA string
    """
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement[base] for base in reversed(pattern))


def hamming_distance(str1: str, str2: str) -> int:
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


def neighborhood(pattern: str, d: int) -> set:
    """
    Find all neighbors of a pattern with at most d mismatches

    Args:
        pattern (str): Pattern to search for
        d (int): Maximum number of mismatches allowed

    Returns:
        set: Set of neighbors of pattern with at most d mismatches
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighbors = set()
    suffix_neighbors = neighborhood(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ["A", "C", "G", "T"]:
                neighbors.add(nucleotide + text)
        else:
            neighbors.add(pattern[0] + text)
    return neighbors


def count_approximate_occurrences(text: str, pattern: str, d: int) -> int:
    """
    Count the number of approximate occurrences of a pattern in text

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for
        d (int): Maximum number of mismatches allowed

    Returns:
        int: Number of approximate occurrences
    """
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i : i + k]) <= d:
            count += 1
    return count


def frequent_words_with_mismatches_and_rc(text: str, k: int, d: int) -> list:
    """
    Find the most frequent k-mers (with mismatches and reverse complements) in a string

    Args:
        text (str): Input DNA string
        k (int): Length of k-mer
        d (int): Maximum number of mismatches allowed

    Returns:
        list: Most frequent k-mers with mismatches and reverse complements
    """
    patterns = {}
    n = len(text)

    # Generate all possible k-mers from the text and their neighborhoods
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        neighborhood_patterns = neighborhood(pattern, d)

        # For each neighbor, count occurrences of both it and its reverse complement
        for neighbor in neighborhood_patterns:
            if neighbor not in patterns:
                rc = reverse_complement(neighbor)
                count = count_approximate_occurrences(text, neighbor, d)
                count_rc = count_approximate_occurrences(text, rc, d)
                patterns[neighbor] = count + count_rc

    # Find the maximum count
    if not patterns:
        return []
    max_count = max(patterns.values())

    # Return all patterns that achieve the maximum count
    return sorted(pattern for pattern, count in patterns.items() if count == max_count)



if __name__ == "__main__":
    with open(
        "datasets/frequentComplement_dataset.txt", "r"
    ) as file:

        genome = file.readline().strip()
        k, d = map(int, file.readline().split())
        print(f"k: {k}\nd: {d}")
    result = frequent_words_with_mismatches_and_rc(genome, k, d)
    print(" ".join(result))
