#Function and Docstring
# def pardeep(a,b):
#     """You can add any two integer"""
#     sum = a+b
#     print(sum)
#     return sum
#
# def deep(a,b):
#     """You can subtract any two integer"""
#     sub = a-b
#     print(sub)
#     return sub

# pardeep(2,2)
# print(deep.__doc__)

# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my(*kids):
  print("The youngest child is " + kids[1])
my("Emil", "Tobias", "Linus")

#Create Function
def my_function1():
  print("Hello from a function")


#Calling a function
def my_function2():
  print("Hello from a function")
my_function2()


#Number of argument
def my_function3(fname, lname):
  print(fname + " " + lname)
my_function3("Emil", "Refsnes")


#keyword argument
def my_function4(child3, child2, child1):
  print("The youngest child is " + child3)
my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linu")

#Passing list any argument
def my_function5(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function5(fruits)

#Return Values
def my_function6(x):
  return 5 * x
print(my_function6(3))