#!/usr/bin/env python3

from Bio.Data import IUPACData


# def seq_validator(seq: str) -> bool:
#     """
#     Checks the input sequence and determines whether it is a DNA or RNA seq

#     Args:
#         seq_input (str): input sequence

#     Returns:
#         bool: if DNA or RNA, returns True else returns False
#     """
#     dna_letters = IUPACData.unambiguous_dna_letters
#     rna_letters = IUPACData.unambiguous_rna_letters

#     # check if seq contains valid dna or rna letters
#     if set(seq) <= set(dna_letters):
#         return True, "DNA"
#     elif set(seq) <= set(rna_letters):
#         return True, "RNA"
#     else:
#         return False, "Invalid sequence"
    

from typing import Tuple, Literal

SequenceType = Literal["dna", "rna", "any"]

def seq_validator(seq: str, seq_type: SequenceType = "any") -> Tuple[bool, str]:
    """
    Validates biological sequences (DNA or RNA) against IUPAC standards.
    
    Args:
        seq (str): Input sequence to validate
        seq_type (str): Expected sequence type ("dna", "rna", or "any")
        
    Returns:
        Tuple[bool, str]: (is_valid, message)
            - is_valid: True if sequence is valid, False otherwise
            - message: "DNA", "RNA", or error message
            
    Raises:
        ValueError: If seq_type is invalid or sequence doesn't match expected type
    """
    if not seq:
        raise ValueError("Empty sequence provided")
    
    # Convert sequence to uppercase for comparison
    seq = seq.upper()
    
    # Get valid letters for DNA and RNA
    dna_letters = set(IUPACData.unambiguous_dna_letters)
    rna_letters = set(IUPACData.unambiguous_rna_letters)
    
    # Check sequence composition
    seq_set = set(seq)
    is_dna = seq_set <= dna_letters
    is_rna = seq_set <= rna_letters
    
    # Validate based on expected sequence type
    if seq_type.lower() == "dna":
        if not is_dna:
            raise ValueError("Invalid DNA sequence - contains non-DNA characters")
        return True, "DNA"
    
    elif seq_type.lower() == "rna":
        if not is_rna:
            raise ValueError("Invalid RNA sequence - contains non-RNA characters")
        return True, "RNA"
    
    elif seq_type.lower() == "any":
        if is_dna:
            return True, "DNA"
        elif is_rna:
            return True, "RNA"
        else:
            invalid_chars = seq_set - (dna_letters | rna_letters)
            raise ValueError(f"Invalid sequence - contains invalid characters: {', '.join(sorted(invalid_chars))}")
    
    else:
        raise ValueError(f"Invalid sequence type specified: {seq_type}. Must be 'dna', 'rna', or 'any'")


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