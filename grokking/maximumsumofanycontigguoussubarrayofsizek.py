def maxsum(k, arr):
    WindowSum = 0
    WindowStart = 0
    Max_sum = 0

    for WindowEnd in range(len(arr)):
        WindowSum += arr[WindowEnd]

        if WindowEnd >= k - 1:
            Max_sum = max(Max_sum, WindowSum)
            WindowSum -= arr[WindowStart]
            WindowStart += 1
            
    return Max_sum

def main():
    
    result = maxsum(2, [2, 3, 4, 1, 5])
    print(result)

main()

