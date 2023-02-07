x = 0
while x == 0:
    try:
        x = int(input("Enter number: "))
        x += 5
        print(x)
    except ValueError:
        print("Better enter number!")



