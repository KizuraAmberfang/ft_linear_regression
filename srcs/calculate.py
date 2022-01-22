import pandas as pd

class linReg: 
	def __init__(self) -> None:
		self.__getThetas()
		pass

	def __getThetas(self):
		try:
			__theta = pd.read_csv("data/theta.csv")
			self.__theta0 = __theta[__theta.columns.values[0]]
			self.__theta1 = __theta[__theta.columns.values[1]]
			if (not(isinstance(self.__theta0.values[0], float)) or not(isinstance(self.__theta1.values[0], float))):
				print("\033[93mWarning: file \"theta.csv\" corrupted, setting thetas to 0.\033[0m")
				dataSet = {
					'theta0': [0],
					'theta1': [0]
					}
				__theta = pd.DataFrame(dataSet)
		except:
			print("\033[93mWarning: could not open \"theta.csv\", setting thetas to 0.\033[0m")
			dataSet = {
				'theta0': [0],
				'theta1': [0]
				}
			__theta = pd.DataFrame(dataSet)
		self.__theta0 = __theta[__theta.columns.values[0]]
		self.__theta1 = __theta[__theta.columns.values[1]]

	def calc(self):
		end = False
		while (end == False):
			try: 
				x = float(input("Enter a value: "))
				y = self.__theta0.values[0] + self.__theta1.values[0] * x
				end = True
				return x, y
			except:
				print("\033[93mWarning: You have to enter a number!\033[0m")