#!/usr/bin/python

with open('AOC3.txt', 'r') as file:
    data = file.read().replace('\n', '')

count = i = z = 0

while i <= 10013:
	if data[i] == "#":
		count = count + 1
	if z <28:
		i = i + 34
		z = z + 3
	else:
		i = i + 3
		z = z - 28

print(count)