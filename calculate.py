import pandas as pd

try:
	theta = pd.read_csv("theta.csv")
	print(theta)
	x = input("Put some kilometers: ")
	theta0 = theta[theta.columns.values[0]]
	theta1 = theta[theta.columns.values[1]]
	print(theta0.values[0])
	print(theta1.values[0])
	y = theta0.values[0] + theta1.values[0] * x
	# print("Estimated price is "  + str(y))
except:
	print("Could not open \"theta.csv\"")