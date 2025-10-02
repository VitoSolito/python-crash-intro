'''Print all prime numbers within a range.

Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

Examples:

6 is not a prime number because it can be made by 2×3 = 6

37 is a prime number because no other whole numbers multiply to make it.'''

def prime(n1,n2):
    l = []
    for number in range(n1,n2+1):
        if number==1 : continue
        for i in range (2,number+1):
            if i==number :
                l.append(number)
                break
            if number%i==0 : break

    return l

def main():
    l = prime(2,100)
    print(l)

main()