#For loop

"""
deep = ["pardeep","deep","labview"]
for pardeep in deep:
    print(pardeep)
"""
"""
deep = [["pardeep",1],["deep",2],["labview",3]]
for pardeep in deep:
    print(pardeep)
"""
"""
deep = [["pardeep",1],["deep",2],["labview",3]]
for pardeep,jaanvi in deep:
    print(pardeep,jaanvi)
"""
"""
deep = [["pardeep",1],["deep",2],["labview",3]]
a = dict(deep)
for pardeep in a.items():
    print(pardeep)
"""
"""
deep = [["pardeep",1],["deep",2],["labview",3]]
a = dict(deep)
for pardeep,jaanvi in a.items():
    print(pardeep,jaanvi)
"""

# a = [11,44,22,7,4,0,22,"pardeep","deep"]
# for deep in a:
#     if str(deep).isnumeric():
#         print(deep)

for x in range(2, 6):
  print(x)
