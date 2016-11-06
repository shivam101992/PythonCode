import re

fh = f.open("regex_sum_42.txt", r)

numlist = list()

for line in fh:
    line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) < 1: continue
    numlist.append(int(x))

finalSum = numlist.sum()
print finalSum
