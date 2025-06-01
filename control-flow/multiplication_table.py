
number = int(input("Enter a number to see its multiplication table: "))

6
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
