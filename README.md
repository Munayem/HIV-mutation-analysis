# HIV-1 Phylogenetic Analysis

Python tools developed during my **MSc Biotechnology with Data Analytics** dissertation at the **University of Bedfordshire** for preprocessing HIV-1 sequence data and analysing phylogenetic migration patterns of drug-resistant variants.

---

## Dissertation

**Title**

*Phylogenetic Analysis of HIV-1 Subtype B in Asian Countries: Geographic Distribution, Mutation Patterns, and Drug Resistance*

---

## Overview

This repository contains custom Python scripts developed to support the preprocessing and phylogenetic analysis of HIV-1 subtype B protease sequences.

The project focused on:

- Sequence quality control by removing ambiguous nucleotide sequences
- Phylogenetic analysis of HIV-1 subtype B
- Geographic migration inference
- Analysis of drug-resistant variants
- Generation of annotated phylogenetic trees

The scripts were developed as part of my MSc dissertation and support a reproducible workflow for sequence preprocessing and migration analysis.

---

## Repository Structure

```text
hiv1-phylogenetic-analysis
│
├── filter_non_degenerate_new.py
├── migration_tree_analysis.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Scripts

### `filter_non_degenerate_new.py`

Removes nucleotide sequences containing ambiguous (degenerate) IUPAC nucleotide codes from FASTA datasets before downstream phylogenetic analysis.

**Features**

- Reads FASTA files using BioPython
- Detects ambiguous nucleotide symbols
- Removes low-quality sequences
- Generates a cleaned FASTA dataset

**Input**

```text
data/hiv_main_data.fasta
```

**Output**

```text
data/hiv_main_data_non_degenerate.fasta
```

---

### `migration_tree_analysis.py`

Analyses Newick phylogenetic trees to infer geographic migration events among HIV-1 subtype B sequences.

**Features**

- Loads Newick tree files
- Extracts country information from sequence names
- Infers ancestral geographic locations
- Detects migration events between countries
- Produces a colour-coded annotated PDF phylogenetic tree

**Input**

```text
results/example_tree.nwk
```

**Output**

```text
results/example_tree.nwk.migration.pdf
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/hiv1-phylogenetic-analysis.git
cd hiv1-phylogenetic-analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

- Python 3.9+
- BioPython
- ETE Toolkit (ETE3)

---

## Usage

### Filter ambiguous nucleotide sequences

```bash
python filter_non_degenerate_new.py
```

### Analyse migration patterns

```bash
python migration_tree_analysis.py
```

---

## Research Workflow

```text
Los Alamos HIV Sequence Database
              │
              ▼
Sequence Collection
              │
              ▼
Removal of Ambiguous Sequences
(filter_non_degenerate_new.py)
              │
              ▼
Clean Sequence Dataset
              │
              ▼
Drug Resistance Analysis
              │
              ▼
Sequence Alignment
(MEGA X + ClustalW)
              │
              ▼
Phylogenetic Tree Construction
              │
              ▼
Migration Analysis
(migration_tree_analysis.py)
              │
              ▼
Annotated Migration Tree (PDF)
```

---

## Technologies

- Python
- BioPython
- ETE3
- MEGA X
- ClustalW
- FigTree
- iTOL
- SWISS-MODEL

---

## Data Sources

The original research utilised publicly available datasets from:

- Los Alamos HIV Sequence Database
- Stanford HIV Drug Resistance Database

The datasets used in the dissertation are **not included** in this repository.

---

## Research Context

These scripts were developed as part of my MSc Biotechnology with Data Analytics dissertation at the University of Bedfordshire.

The project investigated HIV-1 subtype B drug resistance, phylogenetic relationships, and geographic transmission patterns across Asian countries through computational analysis and bioinformatics.

---

## Future Improvements

Potential future developments include:

- Command-line argument support
- Improved error handling
- Additional visualisation features
- Automated reporting
- Unit tests
- Example datasets for demonstration

---

## Author

**Md Abul Munayem**

MSc Biotechnology with Data Analytics (Distinction)

University of Bedfordshire

### Research Interests

- Bioinformatics
- Computational Biology
- Phylogenetics
- Genomics
- Biotechnology
- Data Analytics
- Machine Learning for Biological Data

---

## License

This project is licensed under the MIT License.
