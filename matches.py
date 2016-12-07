import sys
from fm import FmIndex

t = ""
fmB = None

def OneMismatch(p):
	#p = "helloWorld"
	global t
	global fmB
	occurrs = fmB.occurrences(p)

	second = p[len(p)/2:]
	first = p[:len(p)/2]
	#print first
	#print second

	first_exact_matches = fmB.occurrences(first)
	second_exact_matches = fmB.occurrences(second)

	matches = []

	if second_exact_matches != None:
		for index in second_exact_matches:
			start = index - len(first)
			if (start >= 0):
				#run boyer-more/naive starting at start and matching w/ up to one mismatch for first 
				if naive(start, first):
					matches.append(start) #means there is a match or approximate match here; add to list

	if first_exact_matches != None:
		for index in first_exact_matches:
			start = index + len(first) 
			if (start +len(second)) <= (len(t)-1):
				if naive(start,second):
					matches.append(index)
	return list(set(matches))


def naive(start, compared): 
	"""can be changed to boyer more (code available from piazza), but was thinking that since we 
	run through so many p's might not be worth it to preprocess? could also do both and see if one is faster?"""
	mismatches = 0
	location = start
	for i in range(len(compared)):
		if t[start] != compared[i]:
			mismatches+=1
		if mismatches > 1:
			return False
		start+=1
	return True

f = open("test_genome.txt", "r")
t = f.read()
fmB = FmIndex(t)

#will be replaced with kevin's parsing later; just for testing purposes now
a = open("test_pattern_exact.txt", "r")
p = a.read()

matches = OneMismatch(p)
print matches 
