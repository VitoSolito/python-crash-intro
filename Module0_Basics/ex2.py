'''Given two lists of numbers, write a Python code to create a new list such that the latest list 
should contain odd numbers from the first list and even numbers from the second list.'''

def main():
    l1 = [1,2,3,4,5,6]
    l2 = [7,8,9,10,11,12]
    l=[]
    for i in range(0,len(l1)):
        if l1[i]%2!=0:
            l.append(l1[i])

    for i in range(0,len(l2)):
        if l2[i]%2==0:
            l.append(l2[i])
    print(l)

main()