import sys
from FmCheckpoints import FmCheckpoints

def suffixArray(s):
    ''' Given T return suffix array SA(T).  Uses "sorted"
        function for simplicity, which is probably very slow. '''
    satups = sorted([(s[i:], i) for i in xrange(0, len(s))])
    return map(lambda x: x[1], satups) # extract, return just offsets

def bwtFromSa(t, sa=None):
    ''' Given T, returns BWT(T) by way of the suffix array. '''
    bw = []
    dollarRow = None
    if sa is None:
        sa = suffixArray(t)
    for si in sa:
        if si == 0:
            dollarRow = len(bw)
            bw.append('$')
        else:
            bw.append(t[si-1])

    return (''.join(bw), dollarRow) # return string-ized version of list bw


class FmIndex():
    @staticmethod
    def downsampleSuffixArray(sa, n=4):
        ''' Take only the suffix-array entries for every nth suffix.  Keep
            suffixes at offsets 0, n, 2n, etc with respect to the text.
            Return map from the rows to their suffix-array values. '''
        ssa = {}
        for i in xrange(0, len(sa)):
            # We could use i % n instead of sa[i] % n, but we lose the
            # constant-time guarantee for resolutions
            if sa[i] % n == 0:
                ssa[i] = sa[i]
        return ssa

    def __init__(self, t, cpIval=4, ssaIval=4):
        if t[-1] != '$':
            t += '$' # add dollar if not there already
        # Get BWT string and offset of $ within it
        sa = suffixArray(t)
        self.bwt, self.dollarRow = bwtFromSa(t, sa)

        # Get downsampled suffix array, taking every 1 out of 'ssaIval'
        # elements w/r/t T
        self.ssa = self.downsampleSuffixArray(sa, ssaIval)
        self.slen = len(self.bwt)
        # Make rank checkpoints
        self.cps = FmCheckpoints(self.bwt, cpIval)
        # Calculate # occurrences of each character
        tots = dict()
        for c in self.bwt:
            tots[c] = tots.get(c, 0) + 1
        # Calculate concise representation of first column
        self.first = {}
        totc = 0
        for c, count in sorted(tots.iteritems()):
            self.first[c] = totc
            totc += count

    def count(self, c):
        ''' Return number of occurrences of characters < c '''
        if c not in self.first:
            # (Unusual) case where c does not occur in text
            for cc in sorted(self.first.iterkeys()):
                if c < cc: return self.first[cc]
            return self.first[cc]
        else:
            return self.first[c]

    def range(self, p):
        ''' Return range of BWM rows having p as a prefix '''
        l, r = 0, self.slen - 1 # closed (inclusive) interval
        for i in xrange(len(p)-1, -1, -1): # from right to left
            l = self.cps.rank(self.bwt, p[i], l-1) + self.count(p[i])
            r = self.cps.rank(self.bwt, p[i], r)   + self.count(p[i]) - 1
            if r < l:
                break
        return l, r+1

    def resolve(self, row):
        ''' Given BWM row, return its offset w/r/t T '''
        def stepLeft(row):
            ''' Step left according to character in given BWT row '''
            c = self.bwt[row]
            return self.cps.rank(self.bwt, c, row-1) + self.count(c)
        nsteps = 0
        while row not in self.ssa:
            row = stepLeft(row)
            nsteps += 1
        return self.ssa[row] + nsteps

    def occurrences(self, p):
        ''' Return offsets for all occurrences of p, in no particular order '''
        l, r = self.range(p)
        return [ self.resolve(x) for x in xrange(l, r) ]

    def occurrencesReverse(self, p, tLen):
        ''' Return offsets for all occurrences of p, in no particular order '''
        l, r = self.range(p)
        revMatches = [ self.resolve(x) for x in xrange(l, r) ]
        count = 0
        for i in revMatches:
            i = tLen - 1 - i
            revMatches[count] = i
            count += 1
        return revMatches

def test(text):
    p, t = "ba", text
    #              01234567890123456789012345678901234567890123456789012
    # Occurrences:        *         *  *           *         *  *
    fm = FmIndex(t)
    matches = sorted(fm.occurrences(p))
    #matches == [7, 17, 20, 32, 42, 45]
    return matches

def testRev(text, tLen):  #reverse the input strings (for forward-facing T)
    p, t = "ba", text
    #              01234567890123456789012345678901234567890123456789012
    # Occurrences:        *         *  *           *         *  *
    fm = FmIndex(t)
    revMatches = sorted(fm.occurrencesReverse(p, tLen))
    return revMatches

def revertIndexes(list_of_indexes, strlen, lenP):
    """
    To be used on the return of occurences mathod
    """
    new_list = []
    for each in list_of_indexes:
        new_list.append(((each + (lenP-1)) - (strlen -1)) * -1)
    return new_list

def main():
    f = open("genometest.txt", "r")
    t = f.read()
    tRev = "".join(reversed(t))
    tLen = len(t)
    print "T =", t

    fmB = FmIndex(t)
    fmF = FmIndex(tRev)

    print "Suffix Array =", fmB.ssa
    print "BWT =", fmB.bwt, "  dollarRow = ", fmB.dollarRow
    print "Checkpoints =", fmB.cps.cps
    print "Concise first column", fmB.first

    print "Range 'a' =", fmB.range('a')
    print "Range 'baaba' =", fmB.range('baaba')

    print "Offsets of matches in test2() =", test(t)

    print " "

    print "Suffix Array =", fmF.ssa
    print "BWT =", fmF.bwt, "  dollarRow = ", fmF.dollarRow
    print "Checkpoints =", fmF.cps.cps
    print "Concise first column", fmF.first

    print "Range 'a' =", fmF.range('a')
    print "Range 'baaba' =", fmF.range('baaba')

    print "Offsets of matches in test2() =", testRev(tRev, tLen)

    #Test revertIndexes
    print "printing occurrences for next tests"
    print fmB.occurrences("a")
    reversed_occurrences = fmF.occurrences("a")
    print reversed_occurrences
    returned_list = revertIndexes(reversed_occurrences, len(t), len("a"))
    for each in returned_list:
        print each

    print fmB.occurrences("ac")
    print fmF.occurrences("ca") #must reverse string to use forward facing? Is this correct???
    print revertIndexes(fmF.occurrences("ca"), len(t), len("ca"))

    

if __name__ == "__main__":
    main()
