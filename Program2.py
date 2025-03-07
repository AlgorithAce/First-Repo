# Function to swap two numbers using XOR
def swap_using_xor(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

# Example usage
x = 5
y = 10
x, y = swap_using_xor(x, y)

