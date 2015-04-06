# coding: utf-8
seq1 = "THHHHTTTTHHHHTHHHHHHHHTTTHHTTHHHHHTTTTTTHHTHHTHHHTTTHTTHHHHTHTTTHTTTHHTTTTHHHHHHTTTHHTTHHHTHHHHHTTTTTHTTTHHTTHTTHHTTTHHTTTHHTHHTHHTTTTTHHTHHHHHHTHTHTTHTHTTHHHTTHHTHTHHHHHHHHTTHTTHHHTHHTTHTTTTTTHHHTHHH"
seq1 = list(seq1)
seq2 = "THTHTTTHTTTTTHTHTTTHTTHHHTHHTHTHTHTTTTHHTTHHTTHHHTHHHTTHHHTTTHHHTHHHHTTTHTHTHHHHTHTTTHHHTHHTHTTTHHTHHHTHHHHTTHTHHTHHHTTTHTHHHTHHTTTHHHTTTTHHHTHTHHHHTHTTHHTTTTHTHTHTTHTHHTTHTTTHTTTTHHHHTHTHHHTTHHHHHTHH"
seq2 = list(seq2)
def getlen(seq, char):
    res = 0
    for i in range(len(seq)):
        if seq[i] == char:
            res += 1
    return res
print "Sequence #1", "H:", getlen(seq1, "H"), "T:", getlen(seq1, "T")
print "Sequence #2", "H:", getlen(seq2, "H"), "T:", getlen(seq2, "T")
def getmaxlen(seq, char):
    if char == "T":
        split = "H"
    if char == "H":
        split = "T"
    temp = "".join([seq[i] for i in range(len(seq))])
    y = [len(item) for item in temp.split(split)]
    return max(y)
print "Sequence #1: ", "H sequence", getmaxlen(seq1, "H"), ",", "T sequence", getmaxlen(seq1, "T")
print "Sequence #2: ", "H sequence", getmaxlen(seq2, "H"), ",", "T sequence", getmaxlen(seq2, "T")
import random
def throwCoin():
    return random.choice(["H", "T"])
nTrails = 1000
size = 200
ncon = []
for i in range(nTrails):
    seq = [throwCoin() for i in range(size)]
    ncon.append(max(getmaxlen(seq, "H"), getmaxlen(seq, "T")))
print "Mean of maximum length of consecutive heads/tails:",     float(sum(ncon)) / len(ncon)
print "Probability that maximum length of consecutive heads/tails is larger than 5:",     float(sum([item >5 for item in ncon]))/ len(ncon)
