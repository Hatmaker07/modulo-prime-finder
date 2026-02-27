primeFile = open("1stmillionPrimes.txt", "r")
primesList = []
primes = primeFile.readline()
parsedFile = primes.split(",")
for i in range (0,len(parsedFile)-1):
    primesList.append(int(parsedFile[i]))
print("parsed")
while True:
    try:
        index = input()
        index = int(index)
        print(primesList[index-1])
    except:
        if index == "q":
            break
        else:
            print("try again\n if you want to exit this promgram, enter q")
#TODO: add a mode to find if a number is prime (if in the list)

#DONE: add a quit option
