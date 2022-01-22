all:	train calc

calc:
		python3 srcs/calculate.py

train:
		python3 srcs/train.py