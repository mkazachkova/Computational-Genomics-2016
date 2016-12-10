readID = []
start = []
end = []
mismatches = []
phreds = []
phredplot = []
for i in range(0, 50):
	phredplot.append(0)


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

	for score in phreds:
		phredplot[score] += 1

	print phredplot


def compare_phred():
	print 'h'

def main():
	f = open('RealReads3.bed')
	fh = f.readlines()
	read_bed(fh)
	f.close()

	g = open('RealReads3.txt')
	gh = g.readlines()
	read_phred(gh)
	g.close()

main()
