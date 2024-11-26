#!/usr/bin/env python3

from Bio.Data import IUPACData
from typing import Tuple, Literal

SequenceType = Literal["dna", "rna", "protein"]


def seq_validator(seq: str, seq_type: SequenceType = "any") -> Tuple[bool, str]:
    """
    Validates biological sequences (DNA or RNA) against IUPAC standards.

    Args:
        seq (str): Input sequence to validate
        seq_type (str): Expected sequence type ("dna", "rna", or "protein")

    Returns:
        Tuple[bool, str]: (is_valid, message)
            - is_valid: True if sequence is valid, False otherwise
            - message: "DNA", "RNA", "Protein", or error message

    Raises:
        ValueError: If seq_type is invalid or sequence doesn't match expected type
    """
    # check if no sequence is provided
    if not seq:
        raise ValueError("Empty sequence provided")

    # Convert sequence to uppercase for comparison
    seq = seq.upper()

    # Get valid letters for DNA and RNA
    dna_letters = set(IUPACData.unambiguous_dna_letters)
    rna_letters = set(IUPACData.unambiguous_rna_letters)
    protein_letters = set("ACDEFGHIKLMNPQRSTVWY*UOXZ")

    # Check sequence composition
    seq_set = set(seq)
    is_dna = seq_set <= dna_letters
    is_rna = seq_set <= rna_letters
    is_protein = seq_set <= protein_letters

    # Validate based on expected sequence type
    if seq_type.lower() == "dna":
        if not is_dna:
            raise ValueError("Invalid DNA sequence - contains non-DNA characters")
        return True, "DNA"

    elif seq_type.lower() == "rna":
        if not is_rna:
            raise ValueError("Invalid RNA sequence - contains non-RNA characters")
        return True, "RNA"

    elif seq_type.lower() == "protein":
        if not is_protein:
            raise ValueError(
                "Invalid protein sequence - contains non-protein characters"
            )
        return True, "PROTEIN"

    elif seq_type.lower() == "any":
        if is_dna:
            return True, "DNA"
        elif is_rna:
            return True, "RNA"
        elif is_protein:
            return True, "PROTEIN"
        else:
            invalid_chars = seq_set - (dna_letters | rna_letters | protein_letters)
            raise ValueError(
                f"Invalid sequence - contains invalid characters: {', '.join(sorted(invalid_chars))}"
            )

    else:
        raise ValueError(
            f"Invalid sequence type specified: {seq_type}. Must be 'dna', 'rna', or 'protein'"
        )


def is_dna(seq: str) -> bool:
    """
    Helper function to check if a sequence is valid DNA.

    Args:
        seq (str): Sequence to check

    Returns:
        bool: True if valid DNA sequence, False otherwise
    """
    try:
        valid, seq_type = seq_validator(seq, "dna")
        return valid
    except ValueError:
        return False


def is_rna(seq: str) -> bool:
    """
    Helper function to check if a sequence is valid RNA.

    Args:
        seq (str): Sequence to check

    Returns:
        bool: True if valid RNA sequence, False otherwise
    """
    try:
        valid, seq_type = seq_validator(seq, "rna")
        return valid
    except ValueError:
        return False


def is_protein(seq: str) -> bool:
    """
    Helper function to check if a sequence is valid protein.

    Args:
        seq (str): Sequence to check

    Returns:
        bool: True if valid protein sequence, False otherwise
    """
    try:
        valid, seq_type = seq_validator(seq, "protein")
        return valid
    except ValueError:
        return False


# Example usage and testing
# if __name__ == "__main__":
#     test_sequences = [
#         ("ATGC", "any"),
#         ("AUGC", "any"),
#         ("ATGX", "any"),
#         ("ATGC", "dna"),
#         ("AUGC", "rna"),
#         ("ATGC", "rna"),
#         ("", "any"),
#     ]

#     for seq, seq_type in test_sequences:
#         try:
#             result = seq_validator(seq, seq_type)
#             print(f"Sequence: {seq}, Type: {seq_type}, Result: {result}")
#         except ValueError as e:
#             print(f"Sequence: {seq}, Type: {seq_type}, Error: {str(e)}")
