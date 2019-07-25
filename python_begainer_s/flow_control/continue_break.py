shopping_list=['milk','pasta','eggs','spam','bread','rice','carrot']
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring "+item)
        continue
    print(item)

print("printing using break")
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring "+item)
        break
    print(item)



meal=['egg','bacon','span','susage']
for item in meal:
    if item == 'spam':
        nasty_food_item=item
        break

if nasty_food_item:
    print("Can't I have anything without spam in it")

