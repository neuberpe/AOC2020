#!/usr/bi3n/python

with open('AOC3.txt', 'r') as file:
    data = file.read().replace('\n', '')

count1 = 0
i1 = 0
z1 = 0

count3 = 0
i3 = 0
z3 = 0

count5 = 0
i5 = 0
z5 = 0

count7 = 0
i7 = 0
z7 = 0

count02 = 0
i02 = 0
z02 = 0

while i1 <= 10013:
	if data[i1] == "#":
		count1 = count1 + 1
		if z1 <30:
			i1 = i1 + 32
			z1 = z1 + 1
		elif z1 == 30:
			i1 = i1 + 1
			z1 = 0
	else:
		if z1 <30:
			i1 = i1 + 32
			z1 = z1 + 1
		elif z1 == 30:
			i1 = i1 + 1
			z1 = 0

while i3 <= 10013:
	if data[i3] == "#":
		count3 = count3 + 1
		if z3 <28:
			i3 = i3 + 34
			z3 = z3 + 3
		elif z3 == 28:
			i3 = i3 + 3
			z3 = 0
		elif z3 == 29:
			i3 = i3 + 3
			z3 = 1
		elif z3 == 30:
			i3 = i3 + 3
			z3 = 2
	else:
		if z3 <28:
			i3 = i3 + 34
			z3 = z3 + 3
		elif z3 == 28:
			i3 = i3 + 3
			z3 = 0
		elif z3 == 29:
			i3 = i3 + 3
			z3 = 1
		elif z3 == 30:
			i3 = i3 + 3
			z3 = 2

while i5 <= 10013:
	if data[i5] == "#":
		count5 = count5 + 1
		if z5 <26:
			i5 = i5 + 36
			z5 = z5 + 5
		elif z5 == 26:
			i5 = i5 + 5
			z5 = 0
		elif z5 == 27:
			i5 = i5 + 5
			z5 = 1
		elif z5 == 28:
			i5 = i5 + 5
			z5 = 2
		elif z5 == 29:
			i5 = i5 + 5
			z5 = 3
		elif z5 == 30:
			i5 = i5 + 5
			z5 = 4

	else:
		if z5 <26:
			i5 = i5 + 36
			z5 = z5 + 5
		elif z5 == 26:
			i5 = i5 + 5
			z5 = 0
		elif z5 == 27:
			i5 = i5 + 5
			z5 = 1
		elif z5 == 28:
			i5 = i5 + 5
			z5 = 2
		elif z5 == 29:
			i5 = i5 + 5
			z5 = 3
		elif z5 == 30:
			i5 = i5 + 5
			z5 = 4

while i7 <= 10013:
	if data[i7] == "#":
		count7 = count7 + 1
		if z7 <24:
			i7 = i7 + 38
			z7 = z7 + 7
		elif z7 == 24:
			i7 = i7 + 7
			z7 = 0
		elif z7 == 25:
			i7 = i7 + 7
			z7 = 1
		elif z7 == 26:
			i7 = i7 + 7
			z7 = 2
		elif z7 == 27:
			i7 = i7 + 7
			z7 = 3
		elif z7 == 28:
			i7 = i7 + 7
			z7 = 4
		elif z7 == 29:
			i7 = i7 + 7
			z7 = 5
		elif z7 == 30:
			i7 = i7 + 7
			z7 = 6

	else:
		if z7 <24:
			i7 = i7 + 38
			z7 = z7 + 7
		elif z7 == 24:
			i7 = i7 + 7
			z7 = 0
		elif z7 == 25:
			i7 = i7 + 7
			z7 = 1
		elif z7 == 26:
			i7 = i7 + 7
			z7 = 2
		elif z7 == 27:
			i7 = i7 + 7
			z7 = 3
		elif z7 == 28:
			i7 = i7 + 7
			z7 = 4
		elif z7 == 29:
			i7 = i7 + 7
			z7 = 5
		elif z7 == 30:
			i7 = i7 + 7
			z7 = 6

while i02 <= 10013:
	if data[i02] == "#":
		count02 = count02 + 1
		if z02 <30:
			i02 = i02 + 63
			z02 = z02 + 1
		elif z02 == 30:
			i02 = i02 + 32
			z02 = 0
	else:
		if z02 <30:
			i02 = i02 + 63
			z02 = z02 + 1
		elif z02 == 30:
			i02 = i02 + 32
			z02 = 0

print(count1)
print(count3)
print(count5)
print(count7)
print(count02)
print(count1*count3*count5*count7*count02)