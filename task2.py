str1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89]
str2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89]
joinstr = list(set(str1) & set(str2))
print(joinstr)
