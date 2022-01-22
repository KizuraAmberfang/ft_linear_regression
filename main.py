from srcs.calculate import linReg

linReg = linReg()

loop = True
while loop:
	x, y = linReg.calc()
	if (x < 0):
		print("You have to give a positive number!")
	else:
		if y < 0:
			y = 0
		print("Estimated price for {} km is ${:.2f}".format(x, y))
		loop = False