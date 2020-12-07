#!/usr/bin/python

with open("AOC7.txt", "r") as file:
    data = file.read().replace("\n", ";")
mylist = data.split(";")
logic = []
key = []
res = []
c = 0

for k in mylist:
	k = k.split(" ")
	temp = []
	if k[4] != "no":
		i = 4
		while i < len(k):
			temp.append(k[i+1]+" "+k[i+2])
			i += 4
		logic.append(temp)
		key.append(k[0]+" "+k[1])

for k in logic:
	if "shiny gold" in k:
		res.append(key[c])
	c += 1

for k in res:
	f = 0
	for m in logic:
		if k in m:
			res.append(key[f])
		f += 1

print(len(list(set(res))))