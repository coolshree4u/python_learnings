import time
time.sleep(5)
print("Printing after 5 seconds")


word= "bottles"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall")
    print(beer_num, word, "of beer.")
    print("Take One down")
    print("Pass it around")
    if beer_num == 1:
        print("NO more bottles of beer on the well")
    else:
        new_num = beer_num -1;
        if new_num == 1:
            word= 'bottle'
        print(new_num, word, "of beer on the well")
    print()
