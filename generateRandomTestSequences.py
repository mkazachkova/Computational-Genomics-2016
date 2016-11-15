import os

for file in os.listdir("/home/mjoo3/cs439/contaminants/"):
    for contaminant in os.listdir("/home/mjoo3/cs439/contaminants/" + file + "/"):
        genome = open("/home/mjoo3/cs439/contaminants/" + file + "/" + contaminant)

        sequences = genome.readlines()
        lc = 1
        index = 0
        lengths = [10, 20, 30]
        for line in sequences:
            if '>' not in line and not (lc % 100):
                seq = line.strip().upper()
                if 'N' not in seq:
                    print '>' + contaminant + ':' + str(lc)
                    print seq[:lengths[index % 3]] 
                    index += 1
                    

            lc += 1

        
        genome.close()

