course='Python for "Beginners"'
print(course) # """hello multi line string """
print(course[-2]) # negative and postive indexing
print(course[0:6:2]) # slicing 
another=course[:] # copy

#Exercise
name='Jennifer'
print(name[1:-1])

first='john'
last='smith'
message=first+' [' +last +'] is a coder' # unformtted string
msg=f'{first} [{last}] is a coder' # f' ' -> formatted string
print(msg)