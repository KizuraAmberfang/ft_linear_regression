from cmath import inf
import pandas as pd
import matplotlib.pyplot as plt

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
		err += abs(row[0] - a - b * row[0])
	return (err / nRow) / avg

def train(data, avg):
	theta = [0, 0]
	lr = 1/100
	nRow = data.count()[0]
	for i in range(100):
		tempTheta0 = theta[0] - (lr * (1/nRow) * sumError(data, theta))
		tempTheta1 = theta[1] - (lr * (1/nRow) * sumWeightError(data, theta))
		theta = [tempTheta0, tempTheta1]
		errArr.append([
			i,
			calcErr(tempTheta0, tempTheta1, data, nRow, avg)
		])
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
		with open("theta.csv", "w") as file:
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
	dataFile = pd.read_csv("data.csv")
	if (validate(dataFile)):
		mins = dataFile.min()
		maxs = dataFile.max()
		average = dataFile.mean()[1]
		normData = normalize(dataFile, mins, maxs)
		theta = train(normData, average)
		theta = denorm(theta)
		writeTheta(theta)
		ax = plt.subplot()
		ax.set_xlabel(dataFile.columns.values[0])
		ax.set_ylabel(dataFile.columns.values[1])
		ax.set_title("data value and linear regression")
		ax.plot(dataFile[dataFile.columns.values[0]], dataFile[dataFile.columns.values[1]], "r*")
		ax.plot([mins[0], maxs[0]], [calculate(theta, mins[0]), calculate(theta, maxs[0])])
		# ax.plot(errData["iter"], errData["err"])
		plt.show()
	else:
		print("\033[31mFatal: \"data.csv\" is corrupted!\033[0m")
except:
	print("\033[31mFatal: \"data.csv\" not found, we can not train the alghorithm!\033[0m")