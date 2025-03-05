# # Recursion : when a funxn call itself repeatedly.
def shows(n):
    if(n == 0):  #base case
        return
    print(n)
    shows(n-1)
shows(5)
# shows(3)

def fact(a):
    if(a == 1 or a==0):
        return 1
    else:
        return fact(a-1) * a
    
print(fact(5))
