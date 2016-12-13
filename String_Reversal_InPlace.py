def reverse_list(letters, first=0, last=None):
    if last is None:
        last = len(letters)
    last -= 1
    while first < last:
        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1
    print ''.join(letters)   
s = raw_input()
reverse_list(list(s))