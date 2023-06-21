# Print Welcome message 
print('Helllo World.......') #using single ' ' or doble " "
print("using double quotes")
print("my father's name") #either by double " " or \
print('my pet\'s name') # \ ignore the single ' 


#---------------STRING -------------------------------
message="Hello World"
print(message+" using string vrible") #using string vrible
# finding length of string  using len() inbuilt function
print(len(message))
#Acces element of string using index value 0 to len-1
print(message[10])
#range of index
print(message[0:5]) #0 is including and last index is exculding 
#you can also leave first index when strtung from beginng
print(message[:5]) #same incase of ending
print(message[6:]) #it is called slicing

# Methods or functions in python
print(message.upper())
print(message.lower())
print(message.count('o'))
print(message.find('W')) # return index if present otherwise return -1
print(message.replace('World',"Universe")) 
#concatinate
gretting="Good"
day="morning"
print(gretting+" "+day)
#format dtring using place holder
new_message='{} {} welcome!'.format(gretting,day)
print(new_message)
#f string
new_message=f'{gretting} {day} welcome!'
print(new_message)
#dir method to see our prev. methods
print(dir(message))
#help method
print(help(str))
#for specific method
print(help(str))