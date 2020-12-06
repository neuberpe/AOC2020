#!/usr/bin/python

with open("AOC6.txt", "r") as file:
    data = file.read().replace("\n\n", ",")
mylist = data.split(",")
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
res = 0

for k in mylist:
	s =""
	k = k.split("\n")
	s = list(s.join(k))
	for j in abc:
		if s.count(j) == len(k):
			res += 1

print(res)
