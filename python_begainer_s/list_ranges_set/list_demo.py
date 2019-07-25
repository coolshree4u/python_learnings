even=[2,4,6,8]
odd=[1,3,5,7,9]
numbers=odd+even
print(numbers)


numbers.sort()
print("Numbers with sorted manner")
print(numbers)
numbers=even+odd
print(sorted(numbers))

if numbers==sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")

list1=[]
list2=list()

print("list1: {}".format(list1))
print("list2: {}".format(list2))

if list1 == list2:
    print("The lists are equal")

print(list("The lists are equal"))



even=[2,4,6,8]
another_even=even
print(another_even is even)

another_even.sort(reverse=True)
print(even)

list_even=list(even)
print(list_even)
list_even.sort()
print(even)
print(list_even)

