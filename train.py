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

def train(data):
    theta = [0, 0]
    lr = 1/100
    nRow = data.count()[0]
    for i in range(10000):
        tempTheta0 = theta[0] - (lr * (1/nRow) * sumError(data, theta))
        tempTheta1 = theta[1] - (lr * (1/nRow) * sumWeightError(data, theta))
        theta = [tempTheta0, tempTheta1]
    return theta

def denorm(theta):
    rangeX = maxs[0] - mins[0]
    rangeY = maxs[1] - mins[1]
    tempTheta1 = theta[1] * (rangeY / rangeX)
    tempTheta0 = theta[0] * rangeY - theta[1] * (rangeY / rangeX) * mins[0] + mins[1]
    return [tempTheta0, tempTheta1]

def writeTheta(theta):
	try:
		with open("theta.csv", "x") as file:
			file.write("theta0,theta1\n")
			file.write(str(theta[0]) + "," + str(theta[1]) + "\n")
	except:
		print("Error: could not create \"theta.csv\".")


dataFile = pd.read_csv("data.csv")
mins = dataFile.min()
maxs = dataFile.max()
normData = normalize(dataFile, mins, maxs)
theta = train(normData)
theta = denorm(theta)
writeTheta(theta)
plt.plot(dataFile[dataFile.columns.values[0]], dataFile[dataFile.columns.values[1]], "r*")
plt.plot([mins[0], maxs[0]], [calculate(theta, mins[0]), calculate(theta, maxs[0])])
plt.show()