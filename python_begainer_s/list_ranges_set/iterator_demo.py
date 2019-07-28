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

days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days_iterator=iter(days)
for i in range(0, len(days)):
    day_item=next(days_iterator)
    print(day_item)