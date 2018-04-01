import turtle

grid = []
gridSize = 251-15


def inputChecher(question,datTyp):
	while True:
		try:
			uI = datTyp(input(question))
			break
		except(TypeError):
			print"Oops, that isn't a "+datTyp
	return uI



gridBuilder = []
for x in range(gridSize):
	gridBuilder.append("0")
for x in range(gridSize):
	grid.append(gridBuilder[:])

grid[0][gridSize/2]="1"
#print grid

rules = {}
numChecked = 0
while True:
	numChecked = inputChecher("how many do you want blocks to you want to check(must be odd)",int)
	if((not(numChecked%2==0) and numChecked>1)):
		break
	print"Oops, that isn't a valid number, please input an odd number greater that 1"

for x in range(2**numChecked):
	rule = list(bin((2**numChecked)+x))[3:]
	userIn = ""
	while not(userIn=="0" or userIn =="1"):
		userIn = raw_input(rule)

	rules[str(rule)]=userIn

for x in range(1,gridSize):
	for y in range(numChecked/2,gridSize-numChecked/2):
		#print str(grid[x-1][(y-(numChecked/2)):(y+(numChecked/2))+1])
		grid[x][y]=rules[str(grid[x-1][(y-(numChecked/2)):(y+(numChecked/2))+1])]
for x in grid:
	printer = ""
	for y in x:
		if(y=="1"):
			printer+="#"
		else:
			printer+=" "
	print printer
		



