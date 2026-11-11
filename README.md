# Foundations-of-Computer-Science-Final-Project

This project will analyze partial coding sequences of the ribulose-1,5-bisphosphate carboxylase/oxygenase large subunit (rbcL) gene of various plant species in the mint family. It uses DNA sequences from the NCBI GenBank to compute and display biological statistics including number of base pairs, nucleotide composition (visualized with matplotlib pie chart), GC content percentage, codon signal analysis, DNA barcode visualization, and similarity percentages between the plants' sequences. The Python program will generate an HTML webpage with forms where a user can choose the plant to analyze and the plant to compare it to. Additionally, there is an index page describing the project and relevant biological concepts.

------------------------------------------------------------------------------------------------------------------------------

# Plant DNA Analysis Tool

A Python-based computational biology project that analyzes and compares partial coding sequences of the *rbcL* gene across nine plant species in the mint family (Lamiaceae).

## Project Overview

The Plant DNA Analysis Tool uses DNA sequences sourced from NCBI GenBank to examine nucleotide composition and genetic similarities among selected members of the Lamiaceae family.

The program calculates molecular statistics, generates visual representations of DNA sequences, and dynamically creates an HTML webpage where users can select two plants for individual analysis and comparison.

This project combines introductory molecular biology concepts with Python programming, data analysis, and web development.

## Biological Background

### The *rbcL* Gene

The *rbcL* gene encodes the large subunit of RuBisCO (ribulose-1,5-bisphosphate carboxylase/oxygenase), an enzyme essential to photosynthetic carbon fixation.

RuBisCO catalyzes the incorporation of carbon dioxide into ribulose-1,5-bisphosphate (RuBP) during the Calvin cycle, contributing to carbohydrate synthesis.

The *rbcL* gene is also widely used in plant DNA barcoding and molecular identification because it is present across a broad range of plant lineages.

### DNA and Nucleotide Composition

DNA stores genetic information through sequences of four nucleotide bases:

- Adenine (A)
- Thymine (T)
- Cytosine (C)
- Guanine (G)

The project examines nucleotide composition and GC content, the percentage of guanine and cytosine bases within a DNA sequence.

It also examines codons, sequences of three nucleotides that encode amino acids or signal the beginning or termination of protein translation.

## Plant Species

The tool includes nine species from the Lamiaceae (mint) family:

| Common Name | Scientific Name |
|---|---|
| Spearmint | *Mentha spicata* |
| Lavender | *Lavandula angustifolia* |
| Rosemary | *Salvia rosmarinus* |
| Sage | *Salvia officinalis* |
| Lemon Balm | *Melissa officinalis* |
| Basil | *Ocimum basilicum* |
| Catnip | *Nepeta cataria* |
| Oregano | *Origanum vulgare* |
| Bergamot (Bee Balm) | *Monarda didyma* |

## Features and Functionality

### 1. DNA Sequence Statistics

- **Sequence length:** Calculates the total number of nucleotide positions in each sequence.
- **Nucleotide composition:** Counts the occurrences of adenine, thymine, cytosine, and guanine.
- **GC content:** Calculates the percentage of guanine and cytosine bases relative to total sequence length.

### 2. Codon Signal Analysis

- Counts occurrences of the ATG start codon.
- Counts occurrences of the three standard stop codons: TAA, TAG, and TGA.
- Scans the sequence in consecutive groups of three nucleotides, beginning at the first position.

### 3. DNA Visualization

- **Nucleotide composition charts:** Uses Matplotlib to generate pie charts displaying the relative frequencies of A, T, C, and G.
- **DNA barcodes:** Generates colored visual representations of nucleotide sequences, with a distinct color assigned to each of the four bases.

### 4. Sequence Comparison

Calculates the percentage of matching nucleotide positions between two selected sequences.

Users can select any two of the nine plant species through HTML dropdown forms and view their respective statistics alongside the calculated similarity percentage.

### 5. Interactive Web Interface

The Python program dynamically generates HTML webpages displaying:

- Plant names and scientific classifications.
- DNA sequence statistics.
- Codon analysis results.
- Nucleotide composition charts.
- DNA barcode visualizations.
- Pairwise sequence similarity.

An accompanying homepage introduces the project, DNA structure, key genetic concepts, and the biological significance of the *rbcL* gene.

## Technologies Used

| Technology | Application |
|---|---|
| Python | DNA sequence processing, calculations, and HTML generation |
| Matplotlib | Nucleotide composition pie charts |
| HTML | Webpage structure and interactive selection forms |
| CSS | Website styling and layout |
| NCBI GenBank | Source of DNA sequence data |

## Data Source

DNA sequences were obtained from **NCBI GenBank**, the National Center for Biotechnology Information's public nucleotide sequence database.

The project uses partial coding sequences of the *rbcL* gene rather than complete plant genomes.

Individual accession numbers and complete sequence provenance were not systematically documented during the original educational project.

## Limitations and Considerations

This project was developed as an educational programming application to explore the intersection of molecular biology and computer science. Its calculations are intended for introductory analysis and demonstration rather than formal genetic identification or evolutionary research.

Several methodological limitations should be considered:

- **Partial sequences:** Analyses are restricted to the available portions of the *rbcL* gene.
- **Sequence similarity:** Similarity is calculated by comparing nucleotide positions directly up to the length of the shorter sequence. The program does not perform sequence alignment or account for insertions and deletions.
- **Codon analysis:** Codon signals are counted in a single reading frame beginning at the first nucleotide. The program does not establish the actual translated reading frame or identify biologically validated coding boundaries.
- **Ambiguous nucleotides:** The bergamot (*Monarda didyma*) sequence contains an unidentified nucleotide represented by N. This nucleotide is retained in the sequence and included in the total sequence length, affecting GC content calculations.
- **Sequence provenance:** Individual GenBank accession numbers were not systematically recorded, limiting exact reproducibility of the original dataset.

## Project Purpose

This project was developed as a computer science final project to apply programming concepts to a biological dataset. It explores how computational tools can be used to examine genetic information, visualize nucleotide sequences, and investigate molecular similarities among related plant species.
