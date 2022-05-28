numbers = [12, 4, 2, 4, 9, 23, 2, 23, 50, 10, 4, 5, 12, 3]
uniques = []
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)