#!/usr/bin/python

with open("AOC6.txt", "r") as file:
    data = file.read().replace("\n\n", ",")
data = data.replace("\n","")
mylist = data.split(",")

res=[]

for k in mylist:
	res.append(len(list(dict.fromkeys(k))))

print(sum(res))
