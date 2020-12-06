#!/usr/bin/python

with open('AOC6.txt', 'r') as file:
    data = file.read().replace('\n\n', ',')
data = data.replace("\n","")
mylist = data.split(",")

res=[]

for k in mylist:
	k = list(dict.fromkeys(k))
	res.append(len(k))


print(sum(res))