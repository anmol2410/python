# Function Defination
def greet(name):
    print("Hey "+name)


# Function Calling
greet("Anmol")

# Addition by return statement
def add(a,b):
    return a+b
    # by default python return None

# parameter act as placeholder
# 1.postional argument by default (agument means the actual value we supply)
# 2.Keyword argument (a=4,b=2)
# Keyword argument should always come after postinal arguments(7,a=9)

result=add(b=4,a=6)
print("sum : ",result)

# Reusable function
def emoji_converter(message):
    
    words=message.split(" ")
    emojis={
        # Win+semicolon for emojis
        ":)":"😊",
        ":(":"😞"
    }
    output=""
    for word in words:
        output +=emojis.get(word,word)+" "
    return output


message=input(">")
res=emoji_converter(message)
print(res)

# Exceptions
try:
    age=int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')