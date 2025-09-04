#for loops: execute a block of code a fixedd num of times.
#          You can iterate over a range, string, seq, etc.


# Basic syntax of for:

# counting :
# for x in range(1,11):
#     print(x)
 
# reverse counting:
# for x in reversed(range(1,11)):
#     print(x)

# print("Happy New Year ")

# credit_card = "1234-3654-4544-1231"

# for x in credit_card:
#     print(x)

for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)