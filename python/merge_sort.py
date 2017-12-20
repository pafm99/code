import random

random_items = [random.randint(-50, 100) for c in range(20)]


def merge_sort(items):
    if(len(items) > 1):
        mid = len(items)/2
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        for i in range(len(items)):
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if(lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif(lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')


print('Before: ', random_items)
merge_sort(random_items)
print('After: ', random_items)