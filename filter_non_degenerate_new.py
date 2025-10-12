from Bio import SeqIO
import os

# Input and output paths
input_fasta = r"data/hiv_main_data.fasta"
output_fasta = r"data/hiv_main_data_non_degenerate.fasta"

# Define degenerate bases (IUPAC codes)
degenerate_bases = set("RYSWKMBDHVN")

# List to store clean sequences
clean_records = []

print("Filtering non-degenerate sequences...")

# Parse the FASTA and filter
for record in SeqIO.parse(input_fasta, "fasta"):
    seq = str(record.seq).upper()
    if not any(base in degenerate_bases for base in seq):
        clean_records.append(record)

# Save filtered sequences
SeqIO.write(clean_records, output_fasta, "fasta")

print("Filtering complete!")
print(f"Total non-degenerate sequences: {len(clean_records)}")
print(f"Saved to: {output_fasta}")
