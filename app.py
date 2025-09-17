# file =("numbers.txt")
# print(file.read())
# print()
# file_content = file.read()
# print(file_content)
# file.close()

# file = open("colors.txt", "x")


favorite_code = input("Enter your favorite code: ")

file_name = input("Enter a file name to save your code: ")

with open(file_name, "w") as f:
    f.write(favorite_code)

print(f"Your code has been saved in {file_name}")
