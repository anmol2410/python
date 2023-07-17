# Tuples are immutable but similar to lsit ()

tup=(5,7,6)
print(tup)
print(tup.count(5))
print(tup.index(5))

# Unpacking
cord=(1,2,3)
# cord[0]*cord[1]*cord[2]
x=cord[0]
y=cord[1]
z=cord[2]
print(x*y*z)

# to acheive same result we have in python concept of unpacking 
a,b,c=cord
print(a*b*c)

