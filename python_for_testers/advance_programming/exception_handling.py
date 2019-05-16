input1=input("Please enter your first marks")
input2=input("Please enter your second marks")

try:
    print(int(input1)+int(input2))
except:
    print("Your input is incorrect")
finally:
    print("Closing all resources")