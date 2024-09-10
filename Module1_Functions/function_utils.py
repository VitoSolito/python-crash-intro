
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def show_player(name: str, score: int): # we can suggest argument type (no error will be given)
    if not isinstance(name, str):
        raise TypeError
    if not isinstance(score, int):
        raise TypeError
    print("name:", name, "score:", score)

def max_search(x:list):
    assert isinstance(x, list) # check that x is a list variable
    # initialize the maximum as the first element of the list
    max=x[0] 
    index = 0

    for i in range(1, len(x)):
        if x[i] > max:
            max = x[i]
            index = i

    return max, index

def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    return res