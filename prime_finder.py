import math as m
import time as t
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
currentNum = 37
counter = 0
def closest_value(arr, k):
    n = len(arr)
    low, high = 0, n - 1
    # Step 1: Binary search
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
        # Exact match → return immediately
            return arr[mid]
        elif arr[mid] < k:
            low = mid + 1
        else: high = mid - 1
    # Step 2: low and high are the two closest "neighbors"
    candidates = []
    if high >= 0:
        candidates.append(arr[high])
    if low < n:
        candidates.append(arr[low])
    # Step 3: Compare candidates by distance to k
    best = candidates[0]
    for value in candidates[1:]:
        if abs(value - k) < abs(best - k):
            best = value
        elif abs(value - k) == abs(best - k):
            best = max(best, value)
        # tie-breaker: pick the greater value
        return best
while True:
    try:
        InputRange = int(input("max prime number to search to\n"))
        break
    except:
        print("try again")
while True:
    try:
        InputTime = int(input("max time to run for\n"))
        break
    except:
        print("try again")
start = t.time()
while len(primes) < InputRange and t.time() - start < InputTime:
    for c in range (0,100):
        isPrime = True
        currentNum += 2
        limit = closest_value(primes, m.ceil(m.sqrt(currentNum)))
        try:
            limitIndex = primes.index(limit)
        except ValueError:
            limitIndex = 12
        for j in range (0,limitIndex+1):
            if currentNum % primes[j] == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(currentNum)
end = t.time()
print(end-start)
print("found the first ", len(primes), " primes")
savePrimes = False
while True:
    try:
        usrInput = input("write to file?\n(y)es (n)o\n")
        if usrInput == "y":
            savePrimes = True
            break
        elif usrInput != "y":
            savePrime = False
            break
    except:
        print("try again")
if savePrimes == True:
    with open("like, a lot of primes.txt",mode="w") as file:
        for i in range (0,len(primes)-1):
            line = (str(primes[i]))
            line += ","
            file.write(line)
        file.flush()
        file.close()
        print("write complete")
while True:
    try:
        index = input()
        index = int(index)
        print(primes[index-1])
    except:
        if index == "q":
            break
        else:
            print("try again")
