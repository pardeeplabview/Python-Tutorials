# File Seek() and Tell()

f = open("pardeep.txt")
print(f.readline())
print(f.tell()) # define wwhere is your pointer
print(f.readline())
f.seek(15) # start from this value
print(f.readline())