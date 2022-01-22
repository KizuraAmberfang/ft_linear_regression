from srcs.train import train

t = train("data/data.csv", 10000, 1/100)
t.run()
t.print()