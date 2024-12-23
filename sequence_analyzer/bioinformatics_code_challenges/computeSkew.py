#!/usr/bin/env py


def compute_skew(genome: str) -> int:
    """
    Find the difference between the total number of occurrences of G and C in a genome

    Args:
        genome (str): target linear genome sequence

    Returns:
        int: difference in G and C position counts in the genome
    """
    # set skew initial start position
    skew = [0]

    for nucleotide in genome:
        # get previous skew position
        prev_skew = skew[-1]

        # check for C and G
        if nucleotide == "C":
            skew.append(prev_skew - 1)
        elif nucleotide == "G":
            skew.append(prev_skew + 1)
        else:
            skew.append(prev_skew)

    return skew


# if __name__ == "__main__":
#     # print(compute_skew("CATGGGCATCGGCCATACGCC"))
#     print(compute_skew("GAGCCACCGCGATA"))


def min_max_skew(genome: str) -> list:
    """
    Find the minimum/maximum skew position in a genome

    Args:
        genome (str): target linear genome sequence

    Returns:
        list: list of minimum/maximum skew positions in the genome
    """
    # compute skew
    skew = compute_skew(genome)

    # find minimum skew position
    min_skew = min(skew)
    max_skew = max(skew)

    # return all minimum positions
    # return [i for i, s in enumerate(skew) if s == min_skew]
    # return all maximum positions
    return [i for i, s in enumerate(skew) if s == max_skew]


if __name__ == "__main__":
    # genome ="datasets/Salmonella_full_genome.txt"
    # with open(genome, "r") as file:
        # genome = file.read().strip()
    
    # print(minimum_skew(genome))
    print(min_max_skew("GCATACACTTCCCAGTAGGTACTG"))
