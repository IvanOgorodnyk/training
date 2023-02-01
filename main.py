def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

    return min_number

nums1 = [5 ,7, 8 ,1.5]
min1 = minimal(nums1)

nums2 = [5.5, 7.4, 8, 1.9, 2.4]
min2 = minimal(nums2)


if min1 < min2:
    print(min1)
else:
    print(min2)