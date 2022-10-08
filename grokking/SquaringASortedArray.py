def make_squares(arr):
    output_arr = [0 for x in range(len(arr))]
    right = len(arr) - 1
    highest_square_index = len(arr) - 1
    left = 0

    while right > left:
        left_squared = arr[left]*arr[left]
        right_squared = arr[right]*arr[right]

        if right_squared > left_squared:
            output_arr[highest_square_index] = right_squared
            highest_square_index -= 1
            right -= 1
        else:
            output_arr[highest_square_index] = left_squared
            highest_square_index -= 1
            left += 1
    
    return output_arr

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
  
main()


