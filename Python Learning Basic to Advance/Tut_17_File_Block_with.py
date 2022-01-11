#Not need to use close file

with open("pardeep.txt") as f:
    a = f.read(10)
    print(a)