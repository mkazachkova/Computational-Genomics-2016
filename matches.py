
#import time
#start_time = time.time()

#global t
#global self.self.fmB

class Matches():

	def __init__(self, fmB, t):
		self.fmB = fmB
		self.t = t 


	def naive(self, start, compared, num_mismatch_allowed):
		"""can be changed to boyer more (code available from piazza), but was thinking that since we
		run through so many p's might not be worth it to preprocess? could also do both and see if one is faster?"""
		mismatches = 0
		location = start
		mismatchInd = []
		for i in range(len(compared)):
			if start < len(self.t):
				if self.t[start] != compared[i]:
					mismatches+=1
					mismatchInd.append(i)
				if mismatches > num_mismatch_allowed:  #1
					del mismatchInd[len(mismatchInd)]
					return False, mismatches
				start+=1
		return True, mismatchInd


	def exactMatch(self, p):

		#occurrs = self.self.fmB.occurrences(p)

		second = p[len(p)/2:]
		first = p[:len(p)/2]

		first_exact_matches = self.fmB.occurrences(first)
		second_exact_matches = self.fmB.occurrences(second)

		matches = []

		if second_exact_matches != None:
			for index in second_exact_matches:
				start = index - len(first)
				if (start >= 0):
					#run boyer-more/self.naive starting at start and matching w/ up to one mismatch for first
					bool_t, list_t = self.naive(start,first, 0)
					if len(list_t) == 1:
						misMatchpair = (start,list_t[0]+len(first))
						matches.append(misMatchpair) #means there is a match or approximate match here; add to list

		if first_exact_matches != None:
			for index in first_exact_matches:
				start = index + len(first)
				if (start + len(second)) <= (len(self.t)-1):
					bool_t, list_t = self.naive(start,second, 0)
					if len(list_t) == 1:
						misMatchpair = (index,list_t[0])
						matches.append(misMatchpair)
		return list(set(matches))

	def oneMismatch(self, p):

		#occurrs = self.self.fmB.occurrences(p)

		second = p[len(p)/2:]
		first = p[:len(p)/2]

		first_exact_matches = self.fmB.occurrences(first)
		second_exact_matches = self.fmB.occurrences(second)

		matches = []

		if second_exact_matches != None:
			for index in second_exact_matches:
				start = index - len(first)
				if (start >= 0):
					#run boyer-more/self.naive starting at start and matching w/ up to one mismatch for first
					bool_t, list_t = self.naive(start,first, 1)
					if len(list_t) == 1:
						misMatchpair = (start,list_t[0]+len(first))
						matches.append(misMatchpair) #means there is a match or approximate match here; add to list

		if first_exact_matches != None:
			for index in first_exact_matches:
				start = index + len(first)
				if (start + len(second)) <= (len(self.t)-1):
					bool_t, list_t = self.naive(start,second, 1)
					if len(list_t) == 1:
						misMatchpair = (index,list_t[0])
						matches.append(misMatchpair)
		return list(set(matches))

	def twoMismatch(self,p):
		matches = []

		third = p[len(p)/3 + len(p)/3 :]
		first = p[:len(p)/3]
		second = p[len(p)/3:len(p)/3 + len(p)/3]

		first_exact_matches = self.fmB.occurrences(first)
		second_exact_matches = self.fmB.occurrences(second)
		third_exact_matches = self.fmB.occurrences(third)

		for each in first_exact_matches:
			if each + len(p) < len(self.t):
				start_for_second = each + len(first)
				start_for_third = start_for_second + len(second)
				added1, mismatches1 = self.naive(start_for_second, second, 2)
				added2, mismatches2 = self.naive(start_for_third, third, 2)
				#misMatchpair = ()
				mismatchesP = []
				if added1 and added2:
					if len(mismatches1) + len(mismatches2) == 2:
						for i in range(0, len(mismatches1)):
							mismatchesP.append(mismatches1[i] + len(first))
						for j in range(0, len(mismatches2)):
							mismatchesP.append(mismatches2[j] + len(first) + len(second))
						#misMatchpair = (each, mismatchesP[0], mismatchesP[1])
						#for k in range(0, len(mismatchesP)):
						#	misMatchpair[k] = mismatchesP[k]
						matches.append((each, mismatchesP[0], mismatchesP[1]))

		for index in second_exact_matches:
			if (index - len(first)) >= 0 and (index + len(second) + len(first)) < len(self.t):
				start_for_first = index - len(first)
				start_for_third = index + len(second)
				added1, mismatches1 = self.naive(start_for_first, first, 2)
				added2, mismatches2 = self.naive(start_for_third, third, 2)
				#misMatchpair = ()
				mismatchesP = []
				if added1 and added2:
					if len(mismatches1) + len(mismatches2) == 2:
						for i in range(0, len(mismatches1)):
							mismatchesP.append(mismatches1[i])
						for j in range(0, len(mismatches2)):
							mismatchesP.append(mismatches2[j] + len(first) + len(second))
						
						#for k in range(0, len(mismatchesP)):
						#	misMatchpair[k] = mismatchesP[k]
						matches.append((start_for_first, mismatchesP[0], mismatchesP[1]))

		for index in third_exact_matches:
			if (index - len(second) - len(first)) >= 0 and (index + len(third) < len(self.t)):
				start_for_first = index - len(second) - len(first)
				start_for_second = index - len(second)
				added1, mismatches1 = self.naive(start_for_first, first, 2)
				added2, mismatches2 = self.naive(start_for_second, second, 2)
				#misMatchpair = ()
				mismatchesP = []
				if added1 and added2:
					if len(mismatches1) + len(mismatches2) == 2:
						for i in range(0, len(mismatches1)):
							mismatchesP.append(mismatches1[i])
						for j in range(0, len(mismatches2)):
							mismatchesP.append(mismatches2[j] + len(first))
						#for k in range(0, len(mismatchesP)):
						#	misMatchpair[k] = mismatchesP[k]
						matches.append((start_for_first, mismatchesP[0], mismatchesP[1]))
		#print matches
		return list(set(matches))

#matches = OneMismatch(p)
#print matches

#listT = twoMismatch(p, 2)

#print("--- %s seconds ---" % (time.time() - start_time))
#print listT
#for each in listT:
#	print t[each:each+len(p)]
