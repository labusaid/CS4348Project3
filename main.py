import time
from queue import Queue

schedulerFile = open('example.sf', 'r')
algorithm = schedulerFile.readline()

elapsedTime = 0

processQueue = Queue()

processFile = open('example.pf', 'r')

processes = processFile.readlines()

for process in processes:
    processList = process.split()
    # print(processList)
    # handle processList based on selected algorithm
    if algorithm == 'FCFS\n':
        i = 1
        while i < len(processList):
            elapsedTime += int(processList[i+1])
            i+=2

print(f'elapsedTime: {elapsedTime}')