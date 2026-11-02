with open ("test.txt" , "w") as f : 
    f.write("hello\n")
    f.write("world\n")
with open ("test.txt" , "r") as f :
    content = f.read()
print(content)
print(type(content))