# You are given an array and some number S. Determine if any three numbers within the array sum to S.

def threeSum(arr, S):
  arr = sorted(arr)
  for i in range(0, len(arr) - 2):
    # start two pointers, one from the current position + 1 # and the other at the end of the array
    ptr_start, ptr_end = i + 1, len(arr) - 1
    while ptr_start < ptr_end:
      add = arr[i] + arr[ptr_start] + arr[ptr_end]
      # if we find a sum
      if add == S: return True
      # if the sum < S
      elif add < S: ptr_start += 1 # if the sum > S
      else:
        ptr_end -= 1
  return False
