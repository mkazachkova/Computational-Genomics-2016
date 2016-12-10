import csv
from sets import Set 

readID = []
start = []
end = []
mismatches = []
phreds = []


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

def read_bed(fh):
	for line in fh:
		temp = line.split()
		readID.append(temp[0])
		start.append(temp[1])
		end.append(temp[2])
		mismatches.append(temp[3])

def read_phred(fh):
	for line in fh:
		phreds.append(ord(line.strip()) - 33)
	phreds.sort()

	phredplot = []
	for i in range(0, 50):
		phredplot.append(0)

	for score in phreds:
		phredplot[score] += 1

	return phredplot


def average_phred():
	f = open('RealReads3.fq')
	reads = parse_fastq(f.readlines())
	f.close()
	averagephreds = []

	for read in reads:
		tempPhred = reads[read][1]
		avgphred = 0
		for i in range(0, len(tempPhred)):
			avgphred += (ord(tempPhred[i]) - 33)

		averagephreds.append(avgphred / len(tempPhred))
	averagephreds.sort()
    
        avgphredplot = []
        for i in range(0, 50):
            avgphredplot.append(0)

        for score in averagephreds:
            avgphredplot[score] += 1

        return avgphredplot

def get_unique_hits():
	print 'Unique Hits: ' + len(set(readID))

def main():
	csvfile = open('RealReads3.csv', 'wt')
	writer = csv.writer(csvfile)

	f = open('RealReads3.bed')
	fh = f.readlines()
	read_bed(fh)
	f.close()

	g = open('RealReads3.txt')
	gh = g.readlines()
	phredplot = read_phred(gh)
	g.close()

	averagephredplot = average_phred()

	writer.writerow(phredplot)
	writer.writerow(averagephredplot)
	csvfile.close()

	get_unique_hits()


main()
