#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction


def seq_length(seq: str) -> int:
    """
    Calculate the length of a given sequence

    Args:
        seq (str): Sequence to calculate length

    Returns:
        int: Length of sequence
    """
    seq = Seq(seq.upper().strip())
    return len(seq)


def calc_gc_content(seq: str) -> str:
    """
    Calculate the GC content of a given sequence

    Args:
        seq (str): Sequence to calculate GC content of

    Returns:
        str: GC content of sequence
    """
    seq = Seq(seq.upper().strip())
    try:
        gc_decimal = gc_fraction(seq)
        gc_percent = gc_decimal * 100
        return f"\nGC content (dec): {gc_decimal}\nGC content (%): {gc_percent:.3f}"
    except (ValueError, TypeError, NameError):
        return "Invalid sequence"


def find_orf(seq: str) -> list:
    """Find open reading frames (ORFs) in a given DNA sequence

    An open reading frame (ORF) is a sequence of codons that starts with a start codon
    and ends with a stop codon, with no intervening stop codons.

    Args:
        seq (str): DNA sequence, should be uppercase

    Returns:
        list: list of dictionaries containing ORF information (sequence, start position, length)
    """
    seq = seq.upper()  # Convert to uppercase to ensure consistency
    orfs = []

    # Check all three possible reading frames
    for frame in range(3):
        i = frame
        while i < len(seq) - 2:  # Need at least 3 nucleotides for a codon
            codon = seq[i : i + 3]

            # If we find a start codon
            if codon in ["ATG", "GTG", "TTG"]:
                start_pos = i
                orf = []
                j = i

                # Keep reading codons until we hit a stop codon or end of sequence
                while j < len(seq) - 2:
                    current_codon = seq[j : j + 3]

                    # If we hit a stop codon, we've found an ORF
                    if current_codon in ["TAG", "TAA", "TGA"]:
                        if (
                            len(orf) > 0
                        ):  # Only add if we have codons between start and stop
                            orf_seq = "".join(orf)
                            orfs.append(
                                {
                                    "sequence": orf_seq,
                                    "start_position": start_pos,
                                    "length": len(orf_seq),
                                    "frame": frame + 1,
                                }
                            )
                        break

                    orf.append(current_codon)
                    j += 3

            i += 3

    return f"\n{orfs}" if orfs else "No ORFs found"  # return list of orfs


def transcribe_dna(seq: str) -> str:
    """Converts a given DNA or RNA sequence into mRNA

    Args:
        seq (seq object): DNA or RNA sequence

    Returns:
        str: transcribed biological sequence
    """
    # Process sequence if DNA
    coding_seq = Seq(seq.upper().strip())
    # retrieve the template strand from coding strand (put in the 3' to 5' direction)
    temp_strand = coding_seq.reverse_complement()
    # get mrna from temp strand (put in the 5' to 3' direction)
    mrna = temp_strand.reverse_complement().transcribe()
    return f"Template strand (3' to 5'): {temp_strand}\nTranscribed sequence (5' to 3'): {mrna}"


def back_transcribe_rna(seq: str) -> str:
    """
    Reverse transcribe an RNA sequence to DNA

    Args:
        seq (str): RNA sequence to reverse transcribe to DNA

    Returns:
        str: DNA template obtained from reverse transcription
    """
    seq = Seq(seq.upper().strip())
    return f"{seq.back_transcribe()}"


def translate_rna(seq: str) -> str:
    # obtain mrna
    coding_seq = Seq(seq.upper().strip())
    # translate mrna
    protein = coding_seq.transcribe().translate(table=1)
    return f"{protein}"


# print(calc_gc_content("ATCAGTGTTAGCGAGAATACTCAACAAATCGCATTTTTTACGACAGTCAGACGTATTGAAATTAAAAAGC"))
# print(
#     # calc_gc_content(
#     #     # "atcagtgttagcgagaatactcaacaaatcgcattttttacgacagtcagacgtattgaaattaaaaagc\n"
#     #     "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG\n"
#     # ),
#     transcribe_dna(
#         # "atcagtgttagcgagaatactcaacaaatcgcattttttacgacagtcagacgtattgaaattaaaaagc\n"
#         "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
#     ),
#     translate_rna(
#         # "atcagtgttagcgagaatactcaacaaatcgcattttttacgacagtcagacgtattgaaattaaaaagcnnn"
#         "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
#     ),
#     back_transcribe_rna("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG"),
#     find_orf(
#         # "atcagtgttagcgagaatactcaacaaatcgcattttttacgacagtcagacgtattgaaattaaaaagc\n"
#         "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
#     ),
# )
