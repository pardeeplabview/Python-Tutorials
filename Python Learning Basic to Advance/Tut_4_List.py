# Tutorial_4
"""
List
"""

#mutable - can change
#immutable - cannot chnage

pardeep = [11,23,45,13,0,99]
print(pardeep)


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change List Iteams
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Index
thislist = ["apple", "don", "pardeep"]
thislist.pop(1)
print(thislist)

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Loop List
thislist = ["pardeep1", "www", "re"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
