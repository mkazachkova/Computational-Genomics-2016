
import time
start_time = time.time()


def oneMismatch(p, mismatches_allowed):
	global t
	global fmB
	#occurrs = fmB.occurrences(p)

	second = p[len(p)/2:]
	first = p[:len(p)/2]

	first_exact_matches = fmB.occurrences(first)
	second_exact_matches = fmB.occurrences(second)

	matches = []

	if second_exact_matches != None:
		for index in second_exact_matches:
			start = index - len(first)
			if (start >= 0):
				#run boyer-more/naive starting at start and matching w/ up to one mismatch for first
				bool_t, list_t = naive(start,first, mismatches_allowed)
				if bool_t:
					matches.append(start) #means there is a match or approximate match here; add to list

	if first_exact_matches != None:
		for index in first_exact_matches:
			start = index + len(first)
			if (start + len(second)) <= (len(t)-1):
				bool_t, list_t = naive(start,second, mismatches_allowed)
				if list_t == 1:
					matches.append(index)
	print matches
	return list(set(matches))

def twoMismatch(p, mismatches_allowed):
	global t
	global fmB

	#p = "helloWorld"

	matches = []

	third = p[len(p)/3 + len(p)/3 :]
	first = p[:len(p)/3]
	second = p[len(p)/3:len(p)/3 + len(p)/3]

	#print "p is"
	#print p
	#print first
	#print second
	#print third

	first_exact_matches = fmB.occurrences(first)
	second_exact_matches = fmB.occurrences(second)
	third_exact_matches = fmB.occurrences(third)

	for each in first_exact_matches:
		if each + len(p) < len(t):
			start_for_second = each + len(first)
			start_for_third = start_for_second + len(second)
			added1, mismatches1 = naive(start_for_second, second, mismatches_allowed)
			added2, mismatches2 = naive(start_for_third, third, mismatches_allowed)
			if added1 and added2:
				if mismatches1 + mismatches2 == 2:
					matches.append(each)

	for index in second_exact_matches:
		if (index - len(first)) >= 0 and (index + len(second) + len(first)) < len(t):
			start_for_first = index - len(first)
			start_for_third = index + len(second)
			added1, mismatches1 = naive(start_for_first, first, mismatches_allowed)
			added2, mismatches2 = naive(start_for_third, third, mismatches_allowed)
			if added1 and added2:
				if mismatches1 + mismatches2 == 2:
					matches.append(start_for_first)

	for index in third_exact_matches:
		if (index - len(second) - len(first)) >= 0 and (index + len(third) < len(t)):
			start_for_first = index - len(second) - len(first)
			start_for_second = index - len(second)
			added1, mismatches1 = naive(start_for_first, first, mismatches_allowed)
			added2, mismatches2 = naive(start_for_second, second, mismatches_allowed)
			if added1 and added2:
				if mismatches1 + mismatches2 == 2:
					matches.append(start_for_first)


	#print matches
	return list(set(matches))

def naive(start, compared, num_mismatch_allowed):
	"""can be changed to boyer more (code available from piazza), but was thinking that since we
	run through so many p's might not be worth it to preprocess? could also do both and see if one is faster?"""
	mismatches = 0
	location = start
	for i in range(len(compared)):
		if t[start] != compared[i]:
			mismatches+=1
		if mismatches > num_mismatch_allowed:  #1
			return False, mismatches
		start+=1
	return True, mismatches


#matches = OneMismatch(p)
#print matches

listT = twoMismatch(p, 2)

print("--- %s seconds ---" % (time.time() - start_time))
#print listT
for each in listT:
	print t[each:each+len(p)]
