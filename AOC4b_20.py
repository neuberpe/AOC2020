#!/usr/bin/python

with open('AOC4.txt', 'r') as file:
    data = file.read().replace('\n\n', ',')
    data = data.replace("\n"," ")
mylist = data.split(",")
valid =["byr","iyr","eyr","hgt","hcl","ecl","pid"]

solution = []
solution2 =[]

for k in mylist:
	count = 0	
	for v in valid:
		x = k.find(v)
		if x >= 0:
			count += 1
	if count == 7:
		solution.append(k)

print(len(solution))

for j in solution:
	y = j.split()
	check = 0
	for l in y:
		if l[:3] == valid[0]:
			if int(l[4:])>1919 and int(l[4:])<2003:
				check += 1
		if l[:3] == valid[1]:
			if int(l[4:])>2009 and int(l[4:])<2021:
				check += 1
		if l[:3] == valid[2]:
			if int(l[4:])>2019 and int(l[4:])<2031:
				check += 1
		if l[:3] == valid[3]:
			if l[-2:] == "cm":
				if int(l[4:-2])>145 and int(l[4:-2])<194:
					check += 1
			if l[-2:] == "in":
				if int(l[4:-2])>58 and int(l[4:-2])<77:
					check += 1
		if l[:3] == valid[4]:
			if l[4] == "#" and len(l[5:]) == 6:
				check += 1
		if l[:3] == valid[5]:
			if l[4:] == "amb" or l[4:] == "blu" or l[4:] == "brn" or l[4:] == "gry" or l[4:] == "grn" or l[4:] == "hzl" or l[4:] == "oth":
				check += 1
		if l[:3] == valid[6]:
			if len(l[4:]) == 9:
				check += 1
	if check == 7:
		solution2.append(y)

print(len(solution2))