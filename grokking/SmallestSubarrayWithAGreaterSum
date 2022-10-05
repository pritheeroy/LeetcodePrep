import math
def smallest(s, arr):
    windowsum = 0
    windowstart = 0
    minlength = math.inf
    
    for windowend in range(0, len(arr)):
        windowsum += arr[windowend]

        while windowsum >= s:
            minlength = min(minlength, windowend - windowstart + 1)
            windowsum -= arr[windowstart]
            windowstart += 1
    if minlength == math.inf:
        return 0
    return minlength

def main():
    outputs = smallest(7, [2, 1, 5, 2, 3, 2])
    print(outputs)

main()