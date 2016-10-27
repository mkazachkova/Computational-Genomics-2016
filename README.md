# Project Proposal - Computational Genomics 
## Team members: 
Kiki Chang, Jeana Yee, Mariya Kazachkova, Kevin Jza Joo 

## Research Goals:

### Method we want to develop:
We are looking to create a method to detect contamination in data sets of sequencing reads. The method would preprocess the datasets of sequencing reads as well as the dataset of contaminants to maximize time and space efficiency, using data structures such as the Bloom Filter Tree [1]. 

### How to evaluate method:
We believe that the easiest way to evaluate our method is to start by running our algorithm with data sets of sequencing reads that are known to contain certain contaminants and making sure that we are getting the correct results (so the correct contaminants are being identified). Once this is working without any errors, we can move on to looking at data sets where the status of contamination is unknown.  

### Input data needed: 
For our input data we need a data set of sequencing reads (or, preferably, multiple data sets of sequencing reads). We could find these data sets online, and these data sets would likely have a description of what contaminants are present in them (this would allow us to check if our algorithm is working properly, as stated in the "how to evaluate method" section). However, ultimately we think that it would be interesting to get data sets of sequencing reads from a lab here at Hopkins and run our algorithm with that data (as this is a recent idea we had we are unsure of how feasible it would be).  

### Milestones we want to accomplish: 
Here are three milestones we plan on accomplishing during the duration of this project: 

1. Creating our own database/list of common contaminants. We will search through our data sets of sequencing reads to look for the presense of any of the contaminants in our database, thus this set of contaminants needs to be comprehensive (we will need to do research in order to compile this database).

2. Milestone 2

3. Milestone 3

### Stretch Goals:


## References to Papers: 
[1] Brad Solomon and Carleton Kingsford. Large-scale search of transcriptomic read sets with sequence bloom trees. *bioRxiv*, page 017087, 2015.





