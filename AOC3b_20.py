#!/usr/bin/python

with open('AOC3.txt', 'r') as file:
    data = file.read().replace('\n', '')

metric = [[1,1],[3,1],[5,1],[7,1],[1,2]]
w = 31
res= []

for k in metric:
	i=z=count=0
	while i <= 10013:
		if data[i] == "#":
			count += 1
		if z < (w-k[0]):
			i += (w*k[1]+k[0])
			z += k[0]
		else:
			i += (w*k[1]-w+k[0])
			z -= (w-k[0])
	res.append(count)

print(res[0]*res[1]*res[2]*res[3]*res[4])