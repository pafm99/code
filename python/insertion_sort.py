import random

random_items = [random.randint(-50, 100) for c in range(20)]


def insertion_sort(items):
    for i in range(len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1


print("Before: ", random_items)
insertion_sort(random_items)
print("After: ", random_items)