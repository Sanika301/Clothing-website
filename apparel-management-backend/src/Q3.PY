# Initialize the first term and common ratio
first_term = 2
common_ratio = 3
number_of_terms = 6

# Generate and print the terms of the geometric sequence
geometric_sequence = [first_term * (common_ratio ** i) for i in range(number_of_terms)]
print("The first 6 terms of the geometric sequence are:")
print(" ".join(map(str, geometric_sequence)))
