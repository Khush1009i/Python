# nested loop = a loop within another loop(outer, inner)
# outer loop:
#       inner loop:

# one loop in another loop;

# #exapmle:
for x in range(3): 
    for y in range(1,4):
        print(y, end=" ")    
    print()


# Example:- Let's create a rectangle using nested loops:-

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows): 
    for y in range(columns):
        print(symbol, end=" ")    
    print()
