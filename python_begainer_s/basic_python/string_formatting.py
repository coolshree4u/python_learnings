age =24
print("My age is "+str(age)+" years")
print("My age is {0} years".format(age))


print("my age is %d years"%age)

for i in range(1,12):
    print("No. %2d squared is %4d and Cubed is %4d"%(i, i*i, i*i*i))

print("Pi is approximately %12.50f"%(22/7))


for i in range(1,12):
    print("No. {0:2} squared is {1:4} and Cubed is {2:4}".format(i, i**2, i**3))
