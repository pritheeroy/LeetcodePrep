
def longest(str1, k):
    windowstart = 0
    max_length = 0
    max_char_count = 0
    char_frequncy = {}

    for windowend in range(len(str1)):
        right_char = str1[windowend]

        if right_char not in char_frequncy:
            char_frequncy[right_char] = 0
        
        char_frequncy[right_char] += 1

        max_char_count = max(max_char_count, char_frequncy[right_char])

        if (windowend - windowstart + 1 - max_char_count) > k:
            left_char = str1[windowstart]
            char_frequncy[left_char] -= 1
            windowstart += 1

        max_length = max(max_length, windowend - windowstart + 1)

    return max_length

    
    


def main():
    output = longest("aabccbb", 2)
    output2 = longest("abbcb", 1)
    output3 = longest("abccde", 1)
    print(output)
    print(output2)
    print(output3)

main()