list1 = [22, 2, 23, 34, 56, 67]
list2 = [72, 83, 24, 2, 14]

def find_2nd_largest_from_2_Lists(l1):
  largest = l1[0]
  secondLargest = l1[0]
  for i in range(len(l1)):
    if (l1[i] > largest):
      largest = l1[i]
  for j in range(len(l1)):
    if (l1[j] > secondLargest and l1[j] < largest):
      secondLargest = l1[j]
  print(largest, secondLargest)
  
find_2nd_largest_from_2_Lists(list2)
