#!/usr/bin/python

with open("AOC7.txt", "r") as file:
    data = file.read().replace("\n", ";")
mylist = data.split(";")
logic = []
key = []
res = []

for k in mylist:
	k = k.split(" ")
	temp = []
	if k[4] != "no":
		i = 4
		while i < len(k):
			temp.append(k[i])
			temp.append(k[i+1]+" "+k[i+2])
			i += 4
		logic.append(temp)
		key.append(k[0]+" "+k[1])

i=0
gold = logic[key.index("shiny gold")]
while i <len(gold):
	res.append(gold[i])
	i +=1
#print(gold)

up = len(res)
lo = 0
print(res)

while up != lo:
	for k in res[lo:up]:
		if not k.isnumeric():
			for m in key:
				if k in m:
					i=0
					sol = logic[key.index(m)]
					while i < len(sol):
						if sol[i].isnumeric():
							n = int(sol[i])*int(res[res.index(k)-1])
							res.append(str(n))
						else:
							res.append(sol[i])
						i += 1
	lo=up
	up=len(res)
	print(res[lo:up])

i=0
check=0
while i < len(res):
	check +=int(res[i])
	i +=2

print(check)
print(res)

#print(key)
#print(logic)
