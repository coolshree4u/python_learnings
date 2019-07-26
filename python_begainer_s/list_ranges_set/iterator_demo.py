string='123456789'
for i in string:
    print(i)

my_iterator=iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print("Normal string")
for char in string:
    print(char)

print("After iterator")
for char in iter(string):
    print(char)