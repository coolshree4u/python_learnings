i=0
while i<10:
    print("i is now {}".format(i))
    i+=1

available_exits=['east','north-east','south']

exists=''
while exists not in available_exits:
    exists=input("Please choose a direction")
    if exists == 'quit':
        print("game over")
        break

print("Aren't you glad you got out there")