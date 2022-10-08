def anagram(str1, pattern):
    pattern_frequency = {}
    windowstart = 0
    num_matched = 0
    results = []

    for chr in pattern:
        if chr not in pattern_frequency:
            pattern_frequency[chr] = 0
        pattern_frequency[chr] += 1

    for windowend in range(len(str1)):
        right_char = str1[windowend]

        if right_char in pattern_frequency:
            pattern_frequency[right_char] -= 1
            if pattern_frequency[right_char] == 0:
                num_matched += 1

        if num_matched == len(pattern_frequency):
            results.append(windowstart)

        if windowend >= len(pattern) - 1:
            left_char = str1[windowstart]
            windowstart += 1

            if left_char in pattern_frequency:
                if pattern_frequency[left_char] == 0:
                    num_matched -= 1
                pattern_frequency[left_char] += 1

    return results


def main():
    print(anagram("ppqp", "pq"))
    print(anagram("abbcabc", "abc"))


main()
    