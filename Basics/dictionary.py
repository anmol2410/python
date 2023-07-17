customer={
    "name": "Anmol",
    "age": 21,
    "is_verified":True
}
# Accessing by the key
print(customer["name"])
print(customer.get("age"))
print(customer.get("birthdate","july 21 2003")) # return deafault value
customer["name"]="radhika"
print(customer)




