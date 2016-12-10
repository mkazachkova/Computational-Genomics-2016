readID = []
start = []
end = []
mismatches = []
phreds = []



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

	print phreds


def compare_phred():

def main():
	f = open('RealReads3.bed')
	fh = f.readlines()
	read_bed(fh)
	f.close()

	g = open('RealReads3.txt')
	gh = g.readlines()
	read_phred(gh)
	g.close()
