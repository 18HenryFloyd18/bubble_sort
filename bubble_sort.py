# REFLECTION QUESTIONS

# 1: The algorithm knows to stop looping when the swapped variable gets swapped to false after the if statement determines that there is no longer any thing that needs to be sorted because the -1 in the if statement will make sure that it will go until the variable that has already been sorted

# 2: It will run through the code until it determines that is has already been sorted through using the if statement until there is no more values left to use.

# 3:The purpose of the swapped variable is to keep swapping and going through the list until there is no more numbers to be swapped; meaning that it gets set to false and then exits out of the while loop and prints the updated list.

# 4: It is important to understand the algorithm before writing to ensure a fast and smooth coding process where you know what things do and can quickly anylyze problems and solve them.

nums = [5, 3, 8, 1, 2]
print("Starting list:", nums) # print the starting list
swapped = True # set the variable to true

while swapped:
  swapped = False # Set swapped to False here
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]: # Compare nums[i] and nums[i + 1]  
        temp = nums[i]
        nums[i] = nums[i + 1] # Swap them if needed
        nums[i+ 1] = temp
        swapped = True # Don’t forget to mark swapped = True if you do a swap
print("Sorted list:", nums) # Print the sorted list
