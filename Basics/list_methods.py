num=[5,2,1,7,4]
# append() at the last
num.append(8)
print(num)
# insert(index,value) to insert at particular loc
num.insert(0,10)
print(num)
# remove() any element
num.remove(5)
print(num)
# clear() emepty list
num.clear()
print(num)
num=[5,2,1,7,4]
# pop() remove elment at last
num.pop()
print(num)
# existenece of number index()
print(num.index(7))

# in operators is also used for existence
print(10 in num) # Return boolean value

# counting elemnt count()
print(num.count(1))
# sort() method not rerurn any value only sort in ascending
print(num.sort())
num.sort()
print(num)
# reverse()
num.reverse()
print(num)

# copy() of a  list
newlst=num.copy()
print(newlst)

# Exercise -->> remove the duplicate element
newlst.insert(0,1)
newlst.insert(2,1)
unique=[]
for number in newlst:
    if number not in unique:
        unique.append(number)

print(unique)

  
