def longest(str1):
    windowstart = 0
    max_length = 0
    char_frequency = {}

    for windowend in range(len(str1)):
        right_char = str1[windowend]

        if right_char not in char_frequency:
            char_frequency[right_char] = windowend
            max_length = max(max_length, windowend - windowstart + 1)
        else:
            windowstart = max(windowstart, char_frequency[right_char] + 1)

    return max_length

def main():
    output = longest("aabccbb")
    output2 = longest("abbbb")
    output3 = longest("abccde")
    print(output)
    print(output2)
    print(output3)

main()

