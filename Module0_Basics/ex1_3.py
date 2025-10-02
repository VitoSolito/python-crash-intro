''' Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

solution("PYnative", 4) so output must be **tive**. 
Here, you need to remove the first four characters from a string.

solution("PYnative", 2) so output must be **native**. 
Here, you need to remove the first two characters from a string.
Note: n must be less than the length of the string. '''

def solution(s, n):
    if n>=len(s):
        exit("n must be less than the len of string")
    return s[n:]

def main():
    str=solution("Inferenza",3)
    print(str)

main()