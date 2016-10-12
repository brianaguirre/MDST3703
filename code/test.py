__author__ = 'BrianAguirre'


def unique_vals(diction):
    list1 = []
    for i in diction:
        if (diction[i] not in list1):
            list1.append(diction[i])

    return list1


dict1 = {"x":["a", "b", "c"], "y":["a","b"], "z":"b", "c":["a", "b", "c", "d"], "a":["a", "b", "c", "d"]}

print(unique_vals(dict1))

sizes = []

for i in dict1.keys():
    if len(dict1[i]) not in sizes:
        sizes.append(len(dict1[i]))

print(sizes)