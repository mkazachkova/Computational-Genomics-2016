# Project Proposal - Computational Genomics 
## Team members: 
Kiki Chang, Jeana Yee, Mariya Kazachkova, Min Geol Joo 

## Research Goals:

### Method we want to develop:
We are looking to create a method to detect contamination in data sets of sequencing reads. The method would preprocess the datasets of sequencing reads as well as the dataset of contaminants to maximize time and space efficiency, using data structures such as the Bloom Filter Tree [1]. We will be using either Python or C to implement our algorithm.  

### How to evaluate method:
We believe that the easiest way to evaluate our method is to start by running our algorithm with data sets of sequencing reads that are known to contain certain contaminants and making sure that we are getting the correct results (so the correct contaminants are being identified). Once this is working without any errors, we can move on to looking at data sets where the status of contamination is unknown.  

### Input data needed: 
For our input data we need a data set of RNA-seq reads (or, preferably, multiple data sets of sequencing reads from multiple experiments). We could find these data sets online, and see if reads map to genomes of contaminants, and then put the mapped reads into BLAST [4]. This would allow us to check if our algorithm is working properly, as stated in the "how to evaluate method" section. Thus it follows we would also need to pull genomes of contaminants from online, most likely from NCBI. Ultimately, we think that it would be interesting to get data sets of sequencing reads from a lab here at Hopkins and run our algorithm with that data (as this is a recent idea we had we are unsure of how feasible it would be).  

### Milestones we want to accomplish: 
Here are three milestones we plan on accomplishing during the duration of this project: 

1. Creating our own database/file of common contaminants. We will search parse through a large number of diverse RNA-seq experiment runs to look for parts of genomes of contaminant species, and see if these genome substrings are repeated. That way we can measure the relative frequency of contaminant sequences, per contaminant genome. We will choose the contaminant genomes ourselves based on already done research (ex: Mycoplasma genomes would be included, because they are accepted as a common contaminant) [2].

2. Creating a working algorithm (not necessarily the most efficient) that is successfully able to detect the presence of any of the contaminants from our database of contaminants within the data set of sequence reads being tested [3].

3. Optimize the algorithm from milestone 2 to use less space and/or have a lower time complexity.

### Stretch Goals:

1. Implement code to automatically pull multiple data sets of sequence reads off of a selected website (this would prevent us from having to manually download the data sets and run the algorithm on them)

2. Gather data sets of sequence reads from multiple Hopkins labs and run our algroithm on them to discover if any/which contaminants are present. We could then compile some sort of chart or other visual representation of which contaminants are most common in Hopkins labs and/or which contaminants are most common in each lab.

3. Have the algorithm "check" itself so that rather than a binary answer of whether the contaminant is present or not, it could be more of a weighted probability function based on phred scores, hamming/edit distance, as well as clustering contaminant genome parts that appear frequently into "bins" that represent a genome interval from which many contaminant sequences come from.

## References to Papers: 
[1] Brad Solomon and Carleton Kingsford. Large-scale search of transcriptomic read sets with sequence bloom trees. *bioRxiv*, page 017087, 2015.

[2] William B Langdon. Mycoplasma contamination in the 1000 genomes project. BioData Min- ing, 7(1):1, 2014.  

[3] Schmieder, Robert, and Robert Edwards. “Fast Identification and Removal of Sequence Contamination from Genomic and Metagenomic Datasets.” Ed. Francisco Rodriguez-Valera. PLoS ONE 6.3 (2011): e17288. PMC. Web. 27 Oct. 2016.

[4] Anthony O Olarerin-George and John B Hogenesch. Assessing the prevalence of mycoplasma contamination in cell culture via a survey of ncbi’s rna-seq archive. Nucleic acids research, 43(5):2535–2542, 2015. 


