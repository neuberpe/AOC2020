#!/usr/bin/python
#Problem:
#Find the two entries that sum to 2020; what do you get if you multiply them together?

with open('AOC1.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")
mylist = [int(i) for i in mylist]

for i in mylist:
	for k in mylist:
		if k != i:
			if i + k == 2020:
				print(i*k)
				print(i)
				print(k)
