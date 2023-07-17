names=['Anmol','Radhika','prince','Sarah']
names[2]='Prince'
print(names[0::2 ])

# Write a program to find largest number in a lsit
lst=[22,57,96,102,45,7,444]
max=lst[0]
for i in lst:
    if(i>=max):
        max=i
print(max)
