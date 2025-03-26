nums = [5, 3, 8, 1, 2]
print("Starting list:", nums)
swapped = True

while swapped:
  swapped = False # Set swapped to False here
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]: # Compare nums[i] and nums[i + 1]  
        temp = i
        i = i + 1 # Swap them if needed
        i + 1 = temp
        swapped = True # Don’t forget to mark swapped = True if you do a swap
print("Sorted list:", nums)

