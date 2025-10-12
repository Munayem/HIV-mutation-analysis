# HIV Mutation and Migration Analysis

This repository contains the workflow and Python scripts used to analyze HIV sequence data, remove degenerate bases, construct phylogenetic trees, and identify migration patterns between countries.

---

## Repository Contents

| Folder / File | Description |
|----------------|-------------|
| scripts/ | Python scripts for sequence filtering and tree analysis |
| data/ | FASTA data files (or external Google Drive links) |
| results/ | Output trees and analysis results |

---

## Workflow Summary

1. Data collected from:
   - Los Alamos HIV Sequence Database  
     https://www.hiv.lanl.gov/components/sequence/HIV/search/search.html
   - Stanford HIV Drug Resistance Database  
     https://hivdb.stanford.edu/

2. Process steps:
   - Collected FASTA sequences from Los Alamos
   - Removed degenerate bases using Biopython
   - Extracted mutation data from Stanford HIVDB
   - Created phylogenetic trees using MEGA X
   - Visualized migration events using ETE3

---

## Requirements

Install Python dependencies before running the scripts:

```bash
pip install biopython ete3
```

Python version: 3.9 or higher

---

## Usage

### 1. Filter Non-Degenerate Sequences

Run the filtering script to remove sequences containing degenerate bases.

```bash
python scripts/filter_non_degenerate_new.py
```

### 2. Generate and Color Migration Trees

Run the tree analysis script to visualize migration events between countries.

```bash
python scripts/migration_tree_analysis.py
```

---

## External Data Links

The main data and results are stored in Google Drive and can be accessed here:  
https://drive.google.com/drive/folders/170Q1fEDGgGoOOmOzmvtFLIULFdvQywxY?usp=sharing

---

## Author

**Md Abul Munayem**  
