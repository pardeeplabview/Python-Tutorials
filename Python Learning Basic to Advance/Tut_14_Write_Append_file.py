# File Write Append

# c = open("pardeep.txt","a")
# # print(c.read())
# c.write("ok pardeep how are you")
# c.close()

c = open("pardeep.txt","r+")
print(c.read())
c.write("ok pardeep how are you")
c.close()