my_list=list(range(0, 10))
print(my_list)

even=list(range(0,10,2))
odd=list(range(1,10,2))
print(even)
print(odd)


my_string='abcdefghijklmnopqrstuvwxyz'
print(my_string.index('o'))
print(my_string[4])


small_decimal=range(0,10)
print(small_decimal)
print(small_decimal.index(3))

odd = range(1,1000,2)
print(odd)
print(odd[98])


sevens=range(7,1000000,7)
x=int(input("Please enter number less than one million"))
if x in sevens:
    print("{} is divisible by seven".format(x))