import statistics
fobj = open("dravid.txt","r")
strike_rates = []
for line in fobj:
    columns = line.split()
    runs = int(columns[2])
    balls = int(columns[3])
    strike_rate = runs/balls*100
    strike_rates.append(strike_rate)
deviation = statistics.stdev(strike_rates)
print(deviation)

