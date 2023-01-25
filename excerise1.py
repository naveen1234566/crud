l1 = [4,2,13,21,5]
l2 = []

for i in l1:
    temp = lambda i:i**2

    l2.append(temp(i))

print(l2)

l2 = list(map(lambda v : v** 2, l1))
print(l2)

# list of square fo odd numbers
l1 = [4,2,13,21,5]
l2 = []
l2 = list(map(lambda v: v ** 2, filter(lambda u: u%2,l1)))
print(l2)

# using del()methode
mydict = {1:'geeks', 2:'for', 3:'geeks'}
# for key in mydict.keys():
#     if key == 2:
#         del mydict[key]
# print(mydict)

# creating a list of keys to delete
delete = [key for key in mydict if key == 3]

for key in delete:
    del mydict[key]

print(mydict)

# new to list comprehensions:

dict =  {1:'geeks', 2:'for', 3:'geeks'}
delete = []
for key in dict:
    if key == 3:
        delete.append(key)

for i in delete:
    del dict[i]

print(dict)

for key in list(dict):
    if key == 2:
        del dict[key]

print(dict)