# Format- specifiers = {:flags} format a vlaue based on what flags are intrested

# .(num)f = round to many dec places(fied point).
# :(num)  = allocates that many spaces.
# :03     = allocates & zero pad that many spaces
# :<      = left justify
# :>      = right justify
# :^      = center align
# :+      = use a plus sign to indicates postive value
# :=      = place sign to leftmost postion
# :       = insert a space before positive numb
# :,      = comma seprator

price1 = 3000.1415
price2 = -9870.868
price3 = 1200.34

print(f"Price1 is ${price1:,.2f}") 
print(f"Price2 is ${price2:,.2f}") 
print(f"Price3 is ${price3:,.2f}") 