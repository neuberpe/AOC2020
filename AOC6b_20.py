#!/usr/bin/python

with open('AOC6.txt', 'r') as file:
    data = file.read().replace('\n\n', ',')
mylist = data.split(",")
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
res = 0

test =["abc","a\nb\nc","ab\nac","a\na\na\na","b"]

for k in test:
	s =""
	k = k.split("\n")
	a = len(k)
	s = list(s.join(k))
	#s = list(s)
	for j in abc:
		if s.count(j) == a:
			res += 1

print(res)