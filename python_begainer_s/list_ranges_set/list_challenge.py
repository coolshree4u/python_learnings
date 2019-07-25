#add to the program below so that if it finds a meal without spam
#it prints out each of the ingredients of the meal
# You will need to set up the menu as did given below

menu=[]
menu.append(["eggs","spam","bacon"])
menu.append(["eggs","susage","bacon"])
menu.append(["eggs","spam"])
menu.append(["eggs","bacon","spam"])
menu.append(["spam","susage","eggs","bacon","spam"])
menu.append(["spam","eggs","spam","bacon","spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)
