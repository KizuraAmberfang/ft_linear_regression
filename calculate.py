import pandas as pd

end = False
try:
	theta = pd.read_csv("theta.csv")
except:
	print("Could not open \"theta.csv\", setting thetas to 0.")
	dataSet = {
  		'theta0': [0],
  		'theta1': [0]
		}
	theta = pd.DataFrame(dataSet)
try:
	theta0 = theta[theta.columns.values[0]]
	theta1 = theta[theta.columns.values[1]]
except:
	print
while (end == False):
	try: 
		x = float(input("Enter a value: "))
		if (x < 0):
			print("You have to give a positive number!")
		else:
			y = theta0.values[0] + theta1.values[0] * x
			end = True
			print("Estimated price is " + str(y))
	except:
		print("You have to enter a number!")