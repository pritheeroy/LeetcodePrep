def fruits(arr):
    k = 2

    windowstart = 0
    max_fruit = 0
    tree_frequency = {}

    for windowend in range(len(arr)):
        right_tree = arr[windowend]
        
        if right_tree not in tree_frequency:
            tree_frequency[right_tree] = 0
        
        tree_frequency[right_tree] += 1

        while len(tree_frequency) > k:
            left_tree = arr[windowstart]
            tree_frequency[left_tree] -= 1

            if tree_frequency[left_tree] == 0:
                del tree_frequency[left_tree]
            windowstart += 1
        
        max_fruit = max(max_fruit, windowend - windowstart + 1)

    return max_fruit

def main():
    output = fruits(['A', 'B', 'C', 'B', 'B', 'C'])
    print(output)

main()
