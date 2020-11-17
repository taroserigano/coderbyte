'''


Prime Mover
HIDE QUESTION
Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. For example: if num is 16 the output should be 53 as 53 is the 16th prime number.

Use the Parameter Testing feature in the box below to test your code with different arguments.


"[3, 1, 3, 5, 10, 6, 4, 3, 1]"

'''

def IsPrime(number):
    for i in range(2, number / 2 + 1):
        if number % i == 0:
            return False
    return True

def PrimeMover(num):
    prime = [1, 2]

    if num in prime:
        return num + 1
    i = 1
    while len(prime) < num + 1:
        number = prime[-1] + i
        if IsPrime(number):
            i = 1
            prime.append(number)
        else:
            i += 1
    return number
# keep this function call here  
print PrimeMover(raw_input())