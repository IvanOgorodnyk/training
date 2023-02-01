#data = set("hello")
data = {5, 7, 4, 8, 3, 5}

data.add(21)
data.update([123, True, 66, 2])
data.remove(True)
data.pop()
#data.clear()

nums = [5, 7, 3, 5, 5]
new_nums = set(nums)

new_data = frozenset([123, True, 66, 2, 5, 7, 3, 5, 5])


print(new_data)