def longest(arr, k):
    windowstart = 0
    max_length = 0
    max_one_count = 0

    for windowend in range(len(arr)):
        if arr[windowend] == 1:
            max_one_count += 1

        if (windowend - windowstart + 1 - max_one_count) > k:
            if arr[windowstart] == 1:
                max_one_count -= 1

            windowstart += 1
        max_length = max(max_length, windowend - windowstart + 1)

        return max_length