#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TEST CASES
def test_orf_finder():
    test_seq = "ATGCCCTAAATGCCCTAGTGA"
    results = find_orf(test_seq)
    
    if results:
        print(f"Found {len(results)} ORFs:")
        for i, orf in enumerate(results, 1):
            print(f"\nORF {i}:")
            print(f"Sequence: {orf['sequence']}")
            print(f"Start position: {orf['start_position']}")
            print(f"Length: {orf['length']} nucleotides")
            print(f"Reading frame: {orf['frame']}")
    else:
        print("No ORFs found")  # return list of orfs