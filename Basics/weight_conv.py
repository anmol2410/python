weight=int(input("Enter your weight:"))
weight_in=input("(L)bs or (K)g:")

if weight_in=='l' or weight_in=='L':
    print(f'you are {0.454*weight} kilos')
elif weight_in=='k' or weight_in=='K':
    print(f'you are {weight/0.45} pounds')
else:
    print("Enter weight in kg or lbs")