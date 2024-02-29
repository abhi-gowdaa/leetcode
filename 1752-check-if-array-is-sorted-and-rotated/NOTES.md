​This line creates a new list rotated_nums by concatenating two slices of the original list nums:

nums[i + 1:]: This slice starts from the element at index i + 1 and includes all elements up to the end of the list. It represents the rotated portion of the array.

nums[:i + 1]: This slice starts from the beginning of the list and includes elements up to index i. It represents the portion of the array that was moved to the end during rotation.

By concatenating these two slices, we effectively restore the original order of the array.

For example, consider the rotated array [3, 4, 5, 1, 2]. If i = 2, then nums[i + 1:] will be [1, 2] (the rotated portion), and nums[:i + 1] will be [3, 4, 5] (the portion that was moved to the end during rotation). Concatenating these slices gives us [1, 2, 3, 4, 5], which is the sorted original array.

The next part of the line:
return rotated_nums == sorted(rotated_nums)
