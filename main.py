import os, shutil
#
# n = int(input())
# language = []
#
# for _ in range(n):
#     k = int(input()) # количество языков
#     buff = set() # множество для хранения языков
#     for _ in range(k):
#         buff.add((input()))
#         language.append(buff) # добавление всех введёных языков
#
# unic = set.union(*language) # объеденение
# intersec = set.intersection(*language) # пересечение множеств, изучаемй язык всеми учениками
#
# print(len(intersec), '\n'.join(sorted(intersec)), len(unic), '\n'.join(sorted(unic)), sep='\n')



# def F(word):
#     count = 0
#     for i in word:
#         if i == i.capitalize():
#             count += 1
#
#     return count == 1
#
#
# d = {}
# n = int(input())
# for _ in range(n):
#     word = input()
#     d[word.capitalize()] = d.get(word.capitalize(), []) + [word]
#
# word = input().split()
# error = 0
#
# for w in word:
#     if w.capitalize() in d:
#         if w not in d[w.capitalize()]:
#             error += 1
#     else:
#         if F(w) == False:
#             error += 1
#
# print(error)
#


# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def searchBoys():
    for adress, dirs, files in os.walk(input()):
        for file in files:
            if file.endswith('.txt') and 'GirlsNames' not in file:
                yield os.path.join(adress, file)

def searchGirl():
    for adress, dirs, files in os.walk(input()):
        for file in files:
            if file.endswith('.txt') and 'BoysNames' not in file:
                yield os.path.join(adress, file)


#     a[fileLines[0]] = int(fileLines[1])
#/Users/andreypc/Desktop/KursovoyProekt/BabyNames

nameBoys = []
nameGirl = []
a = {}
b = {}
for i in searchBoys():
    fileLines = open(i,'r').readline().split(' ')

    try:
        if a[fileLines[0]] < int(fileLines[1]):
            a[fileLines[0]] = int(fileLines[1])
    except: a[fileLines[0]] = int(fileLines[1])


print(a)


for i in searchGirl():
    fileLines = open(i,'r').readline().split(' ')

    try:
        if b[fileLines[0]] < int(fileLines[1]):
            b[fileLines[0]] = int(fileLines[1])
    except:b[fileLines[0]] = int(fileLines[1])

print(b)























