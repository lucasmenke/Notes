listOfNumbers = []

for i in range(10):
    if i % 2 == 0:
        listOfNumbers.append(i)

print(listOfNumbers)

def printAllNumbersToN(n):
    for i in range(n+1):
        print(i)

printAllNumbersToN(10)