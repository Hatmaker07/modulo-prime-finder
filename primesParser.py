primeFile = open("1stmillionPrimes.txt", "r")
primesList = []
primes = primeFile.readline()
parsedFile = primes.split(",")
primes = "" # memory management? in my high level language? imposiible!
for i in range (0,len(parsedFile)-1):
    primesList.append(int(parsedFile[i]))
parsedFile = [] # yet more memory management in python lmfao
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

