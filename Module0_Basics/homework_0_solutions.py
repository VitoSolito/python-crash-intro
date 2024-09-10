
def ex_1_1():
    print("Printing current and previous number and their sum in a range(10)")
    previous_num = 0

    # loop from 1 to 10
    for i in range(1, 11):
        x_sum = previous_num + i
        print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
        # modify previous number
        # set it to the current number
        previous_num = i


def ex_1_2(word:str):
    print("Original String:", word)

    # get the length of a string
    size = len(word)

    # iterate a each character of a string
    # start: 0 to start with first character
    # stop: size-1 because index starts with 0
    # step: 2 to get the characters present at even index like 0, 2, 4
    print("Printing only even index chars")
    for i in range(0, size - 1, 2):
        print("index[", i, "]", word[i])

def ex_1_3(word:str, n:int):
    print('Original string:', word)
    x = word[n:]
    print("Truncated string:", x)
    return x


def ex_2(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list


def ex_3(str1):
    # create a result dictionary
    char_dict = dict()

    for char in str1:
        count = str1.count(char)
        # add / update the count of a character
        char_dict[char] = count
    print('Result:', char_dict)


def ex_4(start, end):
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        # all prime numbers are greater than 1
        # if number is less than or equal to 1, it is not prime
        if num > 1:
            for i in range(2, num):
                # check for factors
                if (num % i) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                print(num)


def ex_5(num=5, factorial=1):
    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        # run loop 5 times
        for i in range(1, num + 1):
            # multiply factorial by current number
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)