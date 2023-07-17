phone=input("Phone : ")
digit_text={
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "four"
}
output=""
for ch in phone:
    output=output+digit_text.get(ch,"!")+" "

print(output)