# prime number finder to find the nth prime.

prime numbers are identified by taking the square root of the current number being tested (sqrt(currentNum)), 
and finding the closest prime number in a list of precomputed prime numbers, then testing to see if currentNum modulo every prime less than or equal to the square root of currentNum.
