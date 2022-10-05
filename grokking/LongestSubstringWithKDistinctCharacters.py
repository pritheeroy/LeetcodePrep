def longest(k, str):
    max_length = 0
    windowstart = 0 
    char_frequency = {}

    for windowend in range(len(str)):
        right_char = str[windowend]

        if right_char not in char_frequency:
            char_frequency[right_char] = 0

        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str[windowstart]
            char_frequency[left_char] -=1

            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowstart += 1

        max_length = max(max_length, windowend - windowstart + 1)

    return max_length

def main():
    output = longest(2, "araaci")
    print(output)

main()

