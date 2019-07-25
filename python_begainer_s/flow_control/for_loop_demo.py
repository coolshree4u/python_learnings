for i in range(0,10):
    print("i is now {}".format(i))

number="9,223,558,669,789,987"
for i in range(0,len(number)):
    print(number[i])

number="9,223,558,669,789,987"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')



number="9,223,558,669,789,987"
clean_number=''
for char in number:
    if char in '0123456789':
        clean_number=clean_number+char

new_number=int(clean_number)
print("\nThe number is {}".format(new_number))


for state in ["not pinin","not more","a stiff","bereft of life"]:
    print("This parrot is "+state)


for i in range(0,100,5):
    print("i is {}".format(i))


for i in range(1,13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i,j, i*j), end='\t')
    print("")
