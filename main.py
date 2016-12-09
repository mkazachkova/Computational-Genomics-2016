import sys
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
            fa[seqid] = ('', '')
        elif lc == 2:
            seq = ln.strip().upper()
        elif lc == 4:
            phred = ln.strip()
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

def main():
    genomeList = []
    reads = {}
    fmB = {}
    matchesByGenome = {}

    occurencesIndex = {}

    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        reads = parse_fastq(f.readlines())
        f.close()        

        for i in range(2, len(sys.argv)):
            genomeList.append(sys.argv[i])
    else:
        print 'Please choose a contaminant'

    genomeSequences = genome_load(genomeList)
    print 'before loading fm index'
    #load the fm index
    for genomeName in genomeSequences:
        fmB[genomeName] = FmIndex(genomeSequences[genomeName])
        matchesByGenome[genomeName] = Matches(fmB[genomeName], genomeSequences[genomeName])
    print 'before eachGenome in fmB'
    for eachGenome in fmB:
            occurencesIndex[eachGenome] = {}
            for eachRead in reads:
                exact = matchesByGenome[eachGenome].exactMatch(reads[eachRead])
                oneMiss = matchesByGenome[eachGenome].oneMismatch(reads[eachRead])
                twoMiss = matchesByGenome[eachGenome].twoMismatch(reads[eachRead])
                occurencesIndex[eachGenome][eachRead] = {0 : exact, 1 : oneMiss, 2 : twoMiss}
                print str(len(occurencesIndex[eachGenome][eachRead][0]))
                print str(len(occurencesIndex[eachGenome][eachRead][1]))
                print str(len(occurencesIndex[eachGenome][eachRead][2]))

                print '----------'
    #now occurencesIndex contains a list of all occurrences of a read, in each contaminant genome




if __name__ == "__main__":
    main()
