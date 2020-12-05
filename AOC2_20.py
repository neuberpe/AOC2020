#!/usr/bin/python

#Problem
#Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
#For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.How many passwords are valid according to their policies?

with open('AOC2.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",") #umändern des obigen strings in liste, gesplittet nach ","
count = 0	#initiern

for k in mylist:	#für jedes element des strings, mache aus k das aktuelle element
	sep1 = k.find("-") #pos -
	sep2 = k.find(":") #pos :
	if k[sep2+2:].count(k[sep2-1]) >= int(k[:sep1]):	#string nach separator2.suchen wert vor separator2 größer gleich min. anzahl (zahl1)
			if k[sep2+2:].count(k[sep2-1]) <= int(k[sep1+1:sep2-2]): 	#wie oben aber kleiner gleich max. anzahl (zahl2)
				count = count + 1 	#wenn alles zutrifft, zählen

print(str(count))