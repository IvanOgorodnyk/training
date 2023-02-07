try:
    with open("txt.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")