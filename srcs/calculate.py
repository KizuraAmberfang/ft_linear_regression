from numpy import isin
import pandas as pd

end = False
try:
	theta = pd.read_csv("data/theta.csv")
	theta0 = theta[theta.columns.values[0]]
	theta1 = theta[theta.columns.values[1]]
	if (not(isinstance(theta0.values[0], float)) or not(isinstance(theta1.values[0], float))):
		print("\033[93mWarning: file \"theta.csv\" corrupted, setting thetas to 0.\033[0m")
		dataSet = {
  			'theta0': [0],
  			'theta1': [0]
			}
		theta = pd.DataFrame(dataSet)
except:
	print("\033[93mWarning: could not open \"theta.csv\", setting thetas to 0.\033[0m")
	dataSet = {
  		'theta0': [0],
  		'theta1': [0]
		}
	theta = pd.DataFrame(dataSet)

theta0 = theta[theta.columns.values[0]]
theta1 = theta[theta.columns.values[1]]
while (end == False):
	try: 
		x = float(input("Enter a value: "))
		if (x < 0):
			print("\033[93mWarning: You have to give a positive number!\033[0m")
		else:
			y = theta0.values[0] + theta1.values[0] * x
			end = True
			print("Estimated price is " + str(y))
	except:
		print("\033[93mWarning: You have to enter a number!\033[0m")