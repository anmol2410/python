for x in range(3):
    for y in range(2):
        print(f'({x},{y})')

#Exersice
for i in range(5):
    if(i==0 or i==2):
        print("****")
    else:
        print("**")

lst=[2,2,2,5,5]
for s in lst:
    print(s*"x")

for row in lst:
    output=''
    for col in range(row):
        output+="x"
    print(output)
