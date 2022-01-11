
#Access Tuple Iteam
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Range of Indxes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Changer Value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Unpacking A Tuple
fruits = ("apple", "banana", "cherry")
(pardeep, deep, labview) = fruits
print(labview)

#Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

