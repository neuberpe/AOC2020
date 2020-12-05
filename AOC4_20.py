#!/usr/bin/python

with open('AOC4.txt', 'r') as file:
    data = file.read().replace('\n\n', ',')
    data = data.replace("\n"," ")
mylist = data.split(",")
valid =["byr","iyr","eyr","hgt","hcl","ecl","pid"]

sol = 0
count = 0
x=0

for k in mylist:
	count = 0	
	for v in valid:
		x = k.find(v)
		if x >= 0:
			count += 1
	if count == 7:
		sol = sol +1

print(sol)