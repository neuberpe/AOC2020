#!/usr/bin/python

#Problem
#Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
#(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
#Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

with open('AOC2.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",") #umändern des obigen strings in liste, gesplittet nach ","
count = 0	#initiern

for k in mylist: 	#für jedes element in der liste wird das element in k genutzt
	sep1 = k.find("-") 	#pos seperator -
	sep2 = k.find(":") 	#pos seperator :
	p1 = int(k[:sep1])	#Zahl/Position 1
	st = k[sep2+1:]		#Stringanteil zu prüfen
	p2 = int(k[sep1+1:sep2-2])	#Zahl/Position 2
	var = k[sep2-1]		#Suchbegriff
	if st[p1] == var:	#Wenn Suchbegriff gleich Buchstabe an p1 aus string
		if st[p2] != var:	#Wenn dann noch ungleich an p2
			count = count + 1
	else:
		if st[p2] == var:	#Wenn ungleich an p1 und gleich an p2
			count = count + 1

print(str(count))