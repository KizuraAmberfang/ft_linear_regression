import pandas as pd
import matplotlib.pyplot as plt
import os

class train:
	def __init__(self, file: str, steps: int, lr: float) -> None:
		self.__errArr = []
		self.__file = file
		try:
			self.__steps = int(steps)
			if self.__steps < 1:
				raise Exception
		except:
			print("\033[31mFatal: steps is not an integer > 0.\033[0m")
			exit()
		try:
			self.__lr = float(lr)
			if self.__lr <= 0:
				raise Exception
		except:
			print("\033[31mFatal: learning rate is not a positive number.\033[0m")
			exit()
		try:
			self.__dataFile = pd.read_csv(self.__file)
			if (self.__validate(self.__dataFile)):
				self.__mins = self.__dataFile.min()
				self.__maxs = self.__dataFile.max()
				if self.__mins[0] == self.__maxs[0] or self.__mins[1] == self.__maxs[1]:
					print("\033[31mFatal: \"{}\" is invalid!\033[0m".format(self.__file))
				else:
					self.__normData = self.__normalize(self.__dataFile, self.__mins, self.__maxs)
					self.__average = self.__normData.mean()[1]
			else:
				print("\033[31mFatal: \"{}\" is corrupted!\033[0m".format(self.__file))
		except:
			print("\033[31mFatal: \"{}\" not found, we can not train the alghorithm!\033[0m".format(self.__file))

	def run(self):
		self.__theta = self.__train()
		self.__theta = self.__denorm(self.__theta)
		self.__writeTheta(self.__theta)

	def print(self):
		try:
			os.mkdir("export")
		except:
			pass
		try:
			ax = plt.figure()
			ax = plt.subplot()
			ax.set_xlabel(self.__dataFile.columns.values[0])
			ax.set_ylabel(self.__dataFile.columns.values[1])
			ax.set_title("data value and linear regression")
			ax.plot(self.__dataFile[self.__dataFile.columns.values[0]], self.__dataFile[self.__dataFile.columns.values[1]], "r*")
			ax.plot([self.__mins[0], self.__maxs[0]], [self.__calculate(self.__theta, self.__mins[0]), self.__calculate(self.__theta, self.__maxs[0])])
			plt.savefig("export/regression")
			print("\033[92mSaved: \"regression.png\"\033[0m")
		except: 
			print("\033[93mWarning: Could not save \"regression.png\".\033[0m")
		try:
			bx = plt.figure()
			bx = plt.subplot()
			bx.set_title("relative error")
			bx.set_xlabel("iteration")
			bx.set_ylabel("relative error")
			bx.plot(self.__errData["iter"], self.__errData["err"])
			plt.savefig("export/relative_error")
			print("\033[92mSaved: \"relative_error.png\"\033[0m")
		except:
			print("\033[93mWarning: Could not save \"relative_error.png\".\033[0m")

	def __normalize(self, data, mins, maxs):
		ret = []
		for row in data.values:
			ret.append([
				(row[0] - mins[0]) / (maxs[0] - mins[0]), 
				(row[1] - mins[1]) / (maxs[1] - mins[1])
				])
		return pd.DataFrame(ret, columns=[data.columns.values[0], data.columns.values[1]])

	def __calculate(self, theta, x):
		return theta[0] + x * theta[1]

	def __sumError(self, data, theta):
		sum = 0
		for row in data.values:
			sum += self.__calculate(theta, row[0]) - row[1]
		return sum

	def __sumWeightError(self, data, theta):
		sum = 0
		for row in data.values:
			sum += (self.__calculate(theta, row[0]) - row[1]) * row[0]
		return sum

	def __calcErr(self, a, b, data, nRow, avg):
		err = 0
		for row in data.values:
			err += abs(row[1] - a - (b * row[0]))
		return (err / nRow) / avg

	def __train(self):
		theta = [0, 0]
		nRow = self.__normData.count()[0]
		prev = 1
		for i in range(self.__steps):
			tempTheta0 = theta[0] - (self.__lr * (1/nRow) * self.__sumError(self.__normData, theta))
			tempTheta1 = theta[1] - (self.__lr * (1/nRow) * self.__sumWeightError(self.__normData, theta))
			theta = [tempTheta0, tempTheta1]
			temp = self.__calcErr(tempTheta0, tempTheta1, self.__normData, nRow, self.__average)
			self.__errArr.append([
				i,
				temp
			])
			if prev > temp:
				prev = temp
			else:
				print("Alghorithm stops after {} iteration. Relative error is {:.2f}.".format(i, temp))
				break
		if i == 9999:
			print("Relative error is {:.2f}.".format(prev))
		self.__errData = pd.DataFrame(self.__errArr, columns=["iter", "err"])
		return theta

	def __denorm(self, theta):
		rangeX = self.__maxs[0] - self.__mins[0]
		rangeY = self.__maxs[1] - self.__mins[1]
		tempTheta1 = theta[1] * (rangeY / rangeX)
		tempTheta0 = theta[0] * rangeY - theta[1] * (rangeY / rangeX) * self.__mins[0] + self.__mins[1]
		return [tempTheta0, tempTheta1]

	def __writeTheta(self, theta):
		try:
			with open("data/theta.csv", "w") as file:
				file.write("theta0,theta1\n")
				file.write(str(theta[0]) + "," + str(theta[1]) + "\n")
				print("\033[92mSaved: \"theta.csv\"\033[0m")
		except:
			print("\033[31mFatal: could not create \"theta.csv\".\033[0m")

	def __validate(self, data):
		try: 
			for row in data.values:
				float(row[0])
				float(row[1])
			return True
		except:
			return False
