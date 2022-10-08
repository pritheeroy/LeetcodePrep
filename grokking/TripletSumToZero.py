def search_triplets(arr):
    output = []
    arr.sort()

    for a in range(len(arr)):
        if a > 0 and arr[a] == arr[a - 1]:
            continue

        left = a + 1
        right = len(arr) - 1

        while left < right:
            curr_sum = arr[a] + arr[left] + arr[right]

            if curr_sum == 0:
                output.append([arr[a], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1 
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1
    return output
                
def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()