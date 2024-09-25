n = int(input("Enter a number: "))

print("Odd numbers between 1 and", n, "are:")
for i in range(1, n + 1):
    if i % 2 != 0:  # Check if the number is odd
        print(i)