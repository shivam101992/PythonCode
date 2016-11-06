#Uses python3

import sys

def min_dot_product(a, b):
    sortedL1=sorted(a,reverse=True)
    sortedL2=sorted(b)
    sum1=0
    for i in range(0,int(n)):
        sum1+=sortedL1[i]*sortedL2[i]
    return sum1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
