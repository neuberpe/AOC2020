#!/usr/bin/python

with open("AOC8.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",")

instruction = []
value = []
acc = 0

for k in mylist:
	k = k.split(" ")
	instruction.append(k[0])
	value.append(k[1])

step=[]
i=1

while not i in step:
	step.append(i)
	if instruction[i-1] == "nop":
		i +=1
	elif instruction[i-1] == "acc":
		acc += int(value[i-1])
		i +=1
	else: 
		i += int(value[i-1])

print(acc)