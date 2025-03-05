# Range = returns a seq of num, starting from 0 by default
#  & increaement by 1 &, stops before specified num.
# range(start?(optional), stop, step?(optional))

seq = range(5)# ending is one less thanthe range
for i  in seq:
    print(i)



for i in range(2,100,2):
    print(i)

#as per user desire (even number)
a= 0
b= int(input("enter the value u want to end: "))
for j in range(a,b,2):
    print(j)


