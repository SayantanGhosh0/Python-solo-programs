'''
 opening files in both ways and reading it and writing in it.
'''

#myfile = open("filename.txt", "r")
with open("filename.txt") as f:
    print(f.read())
#cont = f.read()
#print(cont)
f.close()
myfile = open("filename.txt", "w")
msg=" Hi There"
myfile.write("This is written in the text file")
amt = myfile.write(msg)
print(amt)
myfile.close()
