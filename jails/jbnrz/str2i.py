def string_to_int_array(s):
    return [ord(c) for c in s]

# Example usage:
your_string = "flag.txt"
result = string_to_int_array(your_string)
print(result)
