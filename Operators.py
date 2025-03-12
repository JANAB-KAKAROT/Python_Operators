# Arithmetic Operators
x = 10
y = 3
print("Add:", x + y)
print("Minus:", x - y)
print("Times:", x * y)
print("Divide:", x / y)
print("Leftover:", x % y)
print("Power:", x ** y)
print("Whole Divide:", x // y)

# Assignment Operators
a = 5
a += 3
print("Now a is:", a)

a *= 2
print("Now a is:", a)

# Comparison Operators
print("Same:", x == y)
print("Not Same:", x != y)
print("Bigger:", x > y)
print("Smaller:", x < y)
print("Big or Same:", x >= y)
print("Small or Same:", x <= y)

# Logical Operators
p = True
q = False
print("Both True:", p and q)
print("One True:", p or q)
print("Opposite:", not p)

# Identity Operators
m = [1, 2, 3]
n = [1, 2, 3]
z = m
print("Same Thing:", m is z)
print("Not Same Thing:", m is not n)

# Membership Operators
print("Has:", 2 in m)
print("No Has:", 5 not in m)

# Bitwise Operators
x = 5
y = 3
print("Bits AND:", x & y)
print("Bits OR:", x | y)
print("Bits XOR:", x ^ y)
print("Flip Bits:", ~x)
print("Move Left:", x << 1)
print("Move Right:", x >> 1)
