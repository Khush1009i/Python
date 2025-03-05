
# Escape sequence character == Formatting (next line )
# - for next line == \n
# - for tab space == \t
str1 = "Hello, My self Khush Soni\n"
str2 = "I am from Merta City."
# print(str1)

# concatination == adding two string in python.
print(str1 + str2)

# length of str == len()
# len1= len(str1)
# len2= len(str2)
# print(len1)
# print(len2)
print(len(str1))
print(len(str2))

#Indexing == Every character got index or got a popsition.
str = "Khush Soni"
ch = str[0]
print(ch)
print(str[9])

# Slicing == accessing parts of a string.
# example == str[strtng_indx : endng indx ]
# backward couting can be also done by using " - " in the index.
print(str[ : 6])
print(str1[: 6])
print(str2[6 : 10])
print( str2[-5 : -1] )