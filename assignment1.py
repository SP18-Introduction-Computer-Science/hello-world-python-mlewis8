print("Hello World ")


a  = []
c = [ 'A', 'B' ]

a.append(1)
a.append(c)
a.append(2)
a.append(3)

b = a[1]


#print(b)

#print(a)

# This a now contains [ 1, 2, 3 ]


for loopVar in a[1] :
	print(loopVar)


for index,loopVar in enumerate(a[1]) :
	print(str(index) + " : " + loopVar)



