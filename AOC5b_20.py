#!/usr/bin/python

with open('AOC5.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")

row =[]
column = []
FID = []
testlist = []

for k in mylist:
	ru = 127
	rl = 0
	i = 0
	while i < 7:
		if k[i] == "F":
			ru = ((rl + ru - 1) // 2)
		if k[i] == "B":
			rl = ((rl + ru + 1) // 2)
		if ru == rl:
			row.append(ru)
		i += 1

for k in mylist:
	ru = 7
	rl = 0
	i = 7
	while i < 10:
		if k[i] == "L":
			ru = ((rl + ru - 1) // 2)
		if k[i] == "R":
			rl = ((rl + ru + 1) // 2)
		if ru == rl:
			column.append(ru)
		i += 1

r = 0
while r < len(row):
	FID.append(row[r] * 8 + column[r])
	r += 1

r = min(FID)
while r < max(FID)+1:
	testlist.append(r)
	r += 1

r = 0
while r < max(FID) - min(FID):
	testlist.remove(FID[r])
	r += 1

print(max(FID))
print(testlist)