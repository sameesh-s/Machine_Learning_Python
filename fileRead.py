with open("dataset.txt") as textFile:
	lines = [line.split(',') for line in textFile]
	print lines[0][0]

length=lines.__len__()
print "Length of training set :"+ str(length)



for i in range(len(lines)):
    lines[i][3]=lines[i][3].strip('\n')
print lines[0][0]

print lines
