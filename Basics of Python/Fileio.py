# File I/O : used to perform opt an a file.(read & write)
# Types of files : 
# |-> Text = (.txt, .docx, .log, etc) 
# |-> Binary = (.mp4, .mov,.png, etc)
#|---------|---------------------------------------------|
#|character| Meaning                                     |
#|"r" |open for reading                                  |
#|"w" |open writing, truncating the file first           |
#|"x" |create a new file &open it for working            |
#|"a" |open for writing, append, to end of file if exist |
#|"b" |binary mode                                       |
#|"t" |text mode(default)                                |
#|"+" |open disk file for uploading                      |
#|----|--------------------------------------------------|

#open read & close file:
# data = f.read(5) # read whole data in the file.
# print(data)


# #Reading file:
# line1 = f.readline() #-> read only one line at a time.
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()

# # Write to any file:
f = open("C:/Users/KHUSH SONI/python/Basics of python/demos.txt", "a")
f.write("I want to learn node js")
f.close()

f = open("sample.txt", "w")
f.close()

f = open("sample.txt", "r+")
f.write(" abc")
# f.write("This file re created using 'w' tag ")
f.close()

# #with syntax
# with open("C:/Users/KHUSH SONI/python/Basics of python/demos.txt","r") as f: #as == alias
data = f.read()
print(data)


# Deleting a file:
# for deletin file we use modules the OS modules. Module is a file written by another programmer that 
# genrally has a fuxn we can use:

import os
os.remove("sample.txt")


count =0
with open("practise.txt", "r") as f:
        data = f.read()
        print(data)

        num = ""
        for i in range(len(data)):
            if (data[i] == ","):
                print(int(num))
                num = ""
            else:
                num += data[i]   
                break     
             
nums = data.split(",") 
for val in nums:
     if(int(val)%2 == 0):
        count += 1
print(count)

# count_the_number()
