try:
   x = 5 / 1
   x = int(input())
except ZeroDivisionError:
    print("dilenie na 0")
except ValueError:
    print("you have entered something wrong")
else:
    print("else")
finally:
    print("finally")


