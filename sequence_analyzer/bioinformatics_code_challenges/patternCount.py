#!/usr/bin/env python3

"""
Define an algorithm that will take in a string of text and a substructure or pattern
and return the number of times that pattern exists in the text using sliding window technique
"""


def PatternCount(text: str, pattern: str) -> int:
    """
    Determine the pattern count in text string using sliding window technique

    Args:
        text (str): text string
        pattern (str): pattern to search for in text string

    Return:
        int: pattern count and index positions
    """
    # Validate inputs
    if not pattern or len(pattern) > len(text):
        return 0

    count = 0
    window_size = len(pattern)
    text = text.upper().strip()
    positions = []

    # Slide the window through the text
    for i in range(len(text) - window_size + 1):
        # Check if current window matches the pattern
        if text[i : i + window_size] == pattern:
            count += 1
            positions.append(i)
            
    return f"Text: {text}\nPattern: {pattern}\nCount: {count}\nPositions: {positions}"


if __name__ == "__main__":
    # print(PatternCount("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC", "ATTCTGACT"))
    # print(PatternCount("GCGCG", "GCG"))
    print(PatternCount("GATATATGCATATACTT", "ATAT"))
    
    
def findPosition(pattern: str, genome: str) -> list:
    # read genome from a file on the command line
    with open(genome, "r") as f:
        genome = f.read().strip()

    positions = []

    for i in range(len(genome) - len(pattern) + 1):
        if genome[i : i + len(pattern)] == pattern:
            positions.append(i)

    return positions


genome = "Vibrio_cholerae.txt"
# print(findPosition("CTTGATCAT", genome=genome))
print(findPosition("ATGATCAAG", genome=genome))