import math
def find_substring(str1, pattern):
    pattern_frequency = {}
    windowstart = 0
    min_length = len(str1) + 1
    num_matched = 0
    substring_start = 0

    for chr in pattern:
        if chr not in pattern_frequency:
            pattern_frequency[chr] = 0
        
        pattern_frequency[chr] += 1

    for windowend in range(len(str1)):
        right_char = str1[windowend]

        if right_char in pattern_frequency:
            pattern_frequency[right_char] -= 1
            if pattern_frequency[right_char] >= 0:
                num_matched += 1
        
        while num_matched == len(pattern):
            if min_length > windowend - windowstart + 1:
                min_length = windowend - windowstart + 1
                substring_start = windowstart

            left_char = str1[windowstart]
            windowstart =+ 1

            if left_char in pattern_frequency:
                if pattern_frequency[left_char] == 0:
                    num_matched -= 1
                pattern_frequency[left_char] += 1

    if min_length > len(str1):
        return ""

    return str1[substring_start:substring_start + min_length]

def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()

        

