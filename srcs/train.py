import pandas as pd
import matplotlib.pyplot as plt
import os

def normalize(data, mins, maxs):
    ret = []
    for row in data.values:
        ret.append([
            (row[0] - mins[0]) / (maxs[0] - mins[0]), 
            (row[1] - mins[1]) / (maxs[1] - mins[1])
            ])
    return pd.DataFrame(ret, columns=[data.columns.values[0], data.columns.values[1]])

def calculate(theta, x):
    return theta[0] + x * theta[1]

def sumError(data, theta):
    sum = 0
    for row in data.values:
        sum += calculate(theta, row[0]) - row[1]
    return sum

def sumWeightError(data, theta):
    sum = 0
    for row in data.values:
        sum += (calculate(theta, row[0]) - row[1]) * row[0]
    return sum

def calcErr(a, b, data, nRow, avg):
	err = 0
	for row in data.values:
		err += abs(row[1] - a - (b * row[0]))
	return (err / nRow) / avg

def train(data, avg):
	theta = [0, 0]
	lr = 1/100
	nRow = data.count()[0]
	prev = 1
	for i in range(10000):
		tempTheta0 = theta[0] - (lr * (1/nRow) * sumError(data, theta))
		tempTheta1 = theta[1] - (lr * (1/nRow) * sumWeightError(data, theta))
		theta = [tempTheta0, tempTheta1]
		temp = calcErr(tempTheta0, tempTheta1, data, nRow, avg)
		errArr.append([
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
	global errData
	errData = pd.DataFrame(errArr, columns=["iter", "err"])
	return theta

def denorm(theta):
    rangeX = maxs[0] - mins[0]
    rangeY = maxs[1] - mins[1]
    tempTheta1 = theta[1] * (rangeY / rangeX)
    tempTheta0 = theta[0] * rangeY - theta[1] * (rangeY / rangeX) * mins[0] + mins[1]
    return [tempTheta0, tempTheta1]

def writeTheta(theta):
	try:
		with open("data/theta.csv", "w") as file:
			file.write("theta0,theta1\n")
			file.write(str(theta[0]) + "," + str(theta[1]) + "\n")
			print("\033[92mSaved: \"theta.csv\"\033[0m")
	except:
		print("\033[31mFatal: could not create \"theta.csv\".\033[0m")

def validate(data):
	try: 
		for row in data.values:
			float(row[0])
			float(row[1])
		return True
	except:
		return False

errArr = []
try:
	dataFile = pd.read_csv("data/data.csv")
	if (validate(dataFile)):
		mins = dataFile.min()
		maxs = dataFile.max()
		normData = normalize(dataFile, mins, maxs)
		average = normData.mean()[1]
		theta = train(normData, average)
		theta = denorm(theta)
		writeTheta(theta)
		try:
			os.mkdir("export")
		except:
			pass
		try:
			ax = plt.figure()
			ax = plt.subplot()
			ax.set_xlabel(dataFile.columns.values[0])
			ax.set_ylabel(dataFile.columns.values[1])
			ax.set_title("data value and linear regression")
			ax.plot(dataFile[dataFile.columns.values[0]], dataFile[dataFile.columns.values[1]], "r*")
			ax.plot([mins[0], maxs[0]], [calculate(theta, mins[0]), calculate(theta, maxs[0])])
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
			bx.plot(errData["iter"], errData["err"])
			plt.savefig("export/relative_error")
			print("\033[92mSaved: \"relative_error.png\"\033[0m")
		except:
			print("\033[93mWarning: Could not save \"relative_error.png\".\033[0m")
	else:
		print("\033[31mFatal: \"data.csv\" is corrupted!\033[0m")
except:
	print("\033[31mFatal: \"data.csv\" not found, we can not train the alghorithm!\033[0m")