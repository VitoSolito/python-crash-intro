'''Write a program to count occurrences of all characters within a string. 
The outcome should be contained in a dictionary.'''
import operator
def main():
    s="Pedissequamente"
    d={}
    for i in range(0,len(s)):
        letter = s[i]
        if letter not in d.keys():
            d[letter]=1
        else:
            d[letter]+=1

    l = sorted(d.items(), key = operator.itemgetter(0) )
    print(dict(l))

main()    