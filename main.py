import sys

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
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        reads = parse_fastq(f.readlines())
        f.close()        

        for i in range(2, len(sys.argv)):
            genomeList.append(sys.argv[i])
    else:
        print 'Please choose a contaminant'

    genomeSequences = genome_load(genomeList)

    print 'reads:' + str(len(reads))
    for genome in genomeSequences:
        print genome + ':' + str(len(genomeSequences[genome]))

if __name__ == "__main__":
    main()