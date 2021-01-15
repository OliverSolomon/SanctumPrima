from math import sqrt

function = int(input("\t Please Key in the number of what you want to do \t \n\t\t [ 0 ] Find if number is a prime \n\t\t [ 1 ] Get ALL prime numbers upto a certain number \n\n :--><: "))

number = int(input("Please enter number for evaluation: "))#172
listOfPrimes = [2,3]


def isPrime(num):

    #main idea behind checking if a number is prime is: if you divide the number with all the primes between its squareroot nd two and get no remainder for any of the quotients, then the number is prime. Like Wanhera ;-) //its a "The 100 joke"

    for i in range(2,int(sqrt(number))+1):
        mod = number%i
        if mod == 0:
            print(f"\n{number} is not a prime")
            break
        else:
            if i == int(sqrt(number)) :
                print(f"{number} is prime")

# isPrime(number)

"""List of primes between 2 and the given number"""

def getPrimes(num):
    for j in range(0, number+1):

        for i in range(2,int(sqrt(j))+1):
            mod = j%i
            if mod == 0:
                # print(f"\n{j} is not a prime")
                break
            else:
                if i == int(sqrt(j)) :
                    # print(f"{j} is prime")
                    listOfPrimes.append(j)

    print(listOfPrimes)

# getPrimes(number)

if function == 0:
    isPrime(number)
elif function == 1:
    getPrimes(number)
else:
    print("Invalid Choice, restart program")