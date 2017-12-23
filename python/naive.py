# What is this algorithm doing?
# Answer: multiplies a * binfile
# Has linear time complexity. because the while loop runs the same times as the value of a 

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z
    
print(naive(4,5))