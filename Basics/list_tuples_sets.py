#List
courses=['phy','maths','compsci','eng']
print(courses)
print(courses[0])
#negative indexing 
print(courses[-1])
#len function
print(len(courses))
#Slicing
print(courses[2:])

#-------list Methods---------

#Adding element in list---
courses.append('hindi') #Add element at last of the list
print(courses[0:])

courses.insert(2,'his') #Add element to the particular loaction
print(courses[0:])

cou=['art','education']

courses.extend(cou) #it extend the orginal list and do not create new list of list
print(courses[0:])

#Deleting element in the list-----

#remove() delete the specfic element 
courses.remove('art')
print(courses[0:])

#pop() delete the lat element of the list
popped=courses.pop()
print(courses[0:])

#reverse()
courses.reverse()
print(courses[0:])

#sort
courses.sort()
print(courses[0:])

lst=[23,34,4,23,1,21]
lst.sort() #Asending order by default
print(lst[0:])

lst.sort(reverse=True) #Descending order
print(lst[0:])

#sorted() return sorted version of list which can be store in variable
sortt=sorted(lst)
print(sortt)
#  min()
#  max()
#  sum()

#for getting index of element
print(lst.index(23))

# in
print('maths' in courses) 

#looping
for i in courses:
    print(i)

# enumureate for getting index and values both
for index,values in enumerate(courses,start=1): #you can change index value using start
    print(index,values)

#list to string 
course_str=', '.join(courses) #using join method
print(course_str)

#string to list using split()
course_lst=course_str.split(' - ')
print(course_lst)

#Tuples - Immutable (not changeable)
