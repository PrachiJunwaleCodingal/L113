def reverse_bits_bitwise(n):
    reversed_n = 0
    while n > 0:
        reversed_n <<= 1
        # If the last bit of n is 1, add 1 to the result
        if (n & 1) == 1:
            reversed_n |= 1
        # Shift n right to process the next bit
        n >>= 1
    return reversed_n

num = 10  # Binary: 1010
print(f"Reversed Number: {reverse_bits_bitwise(num)}") # Output: 5 (Binary: 0101)
