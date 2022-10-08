import math


def triplet_sum_close_to_target(arr, target):
    arr.sort()
    curr_closest = math.inf

    for a in range(len(arr)):
        if a > 0 and arr[a] == arr[a - 1]:
            continue

        left = a + 1
        right = len(arr) - 1

        while left < right:

            curr_diff = target - arr[a] - arr[left] - arr[right]

            if abs(curr_diff) < abs(curr_closest) or (abs(curr_diff) == abs(curr_closest) and curr_diff > curr_closest):
                curr_closest = curr_diff
            if curr_diff > 0:
                left += 1
            else:
                right -= 1
    return target - curr_closest


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
  print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))


main()