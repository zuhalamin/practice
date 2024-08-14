import os
input_file= open("practice/test.txt","r")

print(input_file.read())
input_file.seek(0)
print(input_file.readline())
input_file.seek(0) #move the carser at the start of file 
print(input_file.readlines())

#with w we can make new file and overwriting any existing content
output_file = open("practice/result.txt","w")

output_file.write("Hi,my name is bazza.\n")
output_file.write("I am good."+"\n")
output_file.writelines(['Yes','NO'])

#This is make directory we can make a folder
os.mkdir('file1')
os.listdir("C:/")
os.remove('file1')
os.rename('file1','file2')
os.path.exists('tasks')

input_file.close()


