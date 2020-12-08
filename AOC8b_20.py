#!/usr/bin/python

with open("AOC8.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",")

instruction = []
value = []

for k in mylist:
	k = k.split(" ")
	instruction.append(k[0])
	value.append(k[1])

f=0
for k in instruction:
	mod = instruction.copy()
	if k == "jmp":
		mod[f] = "nop"
		step=[]
		i=1
		acc = 0
		while not i in step:
			try:
				step.append(i)
				if mod[i-1] == "nop":
					i +=1
				elif mod[i-1] == "acc":
					acc += int(value[i-1])
					i +=1
				else: 
					i += int(value[i-1])
			except:
				print(str(acc) + ":"+str(f))
				break

	f += 1