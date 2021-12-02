n=open("C:\\Users\\dilee\\OneDrive\\py_lab_5F4\\file_1.txt","r+")
n.write("hello world")
n.seek(0)
print(n.read())