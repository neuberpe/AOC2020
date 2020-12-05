#!/usr/bin/python
#Problem
#In your expense report, what is the product of the three entries that sum to 2020?

with open('AOC1.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")
mylist = [int(i) for i in mylist]

for i in mylist:
	for j in mylist:
		for k in mylist:
			if i != j:
				if j != i:
					if i + k + j == 2020:
						print(i*j*k)
						print(i)
						print(j)
						print(k)
