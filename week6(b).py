import os
my_file=open("my_file.txt","w+")
print(os.access('my_file.txt', os.R_OK)) 
print(os.access('my_file.txt', os.W_OK))
print(os.access('my_file.txt', os.X_OK))
print(os.access('my_file.txt', os.F_OK))