#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
from Bio.Seq import Seq

# decoration
print(stylize("\n---- | Translate mRNA into corresponding protein seq. | ----\n", fg("red")))

# user interaction
messenger_rna = Seq(input("Enter mRNA strand: ").upper())

# function
def translate(mRNA):
    print("\nTranslating mRNA strand...")
    print("Translation done.")
    return mRNA.translate()

# output
protein_sequence = stylize(translate(messenger_rna), fg("red"))
print(f"\nmRNA strand: {messenger_rna}\nCorresponding protein sequence: {protein_sequence}\n")
