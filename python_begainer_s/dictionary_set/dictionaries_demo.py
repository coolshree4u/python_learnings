fruits={
    "orange":"a sweet, organage, citrus fruit",
    "apple":"good for making cider",
    "lemon":"a sour, yellow citrus fruit",
    "grape":"a small, sweet fruit growing in bunches",
    "lime":"a sour, green citrus fruit"
}

print(fruits)
print(fruits['apple'])


bike={
    "make":"Honda",
    "model":"Unicorn 150",
    "color":"red",
    "cubic capacity":"150"
}

print(bike)
print(bike["make"])
print(bike["color"])
bike["makeyear"]=2018
print(bike)

ordered_keys=sorted(list(bike.keys()))

ordered_keys.sort()
for i in ordered_keys:
    print(i," - ",bike.get(i))

# while True:
#     dict_key=input("Please enter attribute : ")
#     if dict_key =='quit':
#         break
#     if dict_key in bike.keys():
#         dict_desc = bike.get(dict_key)
#         print(dict_desc)
#     else:
#         print(dict_key," is not present")


print(bike.items())
print("Iterating dictionary")
for item in bike.items():
    item_description=item
    print("Item description is ",item_description)

print(fruits)
print(bike)

fruits.update(bike)
print(fruits)

test_bike={"model_name":"rx100","brand_name":"Yamaha"}
new_copy_bike=bike.copy()
print(new_copy_bike)
new_copy_bike.update(test_bike)
print("Verifying new copy  ",new_copy_bike)
print("Verifying old copy  ",bike)