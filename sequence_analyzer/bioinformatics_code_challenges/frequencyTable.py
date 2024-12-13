#!/usr/bin/env python3

from patternCount import PatternCount


def FrequencyTable(text: str, k: int) -> int:
    """
    A function that counts the highest occurrence of a string set in a string

    Args:
        text (str): target text to search for occurrence
        k (int): string set number

    Return:
        tuple: (pattern with highest frequency, number of occurrences)
    """
    # create a dictionary to store pattern frequencies
    freq = {}
    text = text.upper().strip()
    text_length = len(text)

    # loop through the string
    for i in range(text_length - k):
        pattern = text[i : i + k]
        # store pattern and its count
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1

    # find pattern with maximum frequency
    max_count = max(freq.values())

    # find all patterns with maximum frequency
    max_patterns = [pattern for pattern, count in freq.items() if count == max_count]

    return max_patterns


if __name__ == "__main__":
    # print(FrequencyTable("AAAGTCTTTCTGCCGGG", 3))
    # print(FrequencyTable("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
    # print(FrequencyTable("TGGACGTTGGCCCAGCTGGTCCCACGTGGT", 3))
    # print(FrequencyTable("CGTTTTGAACATTTTCAACAAGTTTTGCAACATTTT", 4))
    # print(FrequencyTable("GTTGGGTTGGAACAACAACAACAACAAGTTGGGTTGG", 5))
    # print(FrequencyTable("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
    # print(FrequencyTable("ACTACCATGGAGTGGCGGTACTACCATGGGTGGCTACCGTGGCTACCCGTGTTTCAGTGGCGGTGTGGCTACCCGTGTTTCACTACCATGGCGTGTTTCACTACCATGGCGTGTTTCGTGGCTACCAGTGGCGGTAGTGGCGGTCACTTACTACCACTTACTACAGTGGCGGTCACTTACTACACTACCATGGCACTTACTACAGTGGCGGTCACTTACTACAGTGGCGGTAGTGGCGGTGTGGCTACCGTGGCTACCGTGGCTACCGTGGCTACCCGTGTTTCGTGGCTACCACTACCATGGAGTGGCGGTAGTGGCGGTGTGGCTACCCGTGTTTCCACTTACTACCGTGTTTCGTGGCTACCCGTGTTTCCACTTACTACCACTTACTACCGTGTTTCCGTGTTTCCGTGTTTCAGTGGCGGTAGTGGCGGTACTACCATGGCACTTACTACCACTTACTACCACTTACTACCGTGTTTCACTACCATGGAGTGGCGGTCGTGTTTCCGTGTTTCACTACCATGGCACTTACTACACTACCATGGACTACCATGGGTGGCTACCAGTGGCGGTGTGGCTACCCGTGTTTCGTGGCTACCACTACCATGGCGTGTTTCGTGGCTACCACTACCATGGCACTTACTACACTACCATGGGTGGCTACCCACTTACTACGTGGCTACCGTGGCTACCGTGGCTACCACTACCATGGCGTGTTTCGTGGCTACCGTGGCTACCCGTGTTTCCGTGTTTCCGTGTTTCCGTGTTTCACTACCATGGGTGGCTACCCGTGTTTCACTACCATGGCACTTACTACACTACCATGGCGTGTTTCCACTTACTACCACTTACTACAGTGGCGGTACTACCATGGGTGGCTACCAGTGGCGGTCGTGTTTCGTGGCTACCCACTTACTACCGTGTTTCAGTGGCGGTCGTGTTTCGTGGCTACCCACTTACTACCGTGTTTCACTACCATGG", 11))
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            3,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            4,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            5,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            6,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            7,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            8,
        )
    )
    print(
        FrequencyTable(
            "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
            9,
        )
    )
