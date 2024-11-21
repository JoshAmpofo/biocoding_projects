#!/usr/bin/env python3

import sys
import argparse
from input_validator import seq_validator  # Assuming this exists
from functions import (  # Assuming this exists
    seq_length,
    calc_gc_content,
    transcribe_dna,
    translate_rna,
    find_orf,
    back_transcribe_rna
)

def validate_args(args):
    """
    Validate command line arguments to ensure only one operation is selected
    and the sequence type matches the operation.
    """
    # Count number of operation flags set to True
    operations = sum([
        args.dna,
        args.rna,
        args.transcribe,
        args.back_transcribe,
        args.gc_content,
        args.orf,
        args.length,
        args.protein
    ])
    
    if operations == 0:
        raise ValueError("Please specify at least one operation to perform")
    if operations > 1:
        raise ValueError("Please specify only one operation at a time")
    
    # Validate sequence based on operation
    try:
        if args.sequence:
            seq_validator(args.sequence, 
                        'rna' if (args.rna or args.back_transcribe or args.protein) else 'dna')
    except ValueError as e:
        raise ValueError(f"Invalid sequence: {str(e)}")

def process_sequence(args):
    """
    Process the sequence based on the specified operation.
    Returns tuple of (result, description).
    """
    if args.dna or args.transcribe:
        return (transcribe_dna(args.sequence), "DNA transcribed to RNA")
    elif args.rna or args.protein:
        return (translate_rna(args.sequence), "RNA translated to protein")
    elif args.back_transcribe:
        return (back_transcribe_rna(args.sequence), "RNA back-transcribed to DNA")
    elif args.gc_content:
        return (calc_gc_content(args.sequence), "GC content")
    elif args.orf:
        return (find_orf(args.sequence), "Open reading frames")
    elif args.length:
        return (seq_length(args.sequence), "Sequence length")
    else:
        raise ValueError("No valid operation specified")

def main():
    """
    Main function for the BioSequence Analyzer tool.
    """
    parser = argparse.ArgumentParser(
        prog="BioSequence Analyzer",
        description="A tool for analyzing biological sequences such as DNA and RNA."
    )
    parser.add_argument(
        "sequence",
        type=str,
        help="Input sequence to analyze"
    )
    parser.add_argument(
        "-d", "--dna",
        action="store_true",
        help="Transcribe DNA sequence to RNA"
    )
    parser.add_argument(
        "-r", "--rna",
        action="store_true",
        help="Translate RNA sequence to protein"
    )
    parser.add_argument(
        "-t", "--transcribe",
        action="store_true",
        help="Transcribe DNA sequence to RNA"
    )
    parser.add_argument(
        "-b", "--back-transcribe",
        action="store_true",
        help="Back-transcribe RNA sequence to DNA"
    )
    parser.add_argument(
        "-g", "--gc-content",
        action="store_true",
        help="Calculate GC content of sequence"
    )
    parser.add_argument(
        "-o", "--orf",
        action="store_true",
        help="Find open reading frames (ORFs) in sequence"
    )
    parser.add_argument(
        "-l", "--length",
        action="store_true",
        help="Calculate length of sequence"
    )
    parser.add_argument(
        "-p", "--protein",
        action="store_true",
        help="Translate RNA sequence to protein"
    )

    try:
        args = parser.parse_args()
        validate_args(args)
        result, description = process_sequence(args)
        print(f"{description}: {result}")
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()