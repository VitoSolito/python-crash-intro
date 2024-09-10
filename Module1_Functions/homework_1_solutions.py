
def ex_1_0(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

def ex_1_0_show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)


def ex_1_1(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

def ex_2(list1, list2):
    for x, y in zip(list1, list2[::-1]):
        print(x, y) 