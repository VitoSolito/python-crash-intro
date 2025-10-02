def factorial(n):
    sol=1
    if n==0 : return 1
    for i in range (1,n+1):
        sol*=i
    return sol


def main():
    print(factorial(100))

main()