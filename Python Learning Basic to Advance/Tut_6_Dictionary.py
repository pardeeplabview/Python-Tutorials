#Dictionary Items

o = {"p":"10","A":"20","C":"99","D":"65",
     "Pardeep":{"Live":"Panchkula","Age":"23"}}
print(o["Pardeep"])

o["E"] = "57" #add
print(o)

del o["E"] #Delete
print(o)

#Accessing Items
deepi = {"brand": "Ford","model": "Mustang","year": 1964}
l = deepi.get("year")
print(l)

#Keys
x = deepi.keys()
print(x)

#change
deepi["year"] = "9999"
print(deepi)

#Update
deepi.update({"model": "Lovely"})
print(deepi)

#Add Items
deepi["Pardeep"] = "Labview"
print(deepi)

#Remove items
deepi.pop("brand")
#del deepi["model"]
#deepi.clear()
print(deepi)

#loop
for x in deepi.keys():
  print(x)
for x in deepi.values():
  print(x)

#Project
container = {"A":"1","B":"2","C":"3","D":"4"}
print("Search word(A,B,C,D):->")
jaanvi = input()
print(container[jaanvi])





