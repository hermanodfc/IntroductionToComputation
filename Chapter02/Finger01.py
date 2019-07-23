x = int(input("Enter a number (x): "))
y = int(input("Enter a number (y): "))
z = int(input("Enter a number (z): "))

max_odd_number = -1

if x % 2 == 1 and x > max_odd_number:
    max_odd_number = x
    letter_name = "x"
if y % 2 == 1 and y > max_odd_number:
    max_odd_number = y
    letter_name = "y"

if z % 2 == 1 and z > max_odd_number:
    max_odd_number = z
    letter_name = "z"

print()
if max_odd_number != -1:
    print("%s = %d is largest odd number." % (letter_name, max_odd_number))
else:
    print("No odd numbers have been entered.")