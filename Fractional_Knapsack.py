#uses python3
import sys
def sort(weights,values):
    listVW=list()
    for i in range(0,len(weights)):
        listVW.append(values[i]/weights[i])
    newList=zip(listVW,weights) 
    return sorted(newList,reverse=True) 
    
def get_optimal_value(capacity, weights, values):
    value = 0
    sortedList=sort(weights,values)
    for i in range(0,len(sortedList)):
        if capacity==0:
            return value
        for j,k in sortedList:  
            a = min(k,capacity)
            value = value + a * j
            k = k-a
            capacity-=a

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))    