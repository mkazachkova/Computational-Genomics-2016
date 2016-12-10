import sys
import csv

from fm import FmIndex
from matches import Matches

def parse_fastq(fh):
    # turn fastq into a dictionary of tuples
    fa = {}
    lc = 1
    seqid = ''
    seq = ''
    phred = ''

    for ln in fh:
        if lc == 1:
            seqid = ln[1:].split()[0]
        elif lc == 2:
            seq = ln.strip().upper()
        elif lc == 4:
            phred = ln.strip()
            if len(seq) > 4:
                fa[seqid] = (seq, phred)
            lc = 0
        lc += 1

    return fa

def genome_load(genomeList):
    genomeSequences = {}
    for genomeName in genomeList:
        g = open(genomeName)
        temp = ''
        for line in g.readlines():
            if '>' not in line:
                temp = temp + line.strip()
        g.close()

        genomeSequences[genomeName] = temp
    return genomeSequences

def writeFiles(occurencesIndex):
    for genomeName in occurrencesIndex:
        filename = sys.argv[1]
        f = open(filename[0:filename.find('.')] + '.csv', 'wt')
        bed = open(filename[0:filename.find('.')] + '.bed', 'w')

        writer = csv.writer(f)
        exactrow = []
        oneMissStart = []
        twoMissStart = []
        phreds = []

        for eachRead in reads:
            readlen = len(reads[eachRead][0])
            phred = reads[eachRead[1]]

            for exactLocation in occurrencesIndex[genomeName][eachRead]['0']:
                bed.write(eachRead + '\t' + str(exactLocation) + str(exactLocation + readlen) + '0')
            for oneMissTuple in occurrencesIndex[genomeName][eachRead]['1']:
                bed.write(eachRead + '\t' + str(oneMissTuple[0]) + str(oneMissTuple[1] + readlen) + '1')
                phred.write(str(oneMissTuple[1]))
            for twoMissTuple in occurencesIndex[genomeName][eachRead]['2']:
                bed.write(eachRead + '\t' + str(twoMissTuple[0]) + str(twoMissTuple[0] + readlen) + '2')
                phred.write(str(twoMissTuple[1]))
                phred.write(str(twoMissTuple[2]))

        f.close()
        bed.close()

def main():
    genomeList = []
    reads = {}
    fmB = {}
    matchesByGenome = {}

    occurrencesIndex = {}

    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        reads = parse_fastq(f.readlines())
        f.close()        

        for i in range(2, len(sys.argv)):
            genomeList.append(sys.argv[i])
    else:
        print 'Please include contaminant genomes to scan'
    genomeSequences = genome_load(genomeList)

    #load the fm index
    for genomeName in genomeSequences:
        fmB[genomeName] = FmIndex(genomeSequences[genomeName])
        matchesByGenome[genomeName] = Matches(fmB[genomeName], genomeSequences[genomeName])


    for eachGenome in fmB:
            occurrencesIndex[eachGenome] = {}
            for eachRead in reads:
                exact = matchesByGenome[eachGenome].exactMatch(reads[eachRead][0])
                oneMiss = matchesByGenome[eachGenome].oneMismatch(reads[eachRead][0])
                twoMiss = matchesByGenome[eachGenome].twoMismatch(reads[eachRead][0])
                occurrencesIndex[eachGenome][eachRead] = {'0' : exact, '1': oneMiss, '2' : twoMiss}
                
    writeFiles(occurrencesIndex)

if __name__ == "__main__":
    main()
